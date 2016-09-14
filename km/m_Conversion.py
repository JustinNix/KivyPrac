from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Justin Nix'


class ConvertMtoKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        #Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

   # def handle_calculate(self, value):
       # """ handle calculation (could be button press or other call), output result to label widget """
        #result = value ** 2
        #self.root.ids.output_label.text = str(result)

ConvertMtoKmApp().run()