import copy, random


def play_mastermind(colours, positions):
    print(f'Playing Mastermind with {colours} colours and {positions} positions')
    colours_choice = [str(i) for i in range(1, colours+1)]
    answer = random.sample(colours_choice, positions)
    attempt = 0
    for i in range(10):
        attempt += 1
        while True:
            player_ans = list(str(input('What is your guess? ')))
            if len(player_ans) == positions:
                break
            print(f'please input exactly {positions} positions.')
        correct_pos = 0
        correct_col = 0
        for num in player_ans:
            num_list = []
            if num in answer and player_ans.index(num) == answer.index(num):
                correct_pos += 1
            elif num in answer and num not in num_list:
                num_list.append(num)
                correct_col += 1
        a = ''
        for m in answer:
            a += m
        print('Your anwer is',a)
        print('*'*correct_pos + 'o'*correct_col)
        print()
        if player_ans == answer:
            print('Congrats! You win.')
            print(f'You solve it after {attempt} rounds.')
            return True

    for i in answer:
        print(i, end='')
    print('Better luck next time.')
    return False







play_mastermind(8, 4)
