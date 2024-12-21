import tkinter as tk
from tkinter import ttk, messagebox

# Define the scales and intervals
def generate_scale(scale_name):
    scales = {
        "C_major": ["C", "D", "E", "F", "G", "A", "B"],
        "G_major": ["G", "A", "B", "C", "D", "E", "F#"],
        "D_major": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A_major": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E_major": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B_major": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#_major": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "Db_major": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "Ab_major": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
        "Eb_major": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "Bb_major": ["Bb", "C", "D", "Eb", "F", "G", "A"],
        "F_major": ["F", "G", "A", "Bb", "C", "D", "E"],
        "A_minor": ["A", "B", "C", "D", "E", "F", "G"],
        "E_minor": ["E", "F#", "G", "A", "B", "C", "D"],
        "B_minor": ["B", "C#", "D", "E", "F#", "G", "A"],
        "F#_minor": ["F#", "G#", "A", "B", "C#", "D", "E"],
        "C#_minor": ["C#", "D#", "E", "F#", "G#", "A", "B"],
        "G#_minor": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
        "D#_minor": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
        "Bb_minor": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
        "F_minor": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
        "C_minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
        "G_minor": ["G", "A", "Bb", "C", "D", "Eb", "F"],
        "D_minor": ["D", "E", "F", "G", "A", "Bb", "C"],
    }
    return scales.get(scale_name, [])

# Function to find the harmony note
def find_harmony(note, scale, interval):
    scale_notes = generate_scale(scale)
    if note not in scale_notes:
        return f"Error: {note} is not in the {scale} scale."

    # Find the index of the input note
    note_index = scale_notes.index(note)

    # Calculate the index of the harmony note
    harmony_index = (note_index + interval) % len(scale_notes)

    # Return the harmony note
    return scale_notes[harmony_index]

# GUI Application
def calculate_harmony():
    note = note_entry.get()
    scale = scale_combobox.get()
    try:
        interval = int(interval_entry.get()) - 1  # Subtract 1 to match 0-based indexing
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid interval.")
        return

    harmony_note = find_harmony(note, scale, interval)

    if "Error" in harmony_note:
        messagebox.showerror("Error", harmony_note)
    else:
        result_label.config(text=f"Harmony Note: {harmony_note}")

# Main GUI window
root = tk.Tk()
root.title("Harmony Finder")

# Input fields
note_label = tk.Label(root, text="Enter Note:")
note_label.grid(row=0, column=0, padx=10, pady=10)
note_entry = tk.Entry(root)
note_entry.grid(row=0, column=1, padx=10, pady=10)

scale_label = tk.Label(root, text="Select Scale:")
scale_label.grid(row=1, column=0, padx=10, pady=10)
scale_combobox = ttk.Combobox(root, values=list({
    "C_major": [],
    "G_major": [],
    "D_major": [],
    "A_major": [],
    "E_major": [],
    "B_major": [],
    "F#_major": [],
    "Db_major": [],
    "Ab_major": [],
    "Eb_major": [],
    "Bb_major": [],
    "F_major": [],
    "A_minor": [],
    "E_minor": [],
    "B_minor": [],
    "F#_minor": [],
    "C#_minor": [],
    "G#_minor": [],
    "D#_minor": [],
    "Bb_minor": [],
    "F_minor": [],
    "C_minor": [],
    "G_minor": [],
    "D_minor": [],
}.keys()))
scale_combobox.grid(row=1, column=1, padx=10, pady=10)

interval_label = tk.Label(root, text="Enter Interval:")
interval_label.grid(row=2, column=0, padx=10, pady=10)
interval_entry = tk.Entry(root)
interval_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Harmony", command=calculate_harmony)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Harmony Note: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
