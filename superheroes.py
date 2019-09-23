from random import randint

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return randint(0, self.attack_strength)


class Armor():
    def __init__(self, max_block):
        self.max_block = max_block

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

    def defend(self, damage):
        try:
            for armor in self.armors:
                damage -= armor.block()
        except:
            pass
        if damage < 0:
            damage = 0
        return damage

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)

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
            opponent.take_damage(opponent.defend(self.attack()))
            self.take_damage(self.defend(opponent.attack()))

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

    # Keep all your current code, but add these methods
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        pass

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass
