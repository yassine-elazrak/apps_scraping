from tkinter import*
root=Tk()
sizex = 600
sizey = 400
posx  = 40
posy  = 20
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
itemsforlistbox=['one','two','three','four','five','six','seven']

def CurSelet(evt):
    value=str((mylistbox.get(mylistbox.curselection())))
    print(value)

mylistbox=Listbox(root,width=60,height=10,font=('times',13))
mylistbox.bind('<<ListboxSelect>>',CurSelet)
mylistbox.place(x=32,y=90)

for items in itemsforlistbox:
    mylistbox.insert(END,items)
root.mainloop()