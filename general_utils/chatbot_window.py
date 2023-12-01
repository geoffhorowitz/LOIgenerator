import tkinter as tk
from tkinter import ttk

class ChatbotApp:
    def __init__(self, response_model=None):
        self.response_model = response_model

        # set up window root
        self.root = tk.Tk()

        # Create a chatbot frame to contain the text box widget and the submit button
        chatbot_frame = ttk.Frame(self.root)

        # Create a text box widget to display the chatbot's responses
        self.chatbot_output = tk.Text(chatbot_frame)

        # Create a text box widget for the user to enter input
        self.user_input = ttk.Entry(chatbot_frame)

        # Create a button for the user to submit their input
        submit_button = ttk.Button(chatbot_frame, text="Submit", command=self.submit_input)
        # Bind the `Enter` key to the `submit_input()` method
        self.user_input.bind("<Shift-Return>", self.submit_input)

        # Create a label widget to display the text
        label = tk.Label(chatbot_frame, text="Type your response in below. Press Submit or Shift+Enter to submit your text to the LLM")

        # Pack the widgets into the chatbot frame
        self.chatbot_output.pack(fill=tk.BOTH, expand=True)
        label.pack()
        self.user_input.pack(fill=tk.X, expand=True)
        submit_button.pack()

        # Place the chatbot frame in the root window
        chatbot_frame.pack(fill=tk.BOTH, expand=True)

        # Start the mainloop
        self.root.mainloop()

    def submit_input(self, event=None):
        user_input_text = self.user_input.get()
        self.chatbot_output.insert("end", f"User: {user_input_text}\n")

        # TODO: Call the chatbot to generate a response
        try:
            if self.response_model:
                chatbot_response = self.response_model(user_input_text)
            else:
                chatbot_response = "Chatbot: Response"

            print('chatbot_response: '+chatbot_response)
            if chatbot_response:
                self.chatbot_output.insert("end", chatbot_response+"\n")
        except Exception as e:
            print('Error occured')
            print(e)

        # Clear the user input text box
        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    ChatbotApp()