import telebot
import db
from telebot import types
from game import victory_condition


bot_token = '6051637437:AAFrTSDyGI1WRyt-TNs6iErLec-BF3LwM1U'

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['/start'])
def start_message(message):
    if not db.check_user(message.from_user.username):
        db.add_user(message.from_user.username)
    bot.send_message(message, f"Hello {message.from_user.first_name}. Let's play a game of 'Rock, Paper, Scissors'")
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('🖐')
    button2 = types.KeyboardButton('✌')
    button3 = types.KeyboardButton('✊')
    button4 = types.KeyboardButton('🏆')
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, f"Rock Paper Scissors - One Two Three", reply_markup=keyboard)


@bot.message_handler()
def handle_message(message):
    if not db.check_user(message.from_user.username):
        db.add_user(message.from_user.username)
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('🖐')
    button2 = types.KeyboardButton('✌')
    button3 = types.KeyboardButton('✊')
    button4 = types.KeyboardButton('🏆')
    keyboard.add(button1, button2, button3, button4)
    if message.text in ('🖐', '✌', '✊'):
        bot.send_message(message.chat.id, victory_condition(message.text, message.from_user.username)[0])
        bot.send_message(message.chat.id, f"{victory_condition(message.text, message.from_user.username)[1]}\n"
                                          f"Rock Paper Scissors - One Two Three", reply_markup=keyboard)
    elif message.text == '🏆':
        bot.send_message(message.chat.id, f"You have {db.get_score(message.from_user.username)} points.", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, f"Choose one of the options", reply_markup=keyboard)


bot.polling()
