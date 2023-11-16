import random


class Mastermind:

    def __init__(self, colours=8, positions=4):
        self.colours = colours
        self.positions = positions
        self.__code = []

    def set_colours(self, colours):
        self.colours = colours

    def set_positions(self, positions):
        self.positions = positions

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    def gen_code(self):
        colours_choice = [str(i) for i in range(1, self.colours + 1)]
        code = random.sample(colours_choice, self.positions)
        self.code = code

    def gen_code_duplicate(self):
        colours_choice = [str(i) for i in range(1, self.colours + 1)]
        colours_choice_duplicate = []
        for i in range(self.positions):
            for col in colours_choice:
                colours_choice_duplicate.append(col)
        code = random.sample(colours_choice_duplicate, self.positions)
        self.code = code

    def correct_positions(self, answer):
        correct_pos = 0
        for num in answer:
            if num in self.code and answer.index(num) == self.code.index(num):
                correct_pos += 1
        return correct_pos

    def count_colours_min(self,answer,col):
        n_col_code = 0
        for i in self.code:
            if col == i:
                n_col_code += 1
        n_col_ans = 0
        for i in answer:
            if col == i:
                n_col_ans += 1
        if n_col_code <= n_col_ans:
            return n_col_code
        return n_col_ans

    def correct_colours(self, answer):
        correct_col = 0
        num_list = []
        for num in self.code:
            if num in answer and answer.index(num) != self.code.index(num) and num not in num_list:
                correct_col += self.count_colours_min(answer, num)
            num_list.append(num)
        return correct_col

    def __str__(self):
        return f'Playing Mastermind with {self.colours} colours and {self.positions} positions'

    def setup(self):
        print('Select difficulty')
        colours = int(input('Input number of colours (1 to 8): '))
        positions = int(input('Input number of positions (1 to 10): '))
        self.set_colours(colours)
        self.set_positions(positions)
        if colours >= positions:
            duplicated = input('Allow duplicated or nah(Enter if nah)? ')
            if duplicated == '':
                self.gen_code()
            else:
                self.gen_code_duplicate()
        else:
            self.gen_code_duplicate()

        reset = input('Reset? (Press r to reset) ')
        if reset in ['r', 'R']:
            print()
            print('===RESET===')
            print()
            self.setup()

    def play(self):
        self.setup()
        print()
        print(self)
        print(self.code)

        attempt = 0
        while True:
            while True:
                attempt += 1
                player_ans = list(str(input('What is your guess? ')))
                if len(player_ans) == self.positions:
                    break
                print(f'please input exactly {self.positions} positions.')

            a = ''
            for m in player_ans:
                a += m
            print('Your guess is', a)

            correct_pos = self.correct_positions(player_ans)
            correct_col = self.correct_colours(player_ans)

            print('*' * correct_pos + 'o' * correct_col)
            print()

            if player_ans == self.code:
                print('Congrats! You win.')
                print(f'You solve it after {attempt} rounds.')
                break


game1 = Mastermind()
game1.play()
