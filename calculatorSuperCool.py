import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

window = tk.Tk()
window.title("Calculator")
window.geometry("320x480")


mainFrame = ttk.Frame(window)

mainFrame.pack(expand=True)

window.resizable(False,False)

calc_input = tk.StringVar()
input_entry = tk.Entry(mainFrame, textvariable=calc_input, state='disabled', justify='right',font=('Ubuntu', 20))
input_entry.grid(column=0, row=0, columnspan=4,rowspan=1, sticky="nsew")

btn = ['123+', '456-', '789*', 'C0=/']

def button_pressed(*args):
    cur_val = calc_input.get()
    new_val = ''
    
    if args[0] == '=':
        if not cur_val[-1].isnumeric():
            cur_val = cur_val[:-1]
        try:
            new_val = str(eval(cur_val))
            if len(new_val) > 19:
                new_val = '%.2E' % float(new_val)
        except:
            new_val = "ERROR"
    elif args[0] == 'C':
        new_val = ''
    elif cur_val == "ERROR":
        return
    elif len(cur_val)>0 and cur_val.lower().find('e') != -1:
        new_val = cur_val
    elif not args[0].isnumeric():
        if len(cur_val)>0:
            if not cur_val[-1].isnumeric():
                new_val = cur_val[:-1] + args[0]
            else:
                new_val = cur_val + args[0]
    else:
        new_val = cur_val + args[0]

    if type(new_val) == float:
        new_val = round(new_val,10)

    if len(new_val)<20:
        calc_input.set(new_val)

for i in range(1,5):
    for j in range(4):
        btnLabel = btn[i-1][j]
        tk.Button(mainFrame, width=1, height=2, text=btnLabel,
                  command=partial(button_pressed,btnLabel), font=('Ubuntu', 20)).grid(column=j, row=i,sticky='nsew')


window.mainloop()
