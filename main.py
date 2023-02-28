from aiogram import Bot, Dispatcher, executor, types
import classes
import markups

a = classes.Check()

bot = Bot(token='5407299648:AAHuiFOIBLjV0mQI0s9h7FNf9DV1-SMflag')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def strt(message: types.Message):
    await message.answer('Что нужно ?', reply_markup=markups.markup1)


@dp.message_handler(lambda message: message.text == 'Калькулятор рейда')
async def next(message: types.Message):
    await message.answer('Что ?', reply_markup=markups.markup2)


@dp.message_handler(lambda message: message.text in ['Дверь'])
async def get_chto (message:types.Message):
    global a
    a.__setattr__('chto', message.text)
    await message.answer('Какого качества ?', reply_markup=markups.markup3)


@dp.message_handler(lambda message: message.text in ['Дерево', 'Металл', 'МВК'])
async def get_qual(message:types.Message):
    global a
    a.__setattr__('qual', message.text)
    await message.answer('Чем ?', reply_markup=markups.markup4)


@dp.message_handler(lambda message: message.text in ['C4', 'Ракета', 'Бобовая граната', 'Связка боб. гранат', 'Разрывной патрон','Каменный патрон'])
async def get_chem(message:types.Message):
    global a
    a.__setattr__('chem', message.text)
    a.set_dict()
    await message.answer(a.cnt_raid())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)