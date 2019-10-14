import telebot
import logging
import os

from telebot import types

TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN)
telebot.logger.setLevel(logging.DEBUG)


markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add('Yes')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Ваш персонаж реален???", reply_markup=markup)
    bot.register_next_step_handler(message, q1)


def q1(message):
    bot.send_message(message.chat.id, "вы встречали его?", reply_markup=markup)
    bot.register_next_step_handler(message, q2)


def q2(message):
    bot.send_message(message.chat.id, "вы это он? ", reply_markup=markup)
    bot.register_next_step_handler(message, q3)


def q3(message):
    bot.send_message(message.chat.id, "ето ви!")


# bot.enable_save_next_step_handlers(delay=2, filename="./.handler-saves/step.save")
# bot.load_next_step_handlers()
bot.polling()
