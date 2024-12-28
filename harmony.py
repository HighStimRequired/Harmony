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

# Function to process tab data
def process_tab_data(tab_data, scale, interval):
    processed_data = []
    for note in tab_data.split():
        harmony_note = find_harmony(note, scale, interval)
        if "Error" in harmony_note:
            processed_data.append(f"{note} (Error)")
        else:
            processed_data.append(harmony_note)
    return processed_data

# GUI Application
def calculate_harmony():
    if tab_mode.get():
        tab_data = tab_text.get("1.0", tk.END).strip()
        scale = scale_combobox.get()
        try:
            interval = int(interval_entry.get()) - 1  # Subtract 1 to match 0-based indexing
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid interval.")
            return

        harmony_results = process_tab_data(tab_data, scale, interval)
        result_label.config(text="Harmony Notes:\n" + " ".join(harmony_results))
    else:
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
root.geometry("600x400")

# Apply dark mode theme
dark_bg = "#2e2e2e"  # Dark background
dark_fg = "#ffffff"  # Light foreground
button_bg = "#3e3e3e"  # Button background
button_fg = "#ffffff"  # Button foreground

root.configure(bg=dark_bg)  # Set the app's background color

# Tab mode toggle
tab_mode = tk.BooleanVar()
tab_mode_checkbox = tk.Checkbutton(root, text="Tab Mode", variable=tab_mode, bg=dark_bg, fg=dark_fg, selectcolor=dark_bg)
tab_mode_checkbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Input fields
note_label = tk.Label(root, text="Enter Note:", bg=dark_bg, fg=dark_fg)
note_label.grid(row=1, column=0, padx=10, pady=10)
note_entry = tk.Entry(root, bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
note_entry.grid(row=1, column=1, padx=10, pady=10)

scale_label = tk.Label(root, text="Select Scale:", bg=dark_bg, fg=dark_fg)
scale_label.grid(row=2, column=0, padx=10, pady=10)
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
}.keys()), state="readonly")
scale_combobox.grid(row=2, column=1, padx=10, pady=10)

interval_label = tk.Label(root, text="Enter Interval:", bg=dark_bg, fg=dark_fg)
interval_label.grid(row=3, column=0, padx=10, pady=10)
interval_entry = tk.Entry(root, bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
interval_entry.grid(row=3, column=1, padx=10, pady=10)

# Tab input field
tab_label = tk.Label(root, text="Paste Tab Data:", bg=dark_bg, fg=dark_fg)
tab_label.grid(row=4, column=0, padx=10, pady=10)
tab_text = tk.Text(root, bg=dark_bg, fg=dark_fg, insertbackground=dark_fg, height=5, width=40)
tab_text.grid(row=4, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Harmony", command=calculate_harmony, bg=button_bg, fg=button_fg)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Harmony Notes: ", bg=dark_bg, fg=dark_fg)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
