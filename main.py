import telebot
from telebot import types
import logging

bot = telebot.TeleBot("<api_token>")

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(func=lambda m: True)
def random_message(message):
    bot.send_message(message.chat.id, 'Если хочешь поиграть, нажми /start')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, скоро я начну задавать вопросы :)')


bot.polling()
