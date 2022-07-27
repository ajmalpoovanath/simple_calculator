# before running this programme please install tkinter on your system

from tkinter import *

window = Tk()
window.geometry("570x600")
window.title("Calculator")
window.resizable(False, False)
window.configure(bg="#151313")

display = Label(window, width=25, height=2, text="", font=("arial", 30))
display.pack()
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10,
                                                                                                             y=100)  # clear button
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150,
                                                                                                             y=100)  # division button
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=100)  # percentage button
Button(window, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430,
                                                                                                             y=100)  # multiplication button

window.mainloop()
