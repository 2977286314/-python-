from tkinter import *
import threading
import random
import time


def boom():
    root=Tk()
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    a=random.randrange(0,w)
    b=random.randrange(0,h)
    root.title('别摸鱼了！！！！')
    root.geometry('400x100'+'+'+str(a)+'+'+str(b))
    Label(root,text='你又摸鱼了！！！',bg='green',fg='red',font=('黑体',28),width=40,height=40,relief='sunken').pack()
    root.mainloop()

threads=[]
for i in range(50):
    t=threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()