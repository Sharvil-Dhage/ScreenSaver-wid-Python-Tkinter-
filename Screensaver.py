from tkinter  import*
import time
import random
from time import strftime

name = None

def time1():
    string = strftime('%I:%M %p')
    lbl.config(text = string)
    lbl.after(1000, time1)

def submit():
   global name
   name = entry.get()

   if name == '':
    print("Enter Your name")
   else:
    root.destroy()

def quitu():
    window.destroy()


root = Tk()
root.attributes('-fullscreen',True)

labelask = Label(root,text="ENTER YOUR NAME HERE:- ",font=('Gotham Medium',20))
labelask.pack()
entry = Entry(root,font=('Gotham Medium',20))
entry.pack()
submit = Button(root,text='Submit',command=submit)
submit.pack()



root.mainloop()








window = Tk()
window.attributes('-fullscreen',True)
window.title('ScreenSaver By SPD')


photo = PhotoImage(file='space1.png')
photo1 = PhotoImage(file='space2.png')
photo2 = PhotoImage(file='space3.png')

photos = [photo,photo1,photo2]
photos_actual = random.choice(photos)

menu = Menu(window)
window.config(menu=menu)
quitapp = Menu(menu,tearoff=0,font=('Gotham Medium',5) )
menu.add_cascade(label='Quit',menu=quitapp)
quitapp.add_command(label='Quit',command=quitu,font=('Gotham Medium',10))


label = Label(window,image=photos_actual)
label.pack()

lbl = Label(window, font=('Gotham Medium', 30, 'bold'),
            fg='white',
            bg='black')

lbl.place(x=1100,y=650)

label1 = Label(window,text='Hello '+str(name),font=('Gotham Medium',20,'italic'))
label1.place(x=1100,y=610)

time1()
window.mainloop()





