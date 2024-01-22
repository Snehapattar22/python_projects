import tkinter as tk
from tkinter import ttk
import requests

def fetch_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke_data = response.json()

        setup_text.set(joke_data["setup"])
        punchline_text.set(joke_data["punchline"])
    except requests.RequestException as e:
        setup_text.set("Error fetching joke")
        punchline_text.set(str(e))

# GUI setup
app = tk.Tk()
app.title("Joke App")

# Labels for joke display
setup_text = tk.StringVar()
punchline_text = tk.StringVar()

setup_label = tk.Label(app, textvariable=setup_text, font=("Helvetica", 12), wraplength=400)
setup_label.pack(pady=10)

punchline_label = tk.Label(app, textvariable=punchline_text, font=("Helvetica", 12, "italic"), wraplength=400)
punchline_label.pack(pady=10)

# Button to fetch a new joke
fetch_button = tk.Button(app, text="Get Joke", command=fetch_joke)
fetch_button.pack(pady=10)

# Run the app
app.mainloop()
