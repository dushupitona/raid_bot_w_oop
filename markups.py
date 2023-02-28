from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button1 = KeyboardButton('Калькулятор рейда')

button2 = KeyboardButton('Дверь')

button3 = KeyboardButton('Дерево')
button4 = KeyboardButton('Металл')
button5 = KeyboardButton('МВК')

button6 = KeyboardButton('C4')
button7 = KeyboardButton('Ракета')
button8 = KeyboardButton('Бобовая граната')
button9 = KeyboardButton('Связка боб. гранат')
button10 = KeyboardButton('Разрывной патрон')
button11 = KeyboardButton('Каменный патрон')

markup1 = ReplyKeyboardMarkup().add(
    button1)

markup2 = ReplyKeyboardMarkup().add(
    button2)
#'C4', 'Ракета', 'Бобовая граната', 'Связка боб. гранат',\
# 'Разрывной патрон','Каменный патрон'


markup3 = ReplyKeyboardMarkup().add(button3).add(button4).add(button5)

markup4 = ReplyKeyboardMarkup().row(button6, button7).row(button8, button9)\
    .row(button10, button11)