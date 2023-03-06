import dictry
from aiogram import Bot, Dispatcher, executor, types

class Check:

    def __init__(self, chto=str(), qual=str(), chem=str(), dict_raid=dict, dict_res=dict):
        self.dict_raid = dict_raid
        self.dict_res = dict_res
        self.qual = qual
        self.chem = chem
        self.chto = chto

    def __setattr__(self, key, value):
        self.__dict__['dict_res'] = dictry.reslist
        if key == 'chto':
            self.__dict__[key] = value
        elif key == 'qual':
            self.__dict__[key] = value
        elif key == 'chem':
            self.__dict__[key] = value

    def set_dict(self):
        if self.chto == 'Дверь':
            self.__dict__['dict_raid'] = dictry.door[self.qual][self.chem]
        elif self.chto == 'Оконная решетка':
            self.__dict__['dict_raid'] = dictry.window[self.qual][self.chem]
        elif self.chto == 'Стена':
            self.__dict__['dict_raid'] = dictry.wall[self.qual][self.chem]
        elif self.chto == 'Гаражная дверь':
            self.__dict__['dict_raid'] = dictry.garage[self.chem]
        elif self.chto == 'Ворота/Большая стена':
            self.__dict__['dict_raid'] = dictry.big_wall[self.qual][self.chem]

    def cnt_raid(self):
        return f'Вам понадобится {self.dict_raid} {self.chem.lower()}'

    def ret_vlme(self):
        return self.dict_raid

    def cnt_res(self):
        return self.dict_res[self.chem]


