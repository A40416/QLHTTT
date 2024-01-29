from tkinter import *

wind = Tk()
wind.title('Vinh Sôkiuuu')
wind.geometry('600x600')
wind.configure(bg='#0084ff')
xi = 0
yi = 0
def clear_message():
    global yi
    yi -= yi
    for widget in chat_bg.winfo_children():
        widget.destroy()
    yi -= 50
def send_message():
    global yi
    u = user_entry.get()
    user = Label(chat_bg,height=1,width=64,bg='#a6a6a6',fg='black',text=u+' <You ',font=12,anchor='e')
    user.place(x=xi,y=yi)
    if 'hello' in u:
        bot = Label(chat_bg, height=1, width=64, bg='white', fg='black',text=' Bot> Hello', font=12, anchor='w')
        bot.place(x=xi, y=yi+25)
    elif 'how are you?' in u:
        bot = Label(chat_bg, height=1, width=64, bg='white', fg='black', text=' Bot> Im fine', font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
    elif u == 'clear':
        clear_message()
    else:
        bot = Label(chat_bg, height=1, width=64, bg='white', fg='black', text=' Bot> Do not understand you', font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
    
    

		
    yi+=50
    user_entry.delete(0,'end')


hcb_text = Label(height=2,width=19, bg='#0084ff',text='Rule_Bases Chatbots',font=('Impact',20),fg='white')
hcb_text.place(x=200,y=5)
chat_bg = Frame(height=420, width=580, bg='#f5f5f5')
chat_bg.place(x=10,y=80)
entry_bg = Frame(height=60,width=500,bg='white')
entry_bg.place(x=10,y=520)
sendbtn_bg = Frame(height=60, width=65,bg='white')
sendbtn_bg.place(x=525,y=520)
def on_enter(e):
    user_entry.delete(0,'end')
    user_entry.config(fg='black')
def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0,'Enter message...')
        user_entry.config(fg='#5c5a5a')
user_entry = Entry(entry_bg, width=32, bg='white',font=('Helvectica',20),relief=FLAT,border=0)
user_entry.place(x=10,y=13)
user_entry.insert(0,'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>",on_enter)
user_entry.bind("<FocusOut>", on_leave)
send_button = Button(sendbtn_bg,height=1,width=3,bg='#0084ff',text='➤',font=('helvectica',20),
                     activeforeground='white',fg='white',relief=FLAT,border=0,
                     activebackground='#0084ff',command=send_message)
send_button.place(x=5,y=4)

wind.mainloop()