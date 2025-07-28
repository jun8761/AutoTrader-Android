from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys

class LoginPopup(Popup):
    def __init__(self, **kwargs):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text='관리자 코드 입력'))
        self.code_input = TextInput(password=True, multiline=False)
        content.add_widget(self.code_input)
        btn_layout = BoxLayout(size_hint_y=None, height=40)
        ok = Button(text='확인')
        ok.bind(on_press=self.verify)
        btn_layout.add_widget(ok)
        content.add_widget(btn_layout)
        super().__init__(title='Admin Login', content=content,
                         size_hint=(None, None), size=(300, 200), auto_dismiss=False)

    def verify(self, instance):
        if self.code_input.text == '0727':
            self.dismiss()
        else:
            sys.exit(0)