import tkinter as tk

calculator = ""

def tambah_ke_calculator(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculator)

def evalute_calculator():
    global calculator
    try:
        calculator = str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculator)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        
        pass
    pass

def clear_field():
    global calculator
    calculator = ""
    text_result.delete(1.0, "end")
    pass


root = tk.Tk()
root.geometry("300x275")
root.resizable(False,False)

root.title("Calculator")

text_result = tk.Text(root, height=2 ,width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#tombol 1
btn_1 = tk.Button(root, text="1", command=lambda: tambah_ke_calculator(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

#tombol 2
btn_2 = tk.Button(root, text="2", command=lambda: tambah_ke_calculator(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

#tombol 3
btn_3 = tk.Button(root, text="3", command=lambda: tambah_ke_calculator(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

#tombol 4
btn_4 = tk.Button(root, text="4", command=lambda: tambah_ke_calculator(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

#tombol 5
btn_5 = tk.Button(root, text="5", command=lambda: tambah_ke_calculator(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

#tombol 6
btn_6 = tk.Button(root, text="6", command=lambda: tambah_ke_calculator(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

#tombol 7
btn_7 = tk.Button(root, text="7", command=lambda: tambah_ke_calculator(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

#tombol 8
btn_8 = tk.Button(root, text="8", command=lambda: tambah_ke_calculator(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

#tombol 9
btn_9 = tk.Button(root, text="9", command=lambda: tambah_ke_calculator(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

#tombol 0
btn_0 = tk.Button(root, text="0", command=lambda: tambah_ke_calculator(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

#tombol +
btn_plus = tk.Button(root, text="+", command=lambda: tambah_ke_calculator("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

#tombol -
btn_minus = tk.Button(root, text="-", command=lambda: tambah_ke_calculator("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

#tombol *
btn_mul = tk.Button(root, text="*", command=lambda: tambah_ke_calculator("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)

#tombol /
btn_div = tk.Button(root, text="/", command=lambda: tambah_ke_calculator("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

#tombol Open
btn_open = tk.Button(root, text="(", command=lambda: tambah_ke_calculator("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)

#tombol Close
btn_close = tk.Button(root, text=")", command=lambda: tambah_ke_calculator(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

#tombol =
btn_equals = tk.Button(root, text="=", command=evalute_calculator, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2) # columnspan untuk melebarkan tampilan program supaya column muat

#tombol Clear
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2) # columnspan untuk melebarkan tampilan program supaya column muat
 

root.mainloop()