import copy, random


# def play_mastermind(colours, positions):
#     print(f'Playing Mastermind with {colours} colours and {positions} positions')
#     colours_choice = [str(i) for i in range(1, colours+1)]
#     answer = random.sample(colours_choice, positions)
#     print(answer)
#     attempt = 0
#     for i in range(10):
#         attempt += 1
#         while True:
#             player_ans = list(str(input('What is your guess? ')))
#             if len(player_ans) == positions:
#                 break
#             print(f'please input exactly {positions} positions.')
#         correct_pos = 0
#         correct_col = 0
#         for num in player_ans:
#             num_list = []
#             if num in answer and player_ans.index(num) == answer.index(num):
#                 correct_pos += 1
#             if num in answer:
#                 print(num_list)
#                 if num not in num_list:
#                     num_list.append(num)
#             for i in range(len(num_list)):
#                 correct_col += 1
#         a = ''
#         for m in player_ans:
#             a += m
#         print('Your answer is',a)
#         print('*'*correct_pos + 'o'*correct_col)
#         print()
#         if player_ans == answer:
#             print('Congrats! You win.')
#             print(f'You solve it after {attempt} rounds.')
#             return True
#
#     for i in answer:
#         print(i, end='')
#     print('Better luck next time.')
#     return False







# play_mastermind(8, 4)


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


game1 = Mastermind()
print(game1.positions)
print(game1.positions)
print(game1.code)
game1.gen_code()
print('ans',game1.code)
print(game1.correct_positions(game1.code))
# print(game1.count_colours_min('5'))
# print(game1.count_colours_min('1'))
game2 = Mastermind()
game2.gen_code_duplicate()
print('code',game2.code)
print(game2.correct_positions(game1.code))
print(game2.correct_colours(game1.code))
