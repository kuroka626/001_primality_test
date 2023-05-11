from tkinter import *
import test_define

def calculate():
    num = int(entry_1b.get())
    result = test_define.judge(num)
    text.set(str(result))

 
root = Tk()

root.title('素数判定機') 
root.geometry('400x160')
root.resizable(False, False)

frame1 = Frame(root, width=400, height=160, borderwidth=2, relief='solid')
frame1.grid(row=0, column=0)
frame1.propagate(False)

#入力欄
entry_1b = Entry(frame1, width=14)
text = StringVar()
entry_1b.pack()

#説明文
label_1a = Label(frame1, text='任意の自然数を入力', font=('', 14))
label_1a.pack()

#ボタン
button_1a = Button(frame1, text='決定', cursor='hand2', width=10, height=3, command=calculate)
button_1a.pack(padx=0, pady=0)


#返す値
label_1b = Label(frame1, textvariable=text, font=('', 14))
label_1b.pack()


root.mainloop()