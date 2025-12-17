import tkinter

window=tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500,height=300)

my_lable=tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_lable.pack()#thr label won't show up unless we use this packer my_lable.pack()






window.mainloop()