from tkinter import *
from pynput.keyboard import Key, Controller as key_cl
from pynput.mouse import Button as mouse_but, Controller as mouse_cl
import time


def mouse_input():
    mouse = mouse_cl()
    mouse.press(mouse_but.left)
    mouse.release(mouse_but.left)


def key_input(string):
    keyboard = key_cl()
    keyboard.type(string)


def message(number, string):
    keyboard = key_cl()
    text1.insert(END, '程序马上开始了\n')
    time.sleep(3)
    for i in range(number):
        key_input(string)
        mouse_input()
        time.sleep(0.1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


def send():
    mess = str(input1.get())
    num = int(input2.get())
    message(num, mess)
    text1.insert(END, '程序执行成功\n')


root = Tk()
root.title('信息轰炸，微信和qq都可')
root.geometry('400x400')
lb = Label(root, text='在下面的信息和次数框输入轰炸的信息和次数\n点击确定后将指针放在微信或者qq输入框', fg='black', font=('黑体', 10))
lb.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

input1 = Entry(root)
input1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.8)

input2 = Entry(root)
input2.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.1)

button = Button(root, text='确认', command=send)
button.place(relx=0.35, rely=0.6, relheight=0.1, relwidth=0.2)

text1 = Text(root)
text1.place(rely=0.8)

root.mainloop()
