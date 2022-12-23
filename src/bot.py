import telebot;
import setting
from telebot import types
import db

bot = telebot.TeleBot(setting.bot_token);

start_commands = ['Задачи', 'Проекты']

task_command = ['Показать', 'Создать новую']
project_command = ['Показать', 'Создать новый', 'Дать доступ']

# Генерация клавиатуры
def change_keyboard(command = []):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in command:
        key = types.KeyboardButton(i)
        markup.add(key)
    return markup


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    markup = change_keyboard(start_commands)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    
    if message.text in start_commands:
        if message.text == 'Задачи':
            markup = change_keyboard(task_command)
            bot.send_message(message.from_user.id, message.chat.id,reply_markup=markup)
            db.SQLCommand.show_all_tasks(message.chat.id)
        elif message.text == 'Проекты':
            markup = change_keyboard(project_command)
            bot.send_message(message.from_user.id, "ты выбрал проекты",reply_markup=markup)
    else:
        print('in else')

    if message.text == "/start":
        db.SQLCommand.add_user(message.chat.id)
        bot.send_message(message.from_user.id, "start")

    # if message.text == "Привет":
        # item1 = types.KeyboardButton("Кнопка 1")
        # markup.add(item1)
        # bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # elif message.text == "/help":
        # item1 = types.KeyboardButton("Кнопка 2")
        # markup.add(item1)
        # bot.send_message(message.from_user.id, "Напиши привет")
    # else:
        # item1 = types.KeyboardButton("Кнопка 3")
        # markup.add(item1)
        # bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    # bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



# Дебаг
print('bot is working')

bot.polling(none_stop=True, interval=0)