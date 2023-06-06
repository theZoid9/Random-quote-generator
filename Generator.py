import tkinter as tk    
import random 

def quotes():
    quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
]
    return quotes



def button_clicked():
    quote = quotes()
    rand_quote = random.choice(quote)
    results.config(text="{}".format(rand_quote))






window = tk.Tk()

window.geometry("600x480")
window.title("GUI")

label = tk.Label(window, text="Random Quote Generator", font=("Arial",14))
label.pack(padx=20, pady=20)

results = tk.Label(window,text="Your Quote!")
results.pack(ipadx=0, ipady=150)

btn = tk.Button(window, text="CLICK HERE!!!", command=button_clicked)
btn.place(x=0, y=425, height=50, width=600)




window.mainloop()