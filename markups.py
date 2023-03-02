from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



button_strt_ask = KeyboardButton('Калькулятор рейда')

button_door = KeyboardButton('Дверь')
button_grg = KeyboardButton('Гаражная дверь')
button_wndw = KeyboardButton('Оконная решетка')
button_wall = KeyboardButton('Стена')
button_big_wall = KeyboardButton('Ворота/Большая стена')

button_wood = KeyboardButton('Дерево')
button_metal = KeyboardButton('Металл')
button_HQM = KeyboardButton('МВК')
button_stone = KeyboardButton('Камень')

button_C4 = KeyboardButton('C4')
button_rocket = KeyboardButton('Ракета')
button_bob_grnd = KeyboardButton('Бобовая граната')
button9_bundle_bob_grnd = KeyboardButton('Связка боб. гранат')
button_expl_ammo = KeyboardButton('Разрывной патрон')
button11_stn_ammo = KeyboardButton('Каменный патрон')

markup_ask = ReplyKeyboardMarkup().add(
    button_strt_ask)

markup_chto = ReplyKeyboardMarkup().row(button_door,button_grg).row(button_wall, button_wndw)\
    .row(button_big_wall)

markup_qual1 = ReplyKeyboardMarkup().add(button_wood).add(button_metal).add(button_HQM)

markup_qual2 = ReplyKeyboardMarkup().add(button_wood).add(button_stone)

markup_qual3 = ReplyKeyboardMarkup().add(button_wood).add(button_stone).add(button_metal).add(button_HQM)

markup_rd_f_wood_d = ReplyKeyboardMarkup().row(button_C4, button_rocket).row\
    (button_bob_grnd, button9_bundle_bob_grnd).row(button_expl_ammo, button11_stn_ammo)

markup_rd = ReplyKeyboardMarkup().row(button_C4, button_rocket).row\
    (button_bob_grnd, button9_bundle_bob_grnd).row(button_expl_ammo)
