class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class WitchArmy(Enemy):
    def __init__(self):
        super().__init__(name="Witch Army", hp=10, damage=10)
 
class Nithral(Enemy):
    def __init__(self):
        super().__init__(name="Nithral", hp=30, damage=15)

class Snake(Enemy):
    def __init__(self):
        super().__init__(name="Snake", hp=20, damage=2)

class Berserker(Enemy):
    def __init__(self):
        super().__init__(name="Berserker", hp=25, damage=5)

class Witcher(Enemy):
    def __init__(self):
        super().__init__(name="Witcher", hp=25, damage=7)

class Bear(Enemy):
    def __init__(self):
        super().__init__(name="Bear", hp=25, damage=3)

class Guard(Enemy):
    def __init__(self):
        super().__init__(name="Guard", hp=25, damage=15)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=8)

class Monster(Enemy):
    def __init__(self):
        super().__init__(name="Monster", hp=25, damage=10)