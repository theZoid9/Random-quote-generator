import tkinter as tk    
import random 
from quotes import quotes




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