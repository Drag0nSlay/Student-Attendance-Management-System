from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path
import string

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")

        # Main frame
        main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
        main_frame.pack()

        # Load and display image
        image_path = Path("Images/Chatbot1.jpg")  # Ensure correct folder path
        try:
            img_chat = Image.open(image_path)
            img_chat = img_chat.resize((200, 50), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img_chat)
        except FileNotFoundError:
            self.photoimg = None
            print(f"Image not found at {image_path}. Please ensure the image exists.")
        
        # Title Label
        Title_label = Label(
            main_frame,
            bd=3,
            relief=RAISED,
            anchor="nw",
            width=730,
            compound=LEFT,
            image=self.photoimg,
            text="CHATBOT SERVICE",
            font=("Impact", 30, "bold"),
            fg="powder blue",
            bg="white",
        )
        Title_label.pack(side=TOP)

        # Scrollable text area
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(
            main_frame,
            width=65,
            height=20,
            bd=3,
            relief=RAISED,
            font=("Georgia", 14),
            yscrollcommand=self.scroll_y.set,
        )
        self.scroll_y.config(command=self.text.yview)  # Ensure proper linking
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)

        # Button frame
        btn_frame = Frame(self.root, bd=4, bg="white", width=730)
        btn_frame.pack()

        label_1 = Label(
            btn_frame,
            text="Type Something",
            font=("Impact", 14),
            fg="powder blue",
            bg="white",
        )
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = ttk.Entry(btn_frame, width=40, font=("times new roman", 15))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)
        self.entry.bind("<Return>", self.enter_pressed)

        self.send_btn = Button(
            btn_frame,
            text="Send>>",
            command=self.send,
            font=("Georgia", 15, "bold"),
            width=8,
            bg="powder blue",
        )
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(
            btn_frame,
            text="Clear Data",
            command=self.clear_text,
            font=("Arial", 15, "bold"),
            width=8,
            bg="orange",
            fg="white",
        )
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ""
        self.label_2 = Label(
            btn_frame,
            text=self.msg,
            font=("Impact", 14),
            fg="red",
            bg="white",
        )
        self.label_2.grid(row=1, column=1, padx=5, sticky=W)

    def send(self):
        user_input = self.entry.get().strip()
        normalized_input = self.normalize_input(user_input)
        send_msg = f'\t\t\tYou: {self.entry.get()}'
        self.text.insert(END, f'\n{send_msg}')

        if not user_input:
            self.msg = "Please enter some input"
            self.label_2.config(text=self.msg, fg="red")
        else:
            self.msg = ""
            self.label_2.config(text=self.msg, fg="red")

        responses = {
            "hello": "Hi",
            "hi": "Hello",
            "how are you": "Fine, and you?",
            "fantastic": "Nice to hear!",
            "who created you": "I was created by Aman Kothari.",
            "what is your name": "My name is SAMGPT! You can think of me as your friendly AI assistant, here to help with your questions, ideas, and tasks. 😊 If you'd like, you can even give me a nickname!",
            "can you speak hindi": "I'm still learning it...",
            "what is machine learning": "Machine Learning (ML) is a branch of artificial intelligence (AI) that enables computers to learn and make decisions or predictions without being explicitly programmed. Instead of following fixed instructions, ML systems use data to identify patterns and improve their performance over time.",
            "how does face recognition work": "Face recognition works by using algorithms and machine learning techniques to analyze and identify faces from images or video.",
            "how does facial recognition work step by step": "Step 1: Face Detection. The camera detects and locates the image of a face, either alone or in a crowd. ... Step 2: Face analysis. Next, an image of the face is captured and analyzed.",
            "bye": "Thank you for chatting!",
        }
        bot_response = responses.get(normalized_input, "Sorry, I didn't get it.")
        self.text.insert(END, f'\n\nBot: {bot_response}')  # Add bot response to the text widget
        self.text.yview(END)
        self.entry.delete(0, END)

    def normalize_input(self, text):
        text = text.translate(str.maketrans("", "", string.punctuation)).lower()
        return text.strip()

    def clear_text(self):
        self.text.delete("1.0", END)
        self.entry.delete(0, END)

    def enter_pressed(self, event):
        self.send()

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()