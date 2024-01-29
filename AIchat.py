from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import openai

# Thay đổi API key của bạn
openai.api_key = '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'

wind = Tk()
wind.title('ChatBot')
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
    user = Label(chat_bg, height=1, width=64, bg='#a6a6a6', fg='black', text=u + ' <You ', font=12, anchor='e')
    user.place(x=xi, y=yi)

    # Sử dụng OpenAI GPT-3 để tạo phản hồi
    bot_response = generate_bot_response(u)

    bot = Label(chat_bg, height=1, width=64, bg='white', fg='black', text=f' Bot> {bot_response}', font=12, anchor='w')
    bot.place(x=xi, y=yi + 25)

    # Thêm nút đánh giá
    rate_button = Button(chat_bg, height=1, width=4, text='Rate', font=('helvetica', 10), command=lambda: rate_feedback(bot_response))
    rate_button.place(x=xi + 500, y=yi + 25)

    yi += 50
    user_entry.delete(0, 'end')

def generate_bot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {user_input}\nBot:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def rate_feedback(bot_response):
    # Thêm code xử lý đánh giá (ví dụ: hiển thị thông báo hoặc lưu đánh giá vào cơ sở dữ liệu)
    feedback = simpledialog.askstring("Feedback", "Please provide feedback for the bot response:")
    messagebox.showinfo("Feedback", f"Thank you for your feedback!\nYou rated: {feedback}\nBot said: {bot_response}")

hcb_text = Label(height=2, width=14, bg='#0084ff', text='HEX ChatBot', font=('Impact', 20), fg='white')
hcb_text.place(x=200, y=5)

chat_bg = Frame(height=420, width=580, bg='#f5f5f5')
chat_bg.place(x=10, y=80)

entry_bg = Frame(height=60, width=500, bg='white')
entry_bg.place(x=10, y=520)

sendbtn_bg = Frame(height=60, width=65, bg='white')
sendbtn_bg.place(x=525, y=520)

def on_enter(e):
    user_entry.delete(0, 'end')
    user_entry.config(fg='black')

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0, 'Enter message...')
        user_entry.config(fg='#5c5a5a')

user_entry = Entry(entry_bg, width=32, bg='white', font=('Helvectica', 20), relief=FLAT, border=0)
user_entry.place(x=10, y=13)
user_entry.insert(0, 'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

send_button = Button(sendbtn_bg, height=1, width=3, bg='#0084ff', text='➤', font=('helvetica', 20),
                     activeforeground='white', fg='white', relief=FLAT, border=0,
                     activebackground='#0084ff', command=send_message)
send_button.place(x=5, y=4)

wind.mainloop()
