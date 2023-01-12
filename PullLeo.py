import six
import json
import requests
from lxml import etree
from io import StringIO
import argparse
from tabulate import tabulate
import sys

# lang= sys.argv[3]
LangOut = sys.argv[2]
LangIn = sys.argv[3]

arg_parser = argparse.ArgumentParser(
    description="Query the leo.org German/English dictionary.",
    epilog="Note that the developers of this software are in "
           "no way affiliated with leo.org."
)
arg_parser.add_argument('query',
                        metavar='search-term',
                        nargs='+',
                        help="word(s) to search for")
arg_parser.add_argument('-j', '--json',
                        action='store_true',
                        default=False,
                        help='Format results as JSON.')


section_names = (
    'subst',
    'verb',
    'adjadv',
    'preaep',
    'definition',
    'phrase',
    'example',
)


def _get_text(elt):
    buf = StringIO()

    def _helper(_elt):
        if _elt.text is not None:
            buf.write(six.text_type(_elt.text))
        for child in _elt:
            _helper(child)
        if _elt.tail is not None:
            buf.write(six.text_type(_elt.tail))

    _helper(elt)
    return buf.getvalue()


web = "https://dict.leo.org/" + LangOut + LangIn
def search(term, uri=web):
    resp = requests.get(uri, params={'search': term})
    p = etree.HTMLParser()
    html = etree.parse(StringIO(resp.text), p)
    ret = {}
    for section_name in section_names:
        section = html.find(".//div[@data-dz-name='%s']" % section_name)
        if section is None:
            continue
        ret[section_name] = []
        results = section.findall(".//td[@lang='" + LangOut +"']")
        for r_en in results:
            r_de = r_en.find("./../td[@lang='" + LangIn +"']")
            ret[section_name].append({
                LangOut : _get_text(r_en).strip(),
                LangIn : _get_text(r_de).strip(),
            })
    return ret


def main():
    args = arg_parser.parse_args()
    query = ' '.join(args.query)
    results = search(query)
    if args.json:
        print(json.dumps(results))
    else:
        for section_name in results.keys():
            print(section_name)
            print("==========" + query + "==========")
            table = [[r[LangOut], r[LangIn]] for r in results[section_name]]
            print(tabulate(table, headers=[LangOut, LangIn]))


if __name__ == '__main__':
    main()

# text = arg_parser(metavar='book')
# print(text)