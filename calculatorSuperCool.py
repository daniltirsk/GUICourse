import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

window = tk.Tk()
window.title("Calculator")

mainFrame = ttk.Frame(window)
mainFrame.grid(sticky = [tk.N, tk.S, tk.E, tk.W])

calc_input = tk.StringVar()
input_entry = ttk.Entry(mainFrame, textvariable=calc_input, state='disabled', justify='right')
input_entry.grid(column=0, row=0, columnspan=4, sticky=[tk.N, tk.S, tk.E, tk.W])


btn = ['123+', '456-', '789*', 'C0=/']



def button_pressed(*args):
    cur_val = calc_input.get()
    new_val = ''
    if args[0] == '=':
        if not cur_val[-1].isnumeric():
            cur_val = cur_val[:-1]
            
        try:
            new_val = str(eval(cur_val))
        except:
            new_val = "ERROR"
    elif args[0] == 'C':
        new_val = ''
    elif cur_val == "ERROR":
        return
    elif not args[0].isnumeric():
        if len(cur_val)>0:
            if not cur_val[-1].isnumeric():
                new_val = cur_val[:-1] + args[0]
            else:
                new_val = cur_val + args[0]
    else:
        new_val = cur_val + args[0]

    calc_input.set(new_val)

for i in range(1,5):
    for j in range(4):
        btnLabel = btn[i-1][j]
        ttk.Button(mainFrame, text=btnLabel, command=partial(button_pressed,btnLabel)).grid(column=j, row=i)


window.mainloop()
