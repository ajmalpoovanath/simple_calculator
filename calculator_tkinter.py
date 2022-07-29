# before running this programme please install tkinter on your system

from tkinter import *
# Calculator window
window = Tk()
window.geometry("570x600")
window.title("Calculator")
window.resizable(False, False)
window.configure(bg="#151313")
# Calculator screen
display = Label(window, width=25, height=2, text="", font=("arial", 30))
display.pack()
# Buttons
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10,
                                                                                                             y=100)  # clear button
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150,
                                                                                                             y=100)  # division button
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=100)  # percentage button
Button(window, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430,
                                                                                                             y=100)  # multiplication button
Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=10,
                                                                                                             y=165)  # number 7 button
Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150,
                                                                                                             y=165)  # number 8 button
Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=165)  # number 9 button
Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430,
                                                                                                             y=165)  # substaction button
Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=10,
                                                                                                             y=230)  # number 4 button
Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150,
                                                                                                             y=230)  # number 5 button
Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=230)  # number 6 button
Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430,
                                                                                                             y=230)  # addition button
Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=10,
                                                                                                             y=295)  # number 1 button
Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150,
                                                                                                             y=295)  # number 2 button
Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=295)  # number 3 button
Button(window, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=12,
                                                                                                             y=360)  # number 0 button
Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290,
                                                                                                             y=360)  # dot button
Button(window, text="=", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#F96D2C").place(x=430,
                                                                                                             y=300)  # equal button
window.mainloop()
