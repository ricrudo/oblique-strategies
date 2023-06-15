from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from random import choice
from string import punctuation

with open('list.txt') as f:
    CARDS = [x[:-1] for x in f.readlines()]


Builder.load_string('''
<Base>:
    orientation: 'vertical'
    ScreenManager:
        size_hint: 1, 0.8
        id: sm
        Screen:
            name: 'scr_1'
            CustomLabel:
                id: label1
        Screen:
            name: 'scr_2'
            CustomLabel:
                id: label2
    Button:
        size_hint: 1, 0.2
        text: "RANDOM CARD"
        on_release: root.new_card()


<CustomLabel@Label>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    color: 0,0,0,1
    text_size: self.size[0] - (self.parent.height * 0.3), self.size[1] - (self.parent.height * 0.3)
    font_size: '20dp'
    strip: True
    halign: 'center'
    valign: 'middle'

''')

class Base(BoxLayout):

    card = ''

    def new_card(self):
        self.updateCard()
        if self.ids.sm.current == 'scr_1':
            self.ids.sm.current = 'scr_2'
            self.ids.label2.text = self.card
        else:
            self.ids.sm.current = 'scr_1'
            self.ids.label1.text = self.card

    def updateCard(self):
        self.card = choice(CARDS)
        if self.card[-1] not in punctuation:
            self.card += '.'

class OBLIQUE_STRATEGYApp(App):

	def build(self):
		return Base()

if __name__ == '__main__':
	OBLIQUE_STRATEGYApp().run()
