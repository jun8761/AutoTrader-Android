from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login_popup import LoginPopup
from exchange_selector import ExchangeSelectorScreen
from telegram_config_ui import TelegramConfigScreen
from trader import TraderScreen

class RootScreenManager(ScreenManager):
    pass

class AutoTraderApp(App):
    def build(self):
        sm = RootScreenManager()
        login = LoginPopup()
        login.open()
        sm.add_widget(ExchangeSelectorScreen(name='exchange'))
        sm.add_widget(TelegramConfigScreen(name='telegram_config'))
        sm.add_widget(TraderScreen(name='trader'))
        return sm

if __name__ == '__main__':
    AutoTraderApp().run()