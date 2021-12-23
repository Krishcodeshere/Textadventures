import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this castle."""
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Equip(),actions.Heal()]
        else:
            return self.adjacent_moves()
            
class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        Beautiful princess Arya Stark has been locked away in a tower since she was captured as a baby by Witcher.
        Her magical long blonde hair has the power to provide eternal youth, and the evil Witcher uses this power.
        She is waiting for someone to rescue her from the Witcher.
        If you could release her from witcher then you will be the Prince of her kingdom.
        Let's start the journey from the castle...
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy killed {} soldiers. You have {} soldiers remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyPath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of your journey. Keep going.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class WitchArmyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.WitchArmy())
 
    def intro_text(self):
        return """
        You just entered to the second level of your journey. Keep going.

        ******LEVEL 2*****

        """

        if self.enemy.is_alive():
            return """
            The WitchArmy is about to attack you!
            """
        else:
            return """
            Its your victory, the Witch Army failed...!!!
            """


class NithralRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Nithral())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             Nithral is standing in attacking position!
             """
        else:
            return """
             The corpse of dead Nithral is on the ground.
             """

class SnakeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Snake())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             Snake in front of you!
             """
        else:
            return """
             The corpse of a dead Snake is on the ground.
             """

class BerserkerRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Berserker())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Berserker jumps down in front of you!
             """
        else:
            return """
             The corpse of dead Berserker is on the ground.
             """

class WitcherRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Witcher())

    def intro_text(self):
        return """
        You just entered to the third level of your journey. Be ready to fight with Witcher.

        ******LEVEL 3*****
        
        """
        
        if self.enemy.is_alive():
            return """
             Finally, the Witcher is in front of you!
             """
        else:
            return """
             You killed Witcher..!!!!.
             """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """
class LeaveCastleRoom(MapTile):
    def intro_text(self):
        return """
        You see a tower with bright light in the distance...
        .Now you are entering to the final level

        ****LEVEL 3****

        """
        world.load_tiles('map2.txt')
        player.inventory = [items.Harpoon(), items.Spear(),items.SpearGun(),items.Rod()]
        player.victory = False

class MonsterRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Monster())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A monster is there!
             """
        else:
            return """
             The corpse of dead monster is on the ground.
             """

class BearRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bear())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Bear jumps down in front of you!
             """
        else:
            return """
             The corpse of dead Bear is on the ground.
             """

class GuardRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Guard())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             The guards are witing in front of the tower!
             """
        else:
            return """
             You killed guards, so you are about see her.
             """

class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             The Wolf is in front of you!
             """
        else:
            return """
             You killed Wolf.
             """


class TowerRoom(MapTile):
    def intro_text(self):
        return """
        You see a tower with bright light in the distance...
        ... it grows as you get closer! Yes you found Arya Stark!
 
 
        You will be the Prince!
        """
 
    def modify_player(self, player):
        player.victory = True