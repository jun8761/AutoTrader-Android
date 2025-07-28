from kivy.uix.screenmanager import Screen
import threading
import time
import pyupbit
from api_manager import load_config
from notifier import send_telegram

class TraderScreen(Screen):
    def on_enter(self):
        worker = TraderWorker()
        worker.start()

class TraderWorker:
    def __init__(self):
        cfg = load_config()
        api, secret = cfg['api'], cfg['secret']
        self.upbit = pyupbit.Upbit(api, secret) if cfg['exchange']=='upbit' else None
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self.run).start()

    def run(self):
        while self.running:
            try:
                price = pyupbit.get_current_price('KRW-BTC')
                krw = self.upbit.get_balance('KRW')
                if price and krw > 6000:
                    self.upbit.buy_market_order('KRW-BTC', 5000)
                    send_telegram(f"[매수] BTC: {price}")
                time.sleep(60)
            except Exception as e:
                send_telegram(f"[오류] {e}")
                time.sleep(60)