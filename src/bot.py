import telebot
import setting
from telebot import types
import db

bot = telebot.TeleBot(setting.bot_token)

common_command = ['✎', '🗑']

# Генерация клавиатуры
def change_keyboard_inline(answer = []):
    keyboard = types.InlineKeyboardMarkup()
    for i in answer:
        keyboard.add(types.InlineKeyboardButton(text=i[0], callback_data=i[1]))
    return keyboard

def change_keyboard_inline_row(answer = []):
    keyboards = []
    keyboard = types.InlineKeyboardMarkup()
    for i in answer:
        keyboards.append(keyboard.add(types.InlineKeyboardButton(text=common_command[0], callback_data=i), types.InlineKeyboardButton(text=common_command[1], callback_data=i)))
    return keyboards

def change_keyboard_keys(command = []):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    for i in command:
        markup.add(types.KeyboardButton(i))
    return markup

# Клавиатура по умолчанию
default_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
default_keyboard.row('+ задачу', '+ проект')
default_keyboard.row('Входящие', 'Сегодня', 'Скоро') 


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    db.SQLCommand.add_user(message.chat.id)
    bot.send_message(message.from_user.id, 'Привет', reply_markup=default_keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '+ проект':
        mesg = bot.send_message(message.chat.id,'Напишите название проекта', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mesg, add_project)
    elif message.text == '+ задачу':
        data = db.SQLCommand.show_project(message.chat.id)
        # print(data)
        btns = []
        no_project_list = db.SQLCommand.use_def_list(message.chat.id)
        for i in data:
            btns.append([i[0], "in_project|" + str(i[1])])
        btns.append(['Пропустить', 'in_list|' + str(no_project_list)])
        keyboard = change_keyboard_inline(btns)
        mesg = bot.send_message(message.chat.id,'Выберите проект', reply_markup=keyboard)
    elif message.text == 'Входящие':
        data = db.SQLCommand.show_task_list(message.from_user.id)
        if data is None:
            bot.send_message(message.from_user.id, 'Нет задач', reply_markup=default_keyboard)
        else:
            for i in data:
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton(text=common_command[0], callback_data='edit_task|' + str(i[1])), 
                types.InlineKeyboardButton(text=common_command[1], callback_data='delete_task|' + str(i[1])))
                bot.send_message(message.from_user.id, i[0], reply_markup=keyboard)
                keyboard = ''
    elif message.text == 'Сегодня':
        bot.send_message(message.from_user.id, message.text, reply_markup=default_keyboard)
    elif message.text == 'Скоро':
        bot.send_message(message.from_user.id, message.text, reply_markup=default_keyboard)
    else:
        bot.send_message(message.from_user.id, message.from_user.id,reply_markup=default_keyboard)


# Callbacks
def add_project(message):
    project_id = db.SQLCommand.add_project(message.chat.id, message.text)
    callback = 'add_list|' + str(project_id)
    keyboard = change_keyboard_inline([['Вернуться', 'back'], ['Добавить лист', callback]])
    bot.send_message(message.chat.id, 'Проект создан', reply_markup=keyboard)

def add_list(message, project_id):
    list_id = db.SQLCommand.add_list(project_id, message.text)
    bot.send_message(message.chat.id, 'Лист создан')

def add_task(message, list_id):
    list_id = db.SQLCommand.add_task(message.text, list_id)
    bot.send_message(message.chat.id, 'Задание создано', reply_markup=default_keyboard)


# Handlers
@bot.callback_query_handler(func=lambda call: True)
def ans(call):
    data = str(call.data).split('|')
    if data[0] == 'add_list':
        mesg = bot.send_message(call.message.chat.id, 'Напишите название листа', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mesg, add_list, data[1])
    elif data[0] == 'in_project':
        query = db.SQLCommand.show_lists(data[1])
        btns = []
        for i in query:
            btns.append([i[0], "in_list|" + str(i[1])])
        keyboard = change_keyboard_inline(btns)
        mesg = bot.send_message(call.message.chat.id, 'Выберите лист', reply_markup=keyboard)
    elif data[0] == 'in_list':
        mesg = bot.send_message(call.message.chat.id, 'Напишите название задачи', reply_markup=types.ReplyKeyboardRemove())
        # print(data)
        bot.register_next_step_handler(mesg, add_task, data[1])
    elif data[0] == 'back':
        bot.send_message(call.message.chat.id, 'Выберите действие', reply_markup=default_keyboard)


# Дебаг
print('bot is working')

bot.polling(none_stop=True, interval=0)
