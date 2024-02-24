import requests
import tkinter as tk
from threading import Thread
api="http://api.quotable.io/random"
quotes=[]
no=0
window=tk.Tk()
window.geometry("900x400")
window.title("Quote Generator")
window.resizable(0,0)
window.config(bg='#BCC8C6')
window.grid_columnconfigure(0,weight=1)

def load():
    global quotes
    print("***Loading Quotes***")
    for i in range(10):
        randomquot=requests.get(api).json()
        content=randomquot["content"]
        author=randomquot["author"]
        res=content+"\n\n"+"~"+author
        quotes.append(res)
    print("***Finished Loading Quotes***")

load()
def get_q():
    global no
    global quotes
    global qlabel
    qlabel.configure(text=quotes[no])
    no+=1
    if quotes[no]==quotes[-3]:
        thread=Thread(target=load)
        thread.start()

qlabel=tk.Label(window,text="Click on the button to generate a quote!",height=6,pady=10,wraplength=800,font=("Helvetica",18))
qlabel.grid(row=0,column=0,stick="NSWE",padx=20,pady=10)
but=tk.Button(window,command=get_q,text="Generate",bg="#0052cc",fg="#FFFFFF",activebackground="#BCC8C6",font=("Helvetica",18))
but.grid(row=1,column=0,stick="NSWE",padx=20,pady=10)
namel=tk.Label(window,text="Made by Mridul Garg",height=1,width=5,pady=10,wraplength=100,font=("Helvetica",14))
namel.grid(row=2,column=0,stick="NSEW",padx=375,pady=20)

if __name__=="__main__":
    window.mainloop()