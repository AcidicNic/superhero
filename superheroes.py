from random import randint, shuffle
from statistics import mean


# my helper fxns :)
def int_input(question):
    while True:
        int_input = input(question + ": ")
        if int_input.isdigit() and int(int_input) > 0:
            return int(int_input)
        else:
            print("")

def str_input(question):
    while True:
        str_input = input(question + ": ")
        if len(str_input) > 0:
            return str_input
        else:
            print("")

def char_input(question, options):
    while True:
        char_input = input(question + ": ")
        if char_input.lower() in options:
            return char_input
        else:
            print("")

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

ABILITIES = [Weapon("rock", 20), Ability("fire", 80)]
ARMORS = [Armor("leather", 10), Armor("iron", 40)]

class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = int(starting_health)
        self.current_health = int(starting_health)
        # self.abilities = []
        # self.armors = []
        self.abilities = ABILITIES
        self.armors = ARMORS
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
        if int(self.current_health) > 0:
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
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

            # TODO: returns
            if opponent.abilities == [] and self.abilities == []:
                print("It's a draw!")
                return 0

            elif not opponent.is_alive():
                print(f"{self.name} wins!")
                self.add_kills(1)
                return

            elif not self.is_alive():
                print(f"{opponent.name} wins!")
                opponent.add_deaths(1)
                return


    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        self.armors.append(armor)


class Team():
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heros = []

    def add_hero(self, hero):
        ''' Adds hero to the team.
        '''
        if hero not in self.heros:
            self.heros.append(hero)
        else:
            try:
                print(f"{hero.name} is already in this team!")
            except:
                print("Invalid hero.")

    def remove_hero(self, hero):
        ''' Removes hero from the team.
        '''
        if hero in self.heros:
            for hero in self.heros:
                self.heros.remove(hero.name)
        else:
            return 0
            # try:
            #     print(f"{hero.name} isn't in this team.")
            # except:
            #     print("Invalid hero.")

    def view_all_heroes(self):
        ''' Prints the name of each hero on the team.
        '''
        print("Heros: " + ", ".join(self.heros))
        for hero in self.heros:
            print(hero.name)

    def is_alive(self):
        ''' Returns True if any hero in the team is still alive.
        '''
        for hero in self.heros:
            if hero.is_alive:
                return True
        return False

    def survivors(self):
        survivors = []
        for hero in self.heros:
            if hero.is_alive:
                survivors.append(hero.name)
        return survivors


    def attack(self, other_team):
        ''' Battle each team against each other.'''
        shuffle(self.heros)
        shuffle(other_team.heros)
        for hero in self.heros:
            for opponent in other_team.heros:
                hero.fight(opponent)
        if self.is_alive() and not opponent.is_alive():
            return self
        elif not self.is_alive() and opponent.is_alive():
            return other_team
        else:
            return "DRAW"

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heros:
            try:
                hero.current_health = hero.starting_health
            except:
                hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        kd_list = []
        for hero in self.heros:
            if hero.deaths > 1:
                kd_list.append(hero.kills / hero.deaths)
            else:
                kd_list.append(0)
        return mean(kd_list)


class Arena():
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
        self.prev_winner = None
        self.prev_loser = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability_name = str_input("Ability name: ")
        ability_strength = int_input("Attack Strength: ")
        return Ability(ability_name, ability_strength)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon_name = str_input("Weapon name: ")
        weapon_strength = int_input("Attack Strength: ")
        return Weapon(weapon_name, weapon_strength)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armor_name = str_input("Armor name: ")
        armor_strength = int_input("Block Strength: ")
        return Armor(armor_name, armor_strength)

    def create_hero(self):
        ''' Prompt user for Hero information
            return Hero with values from user input.
        '''
        hero_name = str_input("Hero Name")
        hero_health = int_input("Hero Health")
        return Hero(hero_name, hero_health)

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = str_input("What's your team name?")
        team_len = int_input(f"How many heros will {team_name} need?")
        self.team_one = Team(team_name)

        for i in range(int(team_len)):
            self.team_one.add_hero(self.create_hero())


    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = str_input("What's your team name?")
        team_len = int_input(f"How many heros will {team_name} need?")
        self.team_two = Team(team_name)

        for i in range(int(team_len)):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.prev_winner = self.team_one.attack(self.team_two)
        if not self.prev_winner == 'DRAW':
            if self.prev_winner == self.team_one:
                self.prev_loser = self.team_two
            else:
                self.prev_loser = self.team_one


    def show_stats(self):
        '''Prints team statistics to terminal.'''
        if self.prev_winner == "DRAW":
            print(f"{self.team_one} and {self.team_two} tied!")
        else:
            print(f"Team {self.prev_winner.name} wins!! Try harder next time, {self.prev_loser.name}...\n")
            print(f"Team {self.prev_winner.name} \n\tK/D: {self.prev_winner.stats()}")
            print(f"\tSurviving Heros: {self.prev_winner.survivors().join(", ")}")
            print(f"Team {self.prev_loser.name} \n\tK/D: {self.prev_loser.stats()}")
            print(f"\tSurviving Heros: {self.prev_loser.survivors().join(", ")}")


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = char_input("Play Again? Y or N", ['y', 'n'])

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False
        if play_again.lower() == "y":
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()




# TODO: add armor and abilities to heros manually??
# TODO: show statssssss
