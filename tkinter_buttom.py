from tkinter import *
 
clicks = 0
 
 
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

# текст кнопки \ фоновый цвет кнопки \ цвет текста \ отступ от границ до содержимого по горизонтали
# отступ от границ до содержимого по вертикали \ высота шрифта
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
 
root.mainloop()