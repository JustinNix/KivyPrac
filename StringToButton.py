from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class StringToButtonApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.sentence_input = input("Enter a sentence")
        self.split_sentence = self.sentence_input.split()
        self.sentence_list = [str(word) for word in self.split_sentence]

    def build(self):
        self.title = "Turn a string into buttons"
        self.root = Builder.load_file('StringToButton.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for word in self.sentence_list:
            # create a button for each phonebook entry
            temp_button = Button(text=word)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

StringToButtonApp().run()