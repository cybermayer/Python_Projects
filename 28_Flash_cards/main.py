import tkinter
from PIL import Image, ImageTk
import pandas
import random
import json

#--------------------------------------------------------------------  CONSTANTS  ------------------------------------------------------------------------------

# Define constants for languages, fonts, and background color
FR = "French"
EN = "English"
FONT2 = ("Ariel", 40, "italic")
FONT1 = ("Ariel", 60, "bold")
FONT3 = ("Ariel", 40, "normal")
BG_COLOR = "#C4DFDF"

#-------------------------------------------------------------------  DATA PROCESSES  --------------------------------------------------------------------------

# Load the French-English word pairs CSV file into a DataFrame
fr_en_word_pairs_csv = pandas.read_csv(r"PATH TO THE FOREIGN WORDS CSV")
data_frame = pandas.DataFrame(fr_en_word_pairs_csv)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ save stats +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def save(new_stat) -> None:
    # Save the new statistics to a JSON file
    try:
        with open(r"stat.json", "r") as json_to_update:
            json_load = json.load(json_to_update)
            json_load.update(new_stat)
    except FileNotFoundError:
        with open(r"stat.json", "w") as new_json:
            json.dump(new_stat, new_json, indent=4)
    else:
        with open(r"stat.json", "w") as json_to_update:
            json.dump(json_load, json_to_update, indent=4)  

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ last 50 words +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add_to_last_words(picked_word) -> None:
    # Add the picked word to the list of the last 50 words
    global last_50_words
    last_50_words.insert(0, picked_word)
    if len(last_50_words) >= 50:
         last_50_words.pop()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ check stats ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def word_check(picked_word) -> None:

    # Check the statistics of the picked word
    try:
        with open(r"stat.json", "r") as json_to_check:
            card_stats = json.load(json_to_check)
            word_to_check = card_stats[picked_word]

            global times_faild
            times_faild = word_to_check["times_faild"]

            global times_known
            times_known = word_to_check["times_known"]

            if times_known < 5 and picked_word not in last_50_words:
                is_proper_word = True

    except FileNotFoundError:
        times_faild = 0
        times_known = 0
        is_proper_word = True
            
    except KeyError:
        times_faild = 0
        times_known = 0
        is_proper_word = True

    return is_proper_word

def generate_indicators() -> None:
    # Generate indicators for the number of times a word has been failed or known
    with open(r"stat.json", "r") as json_to_check:
            card_stats = json.load(json_to_check)
            word_to_check = card_stats[random_picked_fr_word]

            global times_faild
            times_faild = word_to_check["times_faild"]

            global times_known
            times_known = word_to_check["times_known"]

    global pipes
    global fails
    pipes = ""
    fails = ""
    for i in range(times_known):
         pipes += "✔️"
    for i in range(times_faild):
         fails += "❌"

#----------------------------------------------------------------  ANSWER MECHANISM  -----------------------------------------------------------------------------------
def pick_new_word() -> None:
    # Pick a new French word that meets the criteria
    is_proper_word = False
    
    while is_proper_word == False:
        global random_picked_fr_word
        random_picked_fr_word = random.choice(data_frame.French)
        is_proper_word = word_check(random_picked_fr_word)
      
    global correspondent_eng
    correspondent_eng = data_frame.loc[data_frame.French == random_picked_fr_word, "English"].item()

def wrong_answer() -> None:
    # Handle the wrong answer scenario
    rtrn_msg = " Try to       👆   memorize\n  Next time you'll make it!"
    new_stat = {random_picked_fr_word: {"times_faild": times_faild + 1,
                                            "times_known": 0}
        }
    save(new_stat)
    add_to_last_words(random_picked_fr_word)
    show_bcard(rtrn_msg)

def right_answer(word_to_check) -> None:
    # Handle the right answer scenario
    rtrn_msg = ""
    if word_to_check == data_frame.loc[data_frame.French == random_picked_fr_word, "English"].item():
        rtrn_msg = "Correct answer!✔️"
        new_stat = {random_picked_fr_word: {"times_faild": times_faild, 
                                            "times_known": times_known + 1}
        }
        save(new_stat)
        add_to_last_words(random_picked_fr_word)
        
    else:
        rtrn_msg = "Wrong answer!❌"
        new_stat = {random_picked_fr_word: {"times_faild": times_faild + 1,
                                            "times_known": 0}
        }
        save(new_stat)
        add_to_last_words(random_picked_fr_word)
        
    return rtrn_msg

def call_right_answer() -> None:
    # Call the right_answer function with the word from the entry widget
    submit_word = guess_entry.get()
    rtrn_msg = right_answer(submit_word)
    show_bcard(rtrn_msg)

#--------------------------------------------------------------------- UI SETUP ---------------------------------------------------------------------------------------

# Create the main window for the application
window = tkinter.Tk()
window.geometry("860x690")
window.title("Flashy CARDs")
window.config(bg=BG_COLOR)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  photo paths  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Load images for the cards and buttons
card_back_image = tkinter.PhotoImage(file = r"card_back.png")
card_front_image = tkinter.PhotoImage(file = r"card_front.png")
right_image= tkinter.PhotoImage(file = r"right.png")
wrong_image = tkinter.PhotoImage(file = r"wrong.png")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  canvas setup  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Initialize the list of the last 50 words
global last_50_words
last_50_words = []

# Create a canvas for displaying the cards
canvas_card = tkinter.Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)

def show_fcard() -> None:
    # Display the front of the card with a new word
    pick_new_word()
    canvas_card.create_image(400, 263, image=card_front_image)
    canvas_card.create_text(400, 150, text=FR, font=FONT1)
    canvas_card.create_text(400, 263, text=random_picked_fr_word, font=FONT2)
    canvas_card.grid(column=0, row=0, rowspan=1, padx=40, pady=20)

def show_bcard(return_message) -> None:
    # Display the back of the card with the answer and indicators
    generate_indicators()
    canvas_card.create_image(400, 263, image=card_back_image)
    canvas_card.create_text(350, 50, text=fails, font=("Bauhaus 93", 14, "bold"), fill="red")
    canvas_card.create_text(365, 476, text=pipes, font=("Bauhaus 93", 14, "bold"), fill="green")
    canvas_card.create_text(400, 150, text=EN, font=FONT1)
    canvas_card.create_text(400, 263, text=correspondent_eng, font=FONT2)
    if return_message == "Correct answer!✔️":
        canvas_card.create_text(450, 350, text=return_message, font=FONT3, fill="green")
    elif return_message == "Wrong answer!❌":
        canvas_card.create_text(400, 350, text=return_message, font=FONT3, fill="red")
    else:
        canvas_card.create_text(400, 350, text=return_message, font=FONT3, fill="orange")
    canvas_card.grid(column=0, row=0, rowspan=1, padx=40, pady=20)
    print(last_50_words)
    window.after(5000, show_fcard)

# Create buttons for correct and wrong answers
right_button_card = tkinter.Button(image=right_image, command=call_right_answer, highlightthickness=0)
right_button_card.place(x=130, y=560)

wrong_button_card = tkinter.Button(image=wrong_image, command=wrong_answer, highlightthickness=0)
wrong_button_card.place(x=620, y=560)

# Create an entry widget for the user to input their answer
guess_entry = tkinter.Entry()
guess_entry.configure(width=11, highlightthickness=0, font=FONT2, border=3)
guess_entry.focus()
guess_entry.place(x=265, y=580)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ active functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Show the front card initially
show_fcard()

# Start the Tkinter event loop
window.mainloop()
