import  tkinter as tk
from tkinter import messagebox

def calculate(event):
    text = event.widget.cget("text")
    if(text == "="):
        try:
            answer = str(eval(display.get()))
            display.delete(0, tk.END)
            if answer[-2:] == '.0':
                answer = answer[:-2]
            display.insert(tk.END, str(answer))
        except:
            messagebox.showerror(title='ERROR!', message='This is Not Defined!!')
    elif(text == 'C'):
        display.delete(0, tk.END)
    elif(text == '⌫'):
        curr_val = display.get()
        curr_val = curr_val[:-1]
        display.delete(0, tk.END)
        display.insert(tk.END, curr_val)
    else:
        display.insert(tk.END, text)


window = tk.Tk()
window.title("Calculator")
window.config(bg='black')
calc_img = tk.PhotoImage(file='images/calculator.png')
window.iconphoto(True, calc_img)

frame = tk.Frame(window, bg='black')
frame.pack()

display = tk.Entry(
    frame, width=29, justify='right', font=("Arial", 15, "bold"), bg='black', fg='white'
)
display.grid(row=0, column=0, columnspan=4, ipady=15)

keys = [
    ['C', '⌫'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/']
]

row = 1
for i in range(0, len(keys)):
    key = keys[i]
    column = 0
    for k in key:
        button = tk.Button(
            frame, text=k, width=5, height=2, bg="#242726", fg="white", bd=5, relief='raised',
            activebackground="#2A2C2B",activeforeground='white',font=("Arial", 15, "bold")
        )
        
        if k == '⌫' or k  == 'C':
            button.config(width=12)
            button.config(bg="#eb820b")
            button.grid(row=row, column=column, columnspan=2)
            column += 2
        else:
            button.grid(row=row, column=column)
            column += 1
        
        button.bind("<Button-1>", calculate)
    row += 1

window.mainloop()