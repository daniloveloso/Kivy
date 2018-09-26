#conding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.floatlayout import FloatLayout

def build():
    layout = FloatLayout()

    ed = TextInput(text="vai Agora vai")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.y = 60
    ed.x = 250
    bt = Button(text="Click Aqui")
    bt.size_hint = None, None

    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout

janela = App()
janela.build = build
janela.run()