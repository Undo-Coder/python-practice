import tkinter as tk
from tkinter import font
from tkinter import messagebox

root = tk.Tk()

root.title("tkinter.py") #ウィンドウの名前を変更

root.geometry("500x300") #ウィンドウのサイズを設定

Layout_Contents_width = 300

text_height = 1

todos = []
states = []

def CopyToClipboard(text):
    root.clipboard_clear()       # Clear existing clipboard content
    root.clipboard_append(text)  # Append new text
    root.update()                # Keep clipboard after window closes
    messagebox.showinfo("Success", "Text copied to clipboard.")

def Send_btn (event):
    addList()

def addList():

    state = tk.BooleanVar()
    states.append(state)

    todos.append(None)
    todos[len(todos)-1] = [(txtbox.get().strip()),states[len(states)-1].get(),None,None]

    todos[len(todos)-1][2] = tk.Label(root,text=todos[len(todos)-1][0],anchor="w",height=text_height)
    #todos[len(todos)-1][2].grid(row=0, column=len(todos)-1)
    todos[len(todos)-1][2].pack(side=tk.TOP,fill=tk.X,ipady=5)
    todos[len(todos)-1][2].bind("<Button-1>",lambda event : CopyToClipboard(todos[len(todos)-1][0]))

    todos[len(todos)-1][3] = tk.Checkbutton(SubContents_frame, variable=state,anchor="w",height=text_height,bg="gainsboro")
    #todos[len(todos)-1][3].grid(row=0, column=len(todos)-1)
    todos[len(todos)-1][3].pack(side=tk.TOP,fill=tk.X,ipady=3)

    
    txtbox.delete(0, tk.END)

#font

bold_font = font.Font(size=10,weight="bold")

#コンテンツの実装
root.update()

#一番上(top)のフレームを実装
top_frame = tk.Frame(root,height=25,bg="lightblue")
top_frame.pack(side=tk.TOP, fill=tk.X)

#タブ(左側のコンテンツ)のフレームを実装
SubContents_frame = tk.Frame(root,width=(root.winfo_width() - Layout_Contents_width),bg="gainsboro")
SubContents_frame.pack(side=tk.LEFT, fill=tk.Y)

Right_frame = tk.Frame(root,width=20,bg="gainsboro")
Right_frame.pack(side=tk.RIGHT, fill=tk.Y)

btn = tk.Button(top_frame,text="Add",command=addList)
btn.pack(side=tk.LEFT)

keep_on_top = tk.BooleanVar(value=True)
keep_on_topCheck = tk.Checkbutton(top_frame,variable=keep_on_top,bg="lightblue",command=lambda: root.attributes("-topmost", keep_on_top.get()))
keep_on_topCheck.pack(side=tk.RIGHT)

discription = tk.Label(top_frame,text="Bring the window to the front",bg="lightblue",font=bold_font)
discription.pack(side=tk.RIGHT)

txtbox = tk.Entry(top_frame)
txtbox.pack(side=tk.TOP,fill="x",pady=(4, 0))

#btn2 = tk.Button(SubContents_frame, text="Button 2",bg="lime")
#btn2.grid(row=0,column=0)

txtbox.bind("<Return>", Send_btn)

root.mainloop() #メインループの実行