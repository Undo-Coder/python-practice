import tkinter as tk

root = tk.Tk()

root.title("tkinter.py") #ウィンドウの名前を変更

root.geometry("500x300") #ウィンドウのサイズを設定

Layout_Contents_width = 300

todos = []

def Send_btn (event):
    todos.append(None)
    todos[len(todos)-1] = tk.Label(SubContents_frame,text=("New Todos"+str(len(todos)-1)),anchor="w")
    todos[len(todos)-1].pack()

#コンテンツの実装
root.update()

#一番上(top)のフレームを実装
top_frame = tk.Frame(root,height=25,bg="blue")
top_frame.pack(side=tk.TOP, fill=tk.X)

#タブ(左側のコンテンツ)のフレームを実装
SubContents_frame = tk.Frame(root,bg="lightblue",width=(root.winfo_width() - Layout_Contents_width))
SubContents_frame.pack(side=tk.LEFT, fill=tk.Y)

print(root.winfo_width())

btn = tk.Button(top_frame,text="Hello")
btn.pack(side=tk.LEFT)

#btn2 = tk.Button(SubContents_frame, text="Button 2",bg="lime")
#btn2.grid(row=0,column=0)

root.bind("<Return>",Send_btn)

root.mainloop() #メインループの実行