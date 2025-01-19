from tkinter import *  #importing tkinter
root = Tk()    #defining root to store things
root.geometry("500x450")  # to define te size of the window of application

#Creating a label to print a text
#.grid() is used to specify the exact location of the lebel
mylabel2 = Label(root, text="this is my first gui program").grid(row=1,column=2)

#taking input
    #width= to decide the width of the input box
    #bg=, fg= for background and foreground(text colour) colour
e= Entry(root,width=24, bg="white",fg="red") # this line decides where to store the input
e.grid(row=3,column= 2)
e.insert(0,"enter your name here")  # this fill the box with text intially

#if you can using .grid() you can only take input once as that particular row/column is executed
#you can use .pack() to accept and print multiple time
currentrow=6

def my_click():   #this define the function, what will happen if you click the button
    global currentrow
    greet="hellow   "+e.get()    #e.get() recalls the vlaue enter in e
    mylabel1 = Label(root,text=greet)
    mylabel1.grid(row=currentrow, column=2)
    # this updates the row and column to take and print the input multiple time while assigning row/column
    currentrow += 1

#Button() creates button
    # why to use root
    # specifying to place to store button is important
    #padx and pady is used to resize the button
    #command= is used to call the function
    #state="disabled" is used to disable the button
my_button=Button(root,text="click me",command=my_click,padx=25, pady=11,).grid(row=5, column=2)










#to start the event loop
root.mainloop()














































