import nlp_inti
import match_recipes
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Food Recommender Chatbot")
root.geometry("520x550")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 11))
chat_area.place(x=10, y=10, width=500, height=430)
chat_area.configure(state='disabled', bg="#ffffff")


chat_area.tag_configure("bold", font=("Segoe UI", 11, "bold"))

user_input = tk.Entry(root, font=("Segoe UI", 12), bd=2)
user_input.place(x=10, y=460, width=400, height=35)

send_btn = tk.Button(root, text="Send", font=("Segoe UI", 12, "bold"), bg="#4CAF50", fg="white")
send_btn.place(x=420, y=460, width=80, height=35)

def send_message():
    message = user_input.get()
    if message.strip() == "":
        return

    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "You: ", "bold")
    chat_area.insert(tk.END, message + "\n")

    ingredients = nlp_inti.extract_ingredients(message)
    if not ingredients:
        chat_area.insert(tk.END, "Bot: ", "bold")
        chat_area.insert(tk.END, "There is no food available with ingredients you entered ")
    else:
        chat_area.insert(tk.END, "Bot: ", "bold")
        chat_area.insert(tk.END, f"Finding dishes with {', '.join(ingredients)}...\n")
        results = match_recipes.get_recommendations(ingredients)
        for r in results:
            chat_area.insert(tk.END, r + "\n")

    chat_area.insert(tk.END, "\n")
    chat_area.configure(state='disabled')
    user_input.delete(0, tk.END)

send_btn.config(command=send_message)

root.mainloop()
