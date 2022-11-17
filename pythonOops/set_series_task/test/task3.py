class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("\n Class Employee")

    def print_age(self):
        print(f'{self.name}\'s age', self.age)

    def print_details(self):
        print(f'The employee is {self.name} '
              f'whose age is {self.age} .')


class Player():
    def __init__(self, name, game):
        self.name = name
        self.game = game
        print("\n Class Player")

    def print_game(self):
        print(f'Player plays ', self.game)

    def print_details(self):
        print(f'This player\'s name is {self.name}.'
              f'His fav game is {self.game}')


class CoolProgrammer(Employee, Player):
    def __init__(self, name, age, game):
        super().__init__(name, age)
        super().__init__(name, game)

    def display_language(self):
        print('Favorite programming lang: Python')


roni = CoolProgrammer('Dwaipayan', 28, 'Cricket')
roni.print_details()
roni.print_age()
roni.print_game()
