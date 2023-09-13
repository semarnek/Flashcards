from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
to_learn = []

try:
    data_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("./data/words.csv")
    to_learn = data_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")



def pick_data():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas_f.itemconfig(image, image=f_image)
    canvas_f.itemconfig(front_text_lang, text=f"English", fill="black")
    canvas_f.itemconfig(front_text, text=f"{current_card['English']}", fill="black")

    flip_timer = window.after(3000, flip)


def flip():
    canvas_f.itemconfig(image, image=b_image)
    canvas_f.itemconfig(front_text_lang, text=f"Türkçe", fill="white")
    canvas_f.itemconfig(front_text, text=f"{current_card['Türkçe']}", fill="white")

def delete_data():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    pick_data()


window = Tk()
window.config(bg= BACKGROUND_COLOR, highlightthickness=0)
window.config(padx=50, pady=50)
window.title("Flashy")
flip_timer = window.after(3000, flip)


#buttons
no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image,  bd=0, bg=BACKGROUND_COLOR, command=pick_data)
no_button.grid(row=1, column=0)

yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, bd=0, bg=BACKGROUND_COLOR, command=delete_data)
yes_button.grid(row=1, column=1)



# Canvas
canvas_f = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
f_image = PhotoImage(file="./images/card_front.png")
b_image = PhotoImage(file="./images/card_back.png")
image = canvas_f.create_image(406, 265, image=f_image)
front_text_lang = canvas_f.create_text(400, 150, text="English", fill="black", font=("Arial", 40, "italic"))
front_text = canvas_f.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))
canvas_f.grid(row=0, column=0, columnspan=2)

pick_data()

window.mainloop()
