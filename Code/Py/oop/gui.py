import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Label 1")
label2 = tkinter.Label(main_window, text = "Label 2")

button1 = tkinter.Button(main_window, text = "WOE")

# method positioning
label1.pack()
label2.pack()
button1.pack()

# method menampilkan GUI
main_window.mainloop()