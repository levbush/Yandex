class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor: 'BaseCharacter', target: 'BaseCharacter'):
        if target.is_alive():
            if (abs(target.pos_x - actor.pos_x)**2 + abs(target.pos_y - actor.pos_y)**2)**0.5 <= self.range:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.get_damage(self.damage)
            else:
                print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции {self.get_coords()} с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapon = None
        self.inventory = []
        self.i = 0

    def hit(self, target):
        if self.weapon:
            if isinstance(target, BaseEnemy):
                self.weapon.hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon: Weapon):
        if isinstance(weapon, Weapon):
            self.inventory += [weapon]
            if not self.weapon:
                self.weapon = weapon
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if self.inventory:
            if self.inventory[1:]:
                self.i += 1
                if self.i == len(self.inventory):
                    self.i = 0
                self.weapon = self.inventory[self.i]
                print(f'Сменил оружие на {self.weapon}')
            else:
                print('У меня только одно оружие')
        else:
            print('Я безоружен')

    def heal(self, amount):
        self.hp = min(200, self.hp + amount)
        print(f'Полечился, теперь здоровья {self.hp}')