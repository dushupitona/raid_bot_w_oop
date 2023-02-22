from dictry import *


class WoodDoor:
    def __init__(self, expl, p=int()):
        self.expl = expl
        self.p = p
        self.raidlist = raidlist
        self.reslist = reslist

    def cnt_expl(self):
        self.p = self.raidlist[self.expl]
        return f'Вам понадобится {self.p} {self.expl}'

    def cnt_res(self):
        return self.reslist[self.expl]


a = WoodDoor(str(input()))

print(a.cnt_expl())
print(a.cnt_res())

