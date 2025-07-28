from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from api_manager import save_config, load_config

class TelegramConfigScreen(Screen):
    def on_enter(self):
        cfg = load_config()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.token_input = TextInput(hint_text='텔레그램 봇 토큰', text=cfg.get('telegram_token', ''), multiline=False)
        self.chatid_input = TextInput(hint_text='Chat ID', text=cfg.get('telegram_chat_id', ''), multiline=False)
        btn = Button(text='저장 및 시작', size_hint=(1, None), height=44)
        btn.bind(on_press=self.save_and_next)
        layout.add_widget(self.token_input)
        layout.add_widget(self.chatid_input)
        layout.add_widget(btn)
        self.add_widget(layout)

    def save_and_next(self, instance):
        cfg = load_config()
        cfg['telegram_token'] = self.token_input.text.strip()
        cfg['telegram_chat_id'] = self.chatid_input.text.strip()
        save_config(cfg)
        self.manager.current = 'trader'