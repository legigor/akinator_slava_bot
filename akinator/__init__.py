import telebot
from telebot import types


class Akinator:

    def __init__(self, bot: telebot.TeleBot, msg: types.Message):
        self.bot = bot
        self.msg = msg

    def start(self):
        pass

