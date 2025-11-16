import tkinter as tk
import random
import string

locate_const = 300


def generate_key():
    letters = string.ascii_uppercase
    digits = string.digits

    key_parts = []

    for _ in range(3):
        chars = random.choices(digits, k=2) + random.choices(letters, k=3)
        random.shuffle(chars)
        part = "".join(chars)
        key_parts.append(part)

    return "-".join(key_parts)


def set_background(root, image_path):
    bg_image = tk.PhotoImage(file=image_path)

    canvas = tk.Canvas(root, width=600, height=500)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(locate_const, 250, image=bg_image, anchor="center")

    canvas.image = bg_image

    return canvas


def create_interface(canvas):
    title_lbl = tk.Label(
        canvas, text="MINECRAFT KEY GENERATOR", font=("Arial", 18, "bold"), fg="black"
    )
    canvas.create_window(locate_const, 50, window=title_lbl)

    key_entry = tk.Entry(
        canvas,
        font=("Courier", 14, "bold"),
        justify="center",
        state="readonly",
        relief="solid",
        width=25,
    )
    canvas.create_window(locate_const, 150, window=key_entry)

    def generate_click():
        key = generate_key()
        key_entry.config(state="normal")
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)
        key_entry.config(state="readonly")

    generate_btn = tk.Button(
        canvas,
        text="GENERATE KEY",
        command=generate_click,
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="raised",
        padx=20,
        pady=10,
    )
    canvas.create_window(locate_const, 200, window=generate_btn)
    return key_entry


def init_gui():
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Minecraft Key Generator")
    root.resizable(False, False)

    image_path = "minecraft.gif"
    canvas = set_background(root, image_path)

    key_entry = create_interface(canvas)

    return root, key_entry


if __name__ == "__main__":
    root, key_entry = init_gui()
    root.mainloop()
