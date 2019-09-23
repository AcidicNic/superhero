from random import randint, shuffle

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return randint(0, self.attack_strength)


class Armor():
    def __init__(self, name, max_block):
        self.max_block = max_block
        self.name = name

    def block(self):
        return randint(0, self.max_block)


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.attack_strength/2, self.attack_strength)


class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.weapons = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        tot_block = 0
        try:
            for armor in self.armors:
                tot_block -= armor.block()
            if tot_block < 0:
                tot_block = 0
        except:
            pass
        return tot_block

    def take_damage(self, damage):
        tot_damage = damage - self.defend()
        if tot_damage > 0:
            self.current_health -= tot_damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        return False

    def add_kills(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def fight(self, opponent):
        while True:
            if opponent.abilities == [] and delf.abilities == []:
                print("It's a draw!")
                break
            opponent.take_damage(opponent.take_damage(self.attack()))
            self.take_damage(self.take_damage(opponent.attack()))

            if not opponent.is_alive():
                print(f"{self.name} wins!")
                self.add_kill(1)
                break

            if not self.is_alive():
                print(f"{opponent.name} wins!")
                opponent.add_deaths(1)
                break


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heros = []

    def add_hero(self, hero):
        if hero not in self.heros:
            self.heros.append(hero)
        else:
            try:
                print(f"{hero.name} is already in this team!")
            except:
                print("Invalid hero.")

    def rm_hero(self, hero):
        if hero in self.heros:
            self.heros.remove(hero)
        else:
            return 0
            # try:
            #     print(f"{hero.name} isn't in this team.")
            # except:
            #     print("Invalid hero.")

    def view_all_heroes(self):
        for hero in self.heros:
            print(hero.name)

    def is_alive(self):
        ''' Returns True if any hero in the team is still alive.
        '''
        for hero in self.heros:
            if hero.is_alive:
                return True
        return False

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        shuffle(self.heros)
        shuffle(other_team.heros)
        for hero in self.heros:
            for opponent in other_team.heros:
                while hero.is_alive() and opponent.is_alive():
                    hero.fight(opponent)
        if self.is_alive():
            print(f"Team {self.name} wins!! Try harder next time, {opponent.name}...")
        else:
            print(f"Team {opponent.name} wins!! Try harder next time, {self.name}...")

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heros:
            try:
                hero.current_health = hero.starting_health
            except:
                hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heros:
            print(f"{hero.name}: {hero.kills / hero.deaths}.{hero.kills % hero.deaths}")
