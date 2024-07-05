import os
import random

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_menu():
    while True:
        try:
            print('ROCK PAPER SCISSORS')
            print('')
            print('1) Play')
            print('2) Quit\n')
            user_input = int(input('>: '))
            if user_input == 1:
                break
            elif user_input == 2:
                clrscr()
                print('Quitting...')
                print('Goodbye!')
                exit()
            else: 
                clrscr()
                print('Enter a "1" to Play or "2" to Quit.')
                print('Press enter to continue...')
                input()
                clrscr()
                continue
        except ValueError:
            clrscr()
            print('Enter a "1" to Play or "2" to Quit.')
            print('Press enter to continue...')
            input()
            clrscr()
            continue

def get_user_input():
    while True:
        try:
            clrscr()
            print('Make a choice:')
            print('')
            print('1) ROCK')
            print('2) PAPER')
            print('3) SCISSORS')
            user_choice = int(input('>: '))
            if user_choice == 1:
                return 'ROCK'
            elif user_choice == 2:
                return 'PAPER'
            elif user_choice == 3:
                return 'SCISSORS'
            else:
                clrscr()
                print('Enter a "1" to Play or "2" to Quit.')
                print('Press enter to continue...')
                input()
                clrscr()
                continue
        except:
            clrscr()
            print('Enter "1" for ROCK, "2" for PAPER, and "3" for SCISSORS.')
            print('Press enter to continue...')
            input()
            clrscr()
            continue

def get_cpu_input():
    answer = ['ROCK', 'PAPER', 'SCISSORS']
    return random.choice(answer)

def determine_winner(user_answer, cpu_answer):
    clrscr()
    print(f'User: {user_answer}')
    print(f'CPU: {cpu_answer}\n')
    if user_answer == cpu_answer:
        print('It\'s a tie!')
        print('Press enter to continue...')
    if user_answer == 'ROCK' and cpu_answer == 'PAPER':
        print('You lose! PAPER beats ROCK!')
        print('Press enter to continue...')
    if user_answer == 'ROCK' and cpu_answer == 'SCISSORS':
        print('You win! ROCK beats SCISSORS!')
        print('Press enter to continue...')
    if user_answer == 'PAPER' and cpu_answer == 'ROCK':
        print('You win! PAPER beats ROCK!')
        print('Press enter to continue...')
    if user_answer == 'PAPER' and cpu_answer == 'SCISSORS':
        print('You lose! SCISSORS beats PAPER!')
        print('Press enter to continue...')
    if user_answer == 'SCISSORS' and cpu_answer == 'ROCK':
        print('You lose! ROCK beats SCISSORS')
        print('Press enter to continue...')
    if user_answer == 'SCISSORS' and cpu_answer == 'PAPER':
        print('You win! SCISSORS beats PAPER!')
        print('Press enter to continue...')
    input()

def play_again_input():
    while True:
        try:
            clrscr()
            print('Play again?\n')
            print('1) Yes')
            print('2) No')
            user_response = int(input('>: '))
            return user_response
        except ValueError:
            clrscr()
            print('Enter 1 to continue playing, or 2 to stop.')
            print('Press enter to continue...')
            input()
            clrscr()
            continue

def play_quit(play_answer):
    if play_answer == 1:
        main()
    else:
        clrscr()
        print('Quitting...')
        print('Goodbye!')
        exit()
        
def main():
    clrscr()
    start_menu()
    user_answer = get_user_input()
    cpu_answer = get_cpu_input()
    determine_winner(user_answer, cpu_answer)
    continue_play = play_again_input()
    play_quit(continue_play)

if __name__ == '__main__':
    main()