from aiogram import Bot, Dispatcher, executor, types
import classes
import markups
from tokenn import token_key

a = classes.Check()

bot = Bot(token=token_key)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def strt(message: types.Message):
    await message.answer('Что нужно ?', reply_markup=markups.markup_ask)


@dp.message_handler(lambda message: message.text == 'Калькулятор рейда')
async def next(message: types.Message):
    await message.answer('Что ?', reply_markup=markups.markup_chto)


@dp.message_handler(lambda message: message.text in ['Гаражная дверь'])
async def get_chto_grg(message: types.Message):
    global a
    a.__setattr__('chto', message.text)
    a.__setattr__('qual', '')
    await message.answer('Чем ?', reply_markup=markups.markup_rd)


@dp.message_handler(lambda message: message.text in ['Дверь', 'Оконная решетка'])
async def get_chto_dflt(message: types.Message):
    global a
    a.__setattr__('chto', message.text)
    await message.answer('Какого качества ?', reply_markup=markups.markup_qual1)


@dp.message_handler(lambda message: message.text in ['Стена'])
async def get_chto_wall(message: types.Message):
    global a
    a.__setattr__('chto', message.text)
    await message.answer('Какого качества ?', reply_markup=markups.markup_qual3)


@dp.message_handler(lambda message: message.text in ['Ворота/Большая стена'])
async def get_chto_bigwall(message: types.Message):
    global a
    a.__setattr__('chto', message.text)
    await message.answer('Какого качества ?', reply_markup=markups.markup_qual2)


@dp.message_handler(lambda message: message.text in ['Дерево', 'Металл', 'Камень', 'МВК'])
async def get_qual(message: types.Message):
    global a
    a.__setattr__('qual', message.text)
    if getattr(a, 'qual') == 'Дерево' and getattr(a, 'chto') == 'Дверь':
        await message.answer('Чем ?', reply_markup=markups.markup_rd_f_wood_d)         #обрабатываем исклбчение каменный патрон
    else:
        await message.answer('Чем ?', reply_markup=markups.markup_rd)


@dp.message_handler(lambda message: message.text in ['C4', 'Ракета', 'Бобовая граната', 'Связка боб. гранат', 'Разрывной патрон', 'Каменный патрон'])
async def get_chem(message: types.Message):
    global a
    a.__setattr__('chem', message.text)
    a.set_dict()
    await message.answer(a.cnt_raid())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)