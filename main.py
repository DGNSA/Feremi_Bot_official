import os
import telebot

bot=telebot.TeleBot("2053848737:AAFAZNWiWVbnfo6QAPSG9ffkXbrtMmXrNXY")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hi I'm Feremi_Bot")

@bot.message_handler(commands=["hello"])
def send_hello(message):
    bot.send_message(message,"I'm Fine")

bot.polling()