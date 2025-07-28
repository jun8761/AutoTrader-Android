from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from api_manager import save_config

class ExchangeSelectorScreen(Screen):
    def on_enter(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.spinner = Spinner(
            text='거래소 선택',
            values=('upbit', 'bithumb', 'coinone'),
            size_hint=(1, None), height=44)
        self.api_input = TextInput(hint_text='API 키', multiline=False)
        self.secret_input = TextInput(hint_text='Secret 키', password=True, multiline=False)
        btn = Button(text='저장 및 다음', size_hint=(1, None), height=44)
        btn.bind(on_press=self.save_and_next)
        layout.add_widget(self.spinner)
        layout.add_widget(self.api_input)
        layout.add_widget(self.secret_input)
        layout.add_widget(btn)
        self.add_widget(layout)

    def save_and_next(self, instance):
        exchange = self.spinner.text
        api = self.api_input.text.strip()
        secret = self.secret_input.text.strip()
        save_config({'exchange': exchange, 'api': api, 'secret': secret})
        self.manager.current = 'telegram_config'