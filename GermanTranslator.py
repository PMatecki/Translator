import subprocess
import sys
import ast
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

LangInput = "de"
LangOutput = "pl"

root = Tk()
root.title('PrzemekTranslator')
root.geometry("1000x1000")

#er hat sich mit einer kleinen, wunderbaren Frau und sein kluger Onkel getroffen

# Prepare text boxes
EntryBox = Text(root, width=45, borderwidth=5, height=8)
EntryBox.grid(row=0, rowspan=4, column=0, columnspan=2, padx=10, pady=30)
EntryBoxScrollBar= Scrollbar(root, command=EntryBox.yview, orient="vertical")
EntryBoxScrollBar.grid(row=0, rowspan=4, column=0, columnspan=2, padx=3, pady=30, sticky="nse")
EntryBox.configure(yscrollcommand=EntryBoxScrollBar.set)

GoogleTranslationBox = Text(root, width=45, borderwidth=5, height=8)
GoogleTranslationBoxScrollBar= Scrollbar(root, command=GoogleTranslationBox.yview, orient="vertical")
GoogleTranslationBoxScrollBar.grid(row=0, rowspan=4, column=3, columnspan=3, padx=3, pady=30, sticky="nse")
GoogleTranslationBox.grid(row=0, rowspan=4, column=2, columnspan=2, padx=10, pady=30)
GoogleTranslationBox.configure(yscrollcommand=GoogleTranslationBoxScrollBar.set)
# GoogleTranslationBox.scrollbar.grid(row=0, column=2, rowspan=2,  sticky=N+S+W)
GoogleTranslationBox.insert(END, "Can't touch this")
GoogleTranslationBox.config(state=DISABLED)

# Create box with tabs
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Nouns')
tabControl.add(tab2, text='Adjectives')
tabControl.add(tab3, text='Verbs')
tabControl.grid(row=12, rowspan=8, column=0, columnspan=5, padx=3, pady=30, sticky="nse")

# Label(tab1, text= 'Welcome to GeeksForGeeks').grid(column=0, row=20, padx=30, pady=30)
# Label(tab2, text= 'Lets dive into the world of computers').grid(column=0, row=20, padx=30, pady=30)

LeoTranslationBox = Text(tab1, width=95, borderwidth=5, height=20, wrap="none")
LeoTranslationBox.grid(row=18, rowspan=8, column=0, columnspan=5, padx=10, pady=30)
LeoTranslationBox.insert(END, "<Nouns translated with Leo.org dictionary will be displayed here>")
LeoTranslationBoxScrollBar= Scrollbar(tab1, command=LeoTranslationBox.yview, orient="vertical")
LeoTranslationBoxScrollBar.grid(row=18, rowspan=8, column=3, columnspan=2, padx=3, pady=30, sticky="nse")
LeoTranslationBox.configure(yscrollcommand=LeoTranslationBoxScrollBar.set)
LeoTranslationBoxScrollBarX= Scrollbar(tab1, command=LeoTranslationBox.xview, orient="horizontal")
LeoTranslationBoxScrollBarX.grid(row=18, rowspan=8, column=0, columnspan=5, padx=0, pady=2, sticky="sew")
LeoTranslationBox.configure(xscrollcommand=LeoTranslationBoxScrollBarX.set)
#LeoTranslationBoxScrollBarHorizontal= Scrollbar(tab1, command=LeoTranslationBox.yview, orient="horizontal", width=20)
#LeoTranslationBoxScrollBarHorizontal.grid(row=19, rowspan=1, column=0, columnspan=5, padx=15, pady=10, sticky="sew")
#LeoTranslationBox.configure(yscrollcommand=LeoTranslationBoxScrollBarHorizontal.set)
LeoTranslationBox.config(state=DISABLED)

LeoTranslationBox2 = Text(tab2, width=95, borderwidth=5, height=20, wrap="none")
LeoTranslationBox2.grid(row=12, rowspan=8, column=0, columnspan=5, padx=10, pady=30)
LeoTranslationBox2.insert(END, "<Adjectives translated with Leo.org dictionary will be displayed here>")
LeoTranslationBox2ScrollBar= Scrollbar(tab2, command=LeoTranslationBox2.yview, orient="vertical")
LeoTranslationBox2ScrollBar.grid(row=12, rowspan=8, column=3, columnspan=2, padx=3, pady=30, sticky="nse")
LeoTranslationBox2.configure(yscrollcommand=LeoTranslationBox2ScrollBar.set)
#LeoTranslationBox2ScrollBarHorizontal= Scrollbar(tab2, command=LeoTranslationBox2.yview, orient="horizontal", width=20)
#LeoTranslationBox2ScrollBarHorizontal.grid(row=19, rowspan=1, column=0, columnspan=5, padx=15, pady=10, sticky="sew")
#LeoTranslationBox2.configure(yscrollcommand=LeoTranslationBox2ScrollBarHorizontal.set)
LeoTranslationBox2.config(state=DISABLED)

LeoTranslationBox3 = Text(tab3, width=95, borderwidth=5, height=20, wrap="none")
LeoTranslationBox3.grid(row=12, rowspan=8, column=0, columnspan=5, padx=10, pady=30)
LeoTranslationBox3.insert(END, "<Verbs translated with Leo.org dictionary will be displayed here>")
LeoTranslationBox3ScrollBar= Scrollbar(tab2, command=LeoTranslationBox3.yview, orient="vertical")
LeoTranslationBox3ScrollBar.grid(row=12, rowspan=8, column=3, columnspan=2, padx=3, pady=30, sticky="nse")
LeoTranslationBox3.configure(yscrollcommand=LeoTranslationBox3ScrollBar.set)
#LeoTranslationBox3ScrollBarHorizontal= Scrollbar(tab2, command=LeoTranslationBox3.yview, orient="horizontal", width=20)
#LeoTranslationBox3ScrollBarHorizontal.grid(row=19, rowspan=1, column=0, columnspan=5, padx=15, pady=10, sticky="sew")
#LeoTranslationBox3.configure(yscrollcommand=LeoTranslationBox3ScrollBarHorizontal.set)
LeoTranslationBox3.config(state=DISABLED)

# Prepare radio buttons
TranslationWay = [
        ("DE->PL", "DE->PL"),
        ("PL->DE", "PL->DE"),
        ("ENG->DE", "ENG->DE"),
    ]

l = []

lng = StringVar()
lng.set("DE->PL")

for index, tuple in enumerate(TranslationWay):
    l.append(TranslationWay[index])
    for text, mode in l:
        Radiobutton(root, text=text, variable=lng, value=mode).grid(row=4, rowspan=1, column=index, columnspan=1,
                                                                    padx=50, pady=10)

SelectedTranslationWay = lng.get()

# Prepare checkboxes
Nouns = StringVar()
Adjectives = StringVar()
Verbs = StringVar()

N =Checkbutton(root, text="Nouns", variable=Nouns, onvalue="y", offvalue="n")
N.select()
N.grid(row=7, column=0, columnspan=1, padx=10, pady=10)

A =Checkbutton(root, text="Adjectives", variable=Adjectives, onvalue="y", offvalue="n")
A.select()
A.grid(row=7, column=1, columnspan=1, padx=10, pady=10)

V =Checkbutton(root, text="Verbs", variable=Verbs, onvalue="y", offvalue="n")
V.select()
V.grid(row=7, column=2, columnspan=1, padx=10, pady=10)

# Function to clear textboxes
def ClearBoxes():
    EntryBox.delete(1.0,END)
    GoogleTranslationBox.config(state=NORMAL)
    GoogleTranslationBox.delete(1.0,END)
    GoogleTranslationBox.insert(END, "<Translation from Google Translator will be displayed here>")
    GoogleTranslationBox.config(state=DISABLED)
    LeoTranslationBox.config(state=NORMAL)
    LeoTranslationBox.delete(1.0, END)
    LeoTranslationBox.config(state=DISABLED)
    LeoTranslationBox2.config(state=NORMAL)
    LeoTranslationBox2.delete(1.0, END)
    LeoTranslationBox2.config(state=DISABLED)
    LeoTranslationBox3.config(state=NORMAL)
    LeoTranslationBox3.delete(1.0, END)
    LeoTranslationBox3.config(state=DISABLED)

#Tłumaczenie z Google Translator
def GoogleTranslate():
    global LangInput
    global LangOutput
    global TextToTranslate
    global SelectedTranslationWay
    global Nouns
    global Adjectives
    global Verbs

    TextToTranslate = EntryBox.get("1.0", END)
    SelectedTranslationWay = lng.get()

    GoogleTranslationBox.config(state=NORMAL)
    GoogleTranslationBox.delete(1.0, END)
    GoogleTranslationBox.config(state=DISABLED)
    LeoTranslationBox.config(state=NORMAL)
    LeoTranslationBox.delete(1.0, END)
    LeoTranslationBox.config(state=DISABLED)
    LeoTranslationBox2.config(state=NORMAL)
    LeoTranslationBox2.delete(1.0, END)
    LeoTranslationBox2.config(state=DISABLED)
    LeoTranslationBox3.config(state=NORMAL)
    LeoTranslationBox3.delete(1.0, END)
    LeoTranslationBox3.config(state=DISABLED)

    if SelectedTranslationWay == "DE->PL":
        LangInput = "de"
        LangOutput = "pl"

    if SelectedTranslationWay == "PL->DE":
        LangInput = "pl"
        LangOutput = "de"

    if SelectedTranslationWay == "ENG->DE":
        LangInput = "en"
        LangOutput = "de"

    create3 = [sys.executable, 'GoogleTransPull.py', TextToTranslate, LangOutput, LangInput]
    f = subprocess.run(create3, shell=False, stdout=subprocess.PIPE)
    e = f.stdout.decode()
    GoogleTranslationBox.config(state=NORMAL)

    GoogleTranslationBox.insert(END, e)

    if LangOutput == "de":
        TextToTranslate = GoogleTranslationBox.get("1.0", END)

    # Detect word types using HanoverTagger from HanTa
    create2 = [sys.executable, 'GermanTranslatorDEPL.py', TextToTranslate]
    p = subprocess.run(create2, shell=True, stdout=subprocess.PIPE)
    x = p.stdout.decode()

    # print(TextToTranslate)
    print(x)

    # Split bulk string received from GermanTranslatorDEPL.py into separate strings
    phrase_to_list = x.split('\n')
    StringAllWords = phrase_to_list[0]
    StringNounsOriginal = phrase_to_list[1]
    StringNounsInfinitiv = phrase_to_list[2]
    StringAdjOriginal = phrase_to_list[3]
    StringAdjInfinitiv = phrase_to_list[4]
    StringVerbOriginal = phrase_to_list[5]
    StringVerbInfinitiv = phrase_to_list[6]

    # Change strings defined in previous step into lists
    StringsToLists = [StringNounsInfinitiv, StringAdjInfinitiv, StringVerbInfinitiv]

    for i in range(len(StringsToLists)):
        StringsToLists[i] = ast.literal_eval(StringsToLists[i])
        StringsToLists[i] = [n.strip() for n in StringsToLists[i]]

    # print(StringsToLists[0])
    # Not used at the moment
    NounList = StringsToLists[0]
    AdjList = StringsToLists[1]
    VerbList = StringsToLists[2]

    # Call Leo.org
    if LangInput == "de" or LangOutput == "de":
        def CallLeo(WordsToCheck, WordTab):
            global LangInput
            global LangOutput
            for v in WordsToCheck:
                LangInputX = LangInput
                LangOutputX = LangOutput

                #tu trzeba wykombinować obsłużenie przypadku gdzie langoutput to DE
                if LangInputX != "de":
                    LangOutputX = LangInputX
                    LangInputX = "de"
                create = [sys.executable, 'PullLeo.py', v, LangOutputX, LangInputX]
                a = subprocess.run(create, shell=True, stdout=subprocess.PIPE)
                b = a.stdout.decode()
                # print(b)
                if WordTab == "Nouns":
                    print(b)
                    LeoTranslationBox.config(state=NORMAL)
                    #LeoTranslationBox.delete(1.0, END)
                    LeoTranslationBox.insert(END, b)
                    LeoTranslationBox.config(state=DISABLED)
                elif WordTab == "Adjectives":
                    LeoTranslationBox2.config(state=NORMAL)
                    #LeoTranslationBox2.delete(1.0, END)
                    LeoTranslationBox2.insert(END, b)
                    LeoTranslationBox2.config(state=DISABLED)
                elif WordTab == "Verbs":
                    LeoTranslationBox3.config(state=NORMAL)
                    #LeoTranslationBox3.delete(1.0, END)
                    LeoTranslationBox3.insert(END, b)
                    LeoTranslationBox3.config(state=DISABLED)

        # Checkboxes for Nouns Adjecives & verbs check in Leo.org
        NounChecked = Nouns.get()
        AdjChecked = Adjectives.get()
        VerbChecked = Verbs.get()

        # Define what word types will be queried from Leo.org
        if NounChecked == "y":
            WordType = "Nouns"
            CallLeo(StringsToLists[0], WordType)
        if AdjChecked == "y":
            WordType = "Adjectives"
            CallLeo(StringsToLists[1], WordType)
        if VerbChecked == "y":
            WordType = "Verbs"
            CallLeo(StringsToLists[2], WordType)
# else -> crate pop up informing about missing entry in textbox

    # myLabel= Label(root, text=Nouns.get()+Adjectives.get()+Verbs.get()).grid(row=20, column=0, columnspan=3, padx=10, pady=10)

TranslateButton = Button(root, text="Translate", command=GoogleTranslate).grid(row=5, column=0, columnspan=3, padx=10, pady=10)
ClearButton = Button(root, text="Clear", command=ClearBoxes).grid(row=5, column=1, columnspan=3, padx=10, pady=10)

root.mainloop()