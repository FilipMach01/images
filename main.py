import random
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import os
from dotenv import load_dotenv
import threading
from chords import chord_types
from sound import play_chord


class PexelsImageViewer(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv("PEXELS_API_KEY")
        if not self.api_key:
            raise ValueError("PEXELS_API_KEY environment variable is not set")

        # Configure the window
        self.title("Pexels Random Image Viewer")
        self.geometry("800x600")
        self.configure(bg='#f0f2f5')

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create and configure the image label
        self.image_label = ttk.Label(self.main_frame)
        self.image_label.pack(pady=10, fill=tk.BOTH, expand=True)

        self.image_index = 0

        # Create credits label
        # self.credits_label = ttk.Label(
        #     self.main_frame,
        #     text="",
        #     wraplength=700,
        #     justify="center"
        # )
        # self.credits_label.pack(pady=5)

        # Create loading label
        self.loading_label = ttk.Label(
            self.main_frame,
            text="Loading...",
            font=("Arial", 12)
        )

        # Create refresh button
        style = ttk.Style()
        style.configure("Custom.TButton", padding=10)
        self.refresh_button = ttk.Button(
            self.main_frame,
            text="Get New Image",
            command=self.load_new_image,
            style="Custom.TButton"
        )
        self.refresh_button.pack(pady=10)

        # Store the current PhotoImage
        self.current_photo = None

        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)
        for i, (category, chords) in enumerate(chord_types.items()):
            column_frame = ttk.Frame(self.buttons_frame)
            column_frame.grid(row=0, column=i, padx=10)
            buttons = []
            for chord,tones in chords.items():
                button = ttk.Button(column_frame, text=chord, command=lambda c=tones: play_chord(c))
                buttons.append(button)
                button.pack(pady=2)
        # Initial image load
        self.load_new_image()

    def show_loading(self):
        self.loading_label.pack(pady=10)
        self.refresh_button.config(state="disabled")

    def hide_loading(self):
        self.loading_label.pack_forget()
        self.refresh_button.config(state="normal")

    def fetch_image(self):
        headers = {
            "Authorization": self.api_key
        }

        response = requests.get(
            f"https://api.pexels.com/v1/search?query=nature&page={self.image_index}&per_page=1",
            headers=headers
        )

        if response.status_code != 200:
            raise Exception("Failed to fetch image")

        self.image_index += 1
        return response.json()['photos'][0]

    def load_new_image(self):
        def fetch_and_update():
            try:
                # Show loading state
                self.show_loading()

                # Fetch new image data
                image_data = self.fetch_image()

                # Download the image
                response = requests.get(image_data['src']['large'])
                img_data = BytesIO(response.content)

                # Open and resize image
                pil_image = Image.open(img_data)

                # Calculate new size maintaining aspect ratio
                display_width = 700
                ratio = display_width / pil_image.width
                display_height = int(pil_image.height * ratio)

                pil_image = pil_image.resize((int(display_width * 0.8), int(display_height * 0.8)),
                                             Image.Resampling.LANCZOS)

                # Convert to PhotoImage
                self.current_photo = ImageTk.PhotoImage(pil_image)

                # Update the image and credits
                self.image_label.configure(image=self.current_photo)

                # credits_text = f"Photo by {image_data['photographer']} on Pexels"
                # self.credits_label.configure(text=credits_text)

            except Exception as e:
                # self.credits_label.configure(text=f"Error: {str(e)}")
                print(f"Error: {str(e)}")

            finally:
                # Hide loading state
                self.hide_loading()

        # Run the image fetching in a separate thread
        threading.Thread(target=fetch_and_update, daemon=True).start()


if __name__ == "__main__":
    app = PexelsImageViewer()
    app.mainloop()
