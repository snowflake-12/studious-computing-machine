#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

focused = False
translated = False
check_input = ""

def reset():

    global focused, translated
    focused = False
    translated = False

    plain_morse.delete("1.0", END)
    plain_morse.insert("1.0", "Type your message here, either normal letters, numbers and punctuation or Morse code using '.' for a dot, '-' for a dash, separating letters by spaces and words by '/'.", END)
    plain_morse.configure(fg = "grey")
    result.configure(text = "The translated message appears here with '#' for an untranslatable character.")
    reset_btn.focus()

def ready_translate(event):

    global translated, focused

    if not translated:

        plain_morse.delete("1.0", END)
        plain_morse.configure(fg = "black")

        focused = True

def input_done(event):

    if plain_morse.get() == 0:

        pass

def enter_pressed(event):

    translate()

def translate():

    global focused, translated

    plainmorse = (plain_morse.get("1.0", END)).upper()

    default_text = "Type your message here, either normal letters, numbers and punctuation or Morse code using '.' for a dot, '-' for a dash, separating letters by spaces and words by '/'."

    if (plainmorse == default_text.upper() + "\n") or (focused and plainmorse == "\n"):

        messagebox.showerror("EMPTY FIELD!!!", "Please Enter A Message In The Text Field.")
        plain_morse.delete("1.0", END)
        plain_morse.insert("1.0", default_text)

    elif focused and plainmorse != default_text.upper():

        morse_plain_mix = check(plainmorse)
        translated = True

        if morse_plain_mix:

            text_morse(plainmorse)

        else:

            morse_text(plainmorse)

def check(text):

    result = False

    checker = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@?()=,:'\""

    for i in range(0, len(text)):

        for j in range(0, len(checker)):

            if text[i] == checker[j]:

                result = True
                break

        if result:

            break

    return result

def text_morse(text):

    morse = ""

    for i in range (0, len(text) - 1):

        morse += translate_morse(text[i])

    result.configure(text = morse)


def translate_morse(x):

    return {

        'A' : '.- ',
        'B' : '-... ',
        'C' : '-.-. ',
        'D' : '-.. ',
        'E' : '. ',
        'F' : '..-. ',
        'G' : '--. ',
        'H' : '.... ',
        'I' : '.. ',
        'J' : '-... ',
        'K' : '-.- ',
        'L' : '.-.. ',
        'M' : '-- ',
        'N' : '-. ',
        'O' : '--- ',
        'P' : '.--. ',
        'Q' : '--.- ',
        'R' : '.-. ',
        'S' : '... ',
        'T' : '- ',
        'U' : '..- ',
        'V' : '...- ',
        'W' : '.-- ',
        'X' : '-..- ',
        'Y' : '-.-- ',
        'Z' : '--.. ',
        '0' : '----- ',
        '1' : '.---- ',
        '2' : '..--- ',
        '3' : '...-- ',
        '4' : '....- ',
        '5' : '..... ',
        '6' : '-.... ',
        '7' : '--... ',
        '8' : '---.. ',
        '9' : '----. ',
        '.' : '.-.-.- ',
        '-' : '-....- ',
        '?' : '..--.. ',
        ',' : '--..-- ',
        ':' : '---... ',
        '@' : '.--.-. ',
        '\'': '.----. ',
        '/' : '-..-. ',
        '(' : '-.--.- ',
        ')' : '-.--.- ',
        '"' : '.-..-. ',
        '=' : '-...-',
        ' ' : '/ ',
        '\n': ''

    }.get(x, "#")

def morse_text(morse):

    ptext = ""

    j = 0

    for i in range (0, len(morse)):

        if (morse[i] == '.' or morse[i] == '-' or morse[i] == '/' or morse[i] == '|'):

            j += 1

        else:

            if (j == 1):

                    if morse[i - 1] == '.':

                            ptext += "E"

                    elif (morse[i - 1] == '-'):

                            ptext += "T"
                            
                    else:

                            ptext += " "

                    j = 0


            elif (j == 2):

                        if ((morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "A"				

                        elif ((morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "N"				

                        elif ((morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "I"			

                        elif ((morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "M"

                        j = 0


            elif j == 3:

                        if ((morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "S"

                                    

                        elif ((morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "O"

                                    

                        elif ((morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "U"

                                    

                        elif ((morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "W"

                                    

                        elif ((morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "K"

                                    

                        elif ((morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "R"

                                    

                        elif ((morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "G"

                                    

                        elif ((morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "D"

                                    

                        j = 0

                            
            elif (j == 4):

                        if ((morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "H"

                                    

                        elif ((morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "V"

                                    

                        elif ((morse[i - 4] == '.') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "J"

                                    

                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "B"

                                    
                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "C"

                                    
                        elif ((morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "F"
       

                        elif ((morse[i - 4] == '.') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "L"

                                    

                        elif ((morse[i - 4] == '.') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "P"

                                    

                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "Q"

                                    

                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "X"

                                    

                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "Z"

                                    

                        elif ((morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '-')) :

                                ptext += "Y"

                                    

                        j = 0

                            

            elif (j == 5):

                        if ((morse[i - 5] == '.') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "5"

                                    

                        elif ((morse[i - 5] == '.') and (morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "1"

                                    

                        elif ((morse[i - 5] == '.') and (morse[i - 4] == '.') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "2"

                                    

                        elif ((morse[i - 5] == '.') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "3"

                                    

                        elif ((morse[i - 5] == '.') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "4"

                                    

                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "6"
                                    

                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "7"

                                    
                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "8"

                                    

                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "9"

                                    

                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += "0"

                                    

                        elif ((morse[i - 5] == '-') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '.')) :

                                ptext += "/"

                                    

                        j = 0

                            

            elif (j == 6):

                        if ((morse[i - 6] == '.') and (morse[i - 5] == '-') and (morse[i - 4] == '.') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '-')):

                                ptext += "."

                                    

                        elif ((morse[i - 6] == '.') and (morse[i - 5] == '.') and (morse[i - 4] == '-') and (morse[i - 3] == '-') and (morse[i - 2] == '.') and (morse[i - 1] == '.')):

                                ptext += "?"
                                    

                        elif ((morse[i - 6] == '-') and (morse[i - 5] == '-') and (morse[i - 4] == '.') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '-')):

                                ptext += ","

                                    

                        elif ((morse[i - 6] == '.') and (morse[i - 5] == '-') and (morse[i - 4] == '-') and (morse[i - 3] == '.') and (morse[i - 2] == '-') and (morse[i - 1] == '.')):

                                ptext += "@"

                                    

                        j = 0

            
    result.configure(text = ptext)
    
  
root = Tk()

root.title("MORSE CODE TRANSLATOR")
root.configure(background = "#EEEEEE")
root.geometry("810x670+380+100")
root.resizable(width = False, height = False)

main_label = Label(root, text = "Morse Code Translator", padx = "180", pady = "40", font = "sans 26 bold")
main_label.grid(column = "1")
main_label.configure(background = "#EEEEEE")

frm = LabelFrame(root, text = "Translate A Message", pady = "25", padx = "20", font = "sans 12 bold")
frm.grid(row = "3", column = "1")
frm.configure(background = "#EEEEEE")

input_lbl = Label(frm, text = "INPUT", font = "sans 9")
input_lbl.grid(row = "2", column = "0", pady = (20, 5), sticky = "w")
input_lbl.configure(background = "#EEEEEE")
plain_morse = Text(frm, height = "8", padx = "5", font = "monospace 10", width = "85", fg = "grey", highlightbackground = "black", highlightthickness = "1", wrap = WORD)
plain_morse.grid(row = "3", column = "0")
plain_morse.insert('1.0', "Type your message here, either normal letters, numbers and punctuation or Morse code using '.' for a dot, '-' for a dash, separating letters by spaces and words by '/'.")

output_lbl = Label(frm, text = "OUTPUT", font = "sans 9")
output_lbl.grid(row = "4", column = "0", pady = (25, 5), sticky = "w")
output_lbl.configure(background = "#EEEEEE")
result = Label(frm, height = "8", width = "85", padx = "5", font = "monospace 10", bg = "silver", fg = "black", highlightbackground = "black", highlightthickness = "1", wraplength = "675", text = "The translated message appears here with '#' for an untranslatable character.", justify = "left", anchor = "nw")
result.grid(row = "5", column = "0")

translate_btn = Button(frm, text = "TRANSLATE", bg = "#00DD00", fg = "white", activebackground = "#00AA00", activeforeground = "white", font = "ubuntu 12", cursor = "hand2", width = "15", height = "2", command = translate)
translate_btn.grid(row = 7, pady = (30, 0), sticky = "w", padx = (130, 0))

reset_btn = Button(frm, text = "RESET", bg = "#DD0000", fg = "white", activebackground = "#AA0000", activeforeground = "white", font = "ubuntu 12", cursor = "hand2", width = "15", height = "2", command = reset)
reset_btn.grid(row = 7, pady = (30, 0), sticky = "e", padx = (0, 130))

credit = Label(root, text = "Created By ", font = "sans 11")
credit.grid(row = 8, column = 1, pady = (30, 0), sticky = "e", padx = (0, 115))
credit.configure(background = "#EEEEEE")

name = Label(root, text = "Anik Shahriar", font = "sans 11 italic", fg = "blue")
name.grid(row = 8, column = 1, sticky = "e", pady = (30, 0), padx = (0, 10))
name.configure(background = "#EEEEEE")

plain_morse.bind("<FocusIn>", ready_translate)
root.bind("<Return>", enter_pressed)

root.mainloop()
