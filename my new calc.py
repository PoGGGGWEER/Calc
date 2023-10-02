import tkinter as tk
from tkinter import *

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    print(calculation)
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Fehler")
        pass


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


def square():
    global calculation
    square = number * number


root = tk.Tk()
root.title("Mein Eigener Taschenrechner V.0.01")
root.geometry("392x300")


text_result = tk.Text(root, height=8, width=22, font=("Arial", 24), bd=1, fg="#000000")
text_result.grid(columnspan=5)




btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=8, font=("Arial", 14)).place(x=0,y=75)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=8, font=("Arial", 14)).place(x=98,y=75)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=8, font=("Arial", 14)).place(x=196,y=75)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=8, font=("Arial", 14)).place(x=0,y=115)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=8, font=("Arial", 14)).place(x=98,y=115)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=8, font=("Arial", 14)).place(x=196,y=115)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=8, font=("Arial", 14)).place(x=0,y=155)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=8, font=("Arial", 14)).place(x=98,y=155)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=8, font=("Arial", 14)).place(x=196,y=155)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=8, font=("Arial", 14)).place(x=98,y=195)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=8, font=("Arial", 14)).place(x=294,y=75)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=8, font=("Arial", 14)).place(x=294,y=115)
btn_durch = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=8, font=("Arial", 14)).place(x=294,y=155)
btn_mal = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=8, font=("Arial", 14)).place(x=294, y=195)
btn_offen = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=8, font=("Arial", 14)).place(x=196,y=195)
btn_zu = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=8, font=("Arial", 14)).place(x=0,y=195)
btn_gleich = tk.Button(root, text="=", command=evaluate_calculation, width=12, font=("Arial", 14)).place(x=0,y=235)
btn_leer = tk.Button(root, text="C", command=clear_field, width=8, font=("Arial", 14)).place(x=143,y=235)
root.mainloop()