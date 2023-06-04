import random
import telebot
from telebot import types


bot_token = '6051637437:AAFrTSDyGI1WRyt-TNs6iErLec-BF3LwM1U'


bot = telebot.TeleBot(bot_token)


def win(choice):
    gesture = ['🖐', '✌', '✊']
    bot_choice = random.choice(gesture)
    if choice in gesture:
        if choice == gesture[0] and bot_choice == gesture[0]:
            return f'{gesture[0]}\nDraw'
        elif choice == gesture[0] and bot_choice == gesture[1]:
            return f'{gesture[1]}\nI won'
        elif choice == gesture[0] and bot_choice == gesture[2]:
            return f'{gesture[2]}\nYou won'
        elif choice == gesture[1] and bot_choice == gesture[1]:
            return f'{gesture[1]}\nDraw'
        elif choice == gesture[1] and bot_choice == gesture[2]:
            return f'{gesture[2]}\nI won'
        elif choice == gesture[1] and bot_choice == gesture[0]:
            return f'{gesture[0]}\nYou won'
        elif choice == gesture[2] and bot_choice == gesture[2]:
            return f'{gesture[2]}\nDraw'
        elif choice == gesture[2] and bot_choice == gesture[0]:
            return f'{gesture[0]}\nI won'
        elif choice == gesture[2] and bot_choice == gesture[1]:
            return f'{gesture[1]}\nYou won'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}. Let's play a game of 'Rock, Paper, Scissors'")
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('🖐')
    button2 = types.KeyboardButton('✌')
    button3 = types.KeyboardButton('✊')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, f"Rock Paper Scissors - One Two Three", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('🖐')
    button2 = types.KeyboardButton('✌')
    button3 = types.KeyboardButton('✊')
    keyboard.add(button1, button2, button3)
    won = win(message.text)
    bot.reply_to(message, f"{won}\nRock Paper Scissors - One Two Three", reply_markup=keyboard)


bot.polling()
