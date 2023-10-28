import tkinter as tk
def handler():
    value=int(entryBox.get())
    msg="Even"
    if value%2:
        msg="Odd"
    resultLabel.config(text=msg)
    #print(value)
    #print("Clicked")
root=tk.Tk()
btn=tk.Button(root,text="Submit",bg="red",fg="black",command=handler)
# btn.pack()
# root.mainloop()
entryBox=tk.Entry(root)
resultLabel=tk.Label(root,text="No input given")
entryBox.grid(row=0,column=0)
btn.grid(row=0,column=1)
resultLabel.grid(row=1)
root.mainloop()