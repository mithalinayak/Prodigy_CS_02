import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def keygen(seed, r, size):
    np.random.seed(int(seed * 1000000))
    key = np.random.randint(0, 256, size, dtype=np.uint8)
    return key

def choose_image():
    global img, height, width, channels
    filepath = filedialog.askopenfilename(
        title="Select an image",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.bmp"), ("all files", "*.*"))
    )
    if filepath:
        img = mpimg.imread(filepath)
        height, width, channels = img.shape
        key_label.config(text="Key generated: No")
        original_image_label.config(text="Original Image")
        encrypted_image_label.config(text="Encrypted Image")
        decrypted_image_label.config(text="Decrypted Image")
        update_image_display(img, original_image_canvas)

def save_image(image, title):
    if image is not None:
        filetypes = [("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")]
        save_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=filetypes)
        if save_path:
            plt.imsave(save_path, image)
            messagebox.showinfo(title, f"Image saved to {save_path}")

def update_image_display(image, canvas):
    resized_image = cv2.resize(image, (200, 200))
    image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    image_bytes = cv2.imencode(".png", image_rgb)[1].tobytes()
    img_tk = tk.PhotoImage(data=image_bytes)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk

def encrypt_image():
    global enimg, key, img, height, width, channels
    if img is not None:
        key = keygen(0.01, 3.95, height * width * channels)
        key_label.config(text="Key generated: Yes")
        z = 0
        enimg = np.zeros(shape=[height, width, channels], dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    enimg[i, j, k] = img[i, j, k] ^ key[z]
                    z += 1
        update_image_display(enimg, encrypted_image_canvas)
        save_button.config(state=tk.NORMAL)

def decrypt_image():
    global enimg, decimg, key, height, width, channels
    if enimg is not None:
        z = 0
        decimg = np.zeros(shape=[height, width, channels], dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    decimg[i, j, k] = enimg[i, j, k] ^ key[z]
                    z += 1
        update_image_display(decimg, decrypted_image_canvas)
        save_button.config(state=tk.NORMAL)

def exit_app():
    root.destroy()

# Initialize variables
img = None
enimg = None
decimg = None
key = None

# Create main window
root = tk.Tk()
root.title("Image Encryption Decryption")
root.configure(bg="#34495e")

# Style
button_style = {
    "font": ("Helvetica", 12),
    "bg": "#3498db",
    "fg": "#ecf0f1",
    "activebackground": "#2980b9",
    "activeforeground": "#ecf0f1",
    "width": 12,
    "height": 2
}
label_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#34495e",
    "fg": "#ecf0f1"
}

# Buttons
choose_button = tk.Button(root, text="Choose", command=choose_image, **button_style)
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_image, **button_style)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_image, **button_style)
save_button = tk.Button(root, text="Save", command=lambda: save_image(enimg if enimg is not None else decimg, "Save Image"), state=tk.DISABLED, **button_style)
exit_button = tk.Button(root, text="EXIT", command=exit_app, font=("Helvetica", 12), bg="#e74c3c", fg="#ecf0f1", activebackground="#c0392b", width=12, height=2)

# Labels
original_image_label = tk.Label(root, text="Original Image", **label_style)
encrypted_image_label = tk.Label(root, text="Encrypted Image", **label_style)
decrypted_image_label = tk.Label(root, text="Decrypted Image", **label_style)
key_label = tk.Label(root, text="Key generated: No", **label_style)

# Image Canvases
original_image_canvas = tk.Canvas(root, width=200, height=200, bg="#ecf0f1")
encrypted_image_canvas = tk.Canvas(root, width=200, height=200, bg="#ecf0f1")
decrypted_image_canvas = tk.Canvas(root, width=200, height=200, bg="#ecf0f1")

# Layout
choose_button.grid(row=0, column=0, padx=10, pady=10)
encrypt_button.grid(row=0, column=1, padx=10, pady=10)
decrypt_button.grid(row=0, column=2, padx=10, pady=10)
exit_button.grid(row=0, column=3, padx=10, pady=10)

key_label.grid(row=1, column=0, columnspan=4, padx=10, pady=(10, 0))

original_image_label.grid(row=2, column=0, padx=10, pady=10)
encrypted_image_label.grid(row=2, column=1, padx=10, pady=10)
decrypted_image_label.grid(row=2, column=2, padx=10, pady=10)

original_image_canvas.grid(row=3, column=0, padx=10, pady=10)
encrypted_image_canvas.grid(row=3, column=1, padx=10, pady=10)
decrypted_image_canvas.grid(row=3, column=2, padx=10, pady=10)

save_button.grid(row=4, column=1, padx=10, pady=10)

# Run main loop
root.mainloop()
