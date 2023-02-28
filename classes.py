import dictry

class Check:

    def __init__(self, chto=str(), qual=str(), chem=str(), dict_raid=dict):
        self.dict_raid = dict_raid
        self.qual = qual
        self.chem = chem
        self.chto = chto

    def __setattr__(self, key, value):
        if key == 'chto':
            self.__dict__[key] = value
        elif key == 'qual':
            self.__dict__[key] = value
        elif key == 'chem':
            self.__dict__[key] = value

    def set_dict(self):
        if self.chto == 'Дверь':
            self.__dict__['dict_raid'] = dictry.door[self.qual][self.chem]

    def cnt_raid(self):
        return f'Вам понадобится {self.dict_raid} {self.chem.lower()}'

