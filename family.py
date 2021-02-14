# -*- coding: utf-8 -*-

from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cats_food = 30
    def mudding(self):
        self.mud += 5

    def __str__(self):
        return f'в доме: денег: {self.money}, еды: {self.food}, грязи: {self.mud}, кошачей еды: {self.cats_food}'

class Human:
    tottal_food = 0
    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 30
        self.happyness = 100
    def __str__(self):
        return f'член семьи: {self.name}, сытость: {self.fullness}, счастье: {self.happyness}'
    def pet_the_cat(self):
        self.happyness += 5
        self.fullness -= 10
        print(f'{self.name} целый день гладит кота')
    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        Human.tottal_food += 30
        print(f'{self.name} поел')


class Husband(Human):
    tottal_money = 0
    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0 or self.happyness < 10:
            print(f'{self.name} умер...')
            return
        if self.fullness < 15:
            serge.eat()
        elif self.happyness < 10:
            serge.gaming()
        elif self.house.money < 60:
            serge.work()
        elif dice == 1:
            serge.gaming()
        elif dice == 2:
            self.pet_the_cat()
        else:
            serge.work()
        if self.house.mud > 90:
            self.happyness -= 10
    def work(self):
        self.fullness -= 10
        self.house.money += 150
        Husband.tottal_money += 150
        print(f'{self.name} сходил на работу')

    def gaming(self):
        self.fullness -= 10
        self.happyness += 20
        print(f'{self.name} играет WoT')


class Wife(Human):
    tottal_fur_coat = 0
    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0 or self.happyness < 10:
            print(f'{self.name} умерла...')
            return
        if self.fullness < 15:
            masha.eat()
        elif self.happyness < 10:
            masha.buy_fur_coat()
        elif self.house.food < 65 or self.house.cats_food < 15:
            masha.shopping()
        elif dice == 1:
            masha.shopping()
        elif dice == 2:
            self.pet_the_cat()
        else:
            masha.clean_house()
        if self.house.mud > 90:
            self.happyness -= 10
        if self.house.mud < 0:
            self.house.mud = 0
    def shopping(self):
        if self.house.money > 160:
            self.fullness -= 10
            self.house.money -= 150
            self.house.food += 100
            self.house.cats_food += 20
            print(f'{self.name} закупает продукты')
        else:
            print('Нет денег')

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.fullness -= 10
            self.house.money -= 350
            self.happyness += 60
            print(f'{self.name} покупает шубу')
            Wife.tottal_fur_coat += 1
        else:
            print('Нет денег')
    def clean_house(self):
        self.fullness -= 10
        self.house.mud -= 100
        print(f'{self.name} делает уборку')

class Cat:
    tottal_cats_food = 0
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house
    def __str__(self):
        return f'питомец: {self.name}, сытость: {self.fullness}'

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0:
            print(f'{self.name} умер...')
            return
        if self.fullness < 15:
            cat.eat()

        elif dice == 1:
            cat.sleep()
        else:
            cat.soil()

    def eat(self):
        self.fullness += 20
        self.house.cats_food -= 10
        Cat.tottal_cats_food += 10
        print(f'{self.name} поел')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} поспал')

    def soil(self):
        self.fullness -= 10
        self.house.mud += 10
        print(f'{self.name} подрал обои')

home = House('My_sweet_home')
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
cat = Cat(name='Мурзик', house=home)

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    home.mudding()
    serge.act()
    masha.act()
    cat.act()
    print(serge)
    print(masha)
    print(cat)
    print()
    print(home)
    print()
print(f'Всего заработано денег: {Husband.tottal_money}')
print(f'Всего съедено еды: {Human.tottal_food}')
print(f'Всего куплено шуб: {Wife.tottal_fur_coat}')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
