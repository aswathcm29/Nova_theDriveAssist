import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class FridayApp(App):
    def __init__(self):
        super().__init__()
        self.instructions = []

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        # Text input for instructions
        self.text_input = TextInput(font_size=16, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(self.text_input)

        # Button to submit instructions
        submit_button = Button(text="Submit", size_hint=(1, 0.1))
        submit_button.bind(on_press=self.submit_instruction)
        layout.add_widget(submit_button)

        # Scrollable view to display instructions and responses
        scroll_view = ScrollView()
        self.instructions_label = Label(text='', font_size=14, size_hint_y=None, height=500)
        scroll_view.add_widget(self.instructions_label)
        layout.add_widget(scroll_view)

        return layout

    def submit_instruction(self, instance):
        instruction = self.text_input.text.strip()
        self.text_input.text = ""

        if instruction:
            self.instructions.append(instruction)
            response = self.get_friday_response(instruction)
            self.display_response(instruction, response)

    def get_friday_response(self, instruction):
        # Process the instruction and get the response from your AI assistant
        # Modify this function to call the appropriate functions in your existing code
        response = "Friday's response: " + instruction  # Replace this with the actual response
        return response

    def display_response(self, instruction, response):
        self.instructions_label.text += "You: " + instruction + "\n"
        self.instructions_label.text += "Friday: " + response + "\n\n"
        self.instructions_label.height = max(self.instructions_label.texture_size[1], 500)
        self.instructions_label.text_size = (self.instructions_label.width, None)

if __name__ == '__main__':
    FridayApp().run()
