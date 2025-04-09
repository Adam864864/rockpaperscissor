import random



options = ('rock' , 'paper' , 'scissor')
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock , paper , scissors): ')

    print(f'Player: {player}')
    print(f'Computer: {computer}')


    if player == computer :
        print('tie')
    elif player == 'rock' and computer == 'scissor' :
        print('you win')
    elif player == 'paper' and computer == 'rock' :
        print('you win')
    elif player == 'scissor' and computer == 'paper':
        print('win')
    else:
        print('loser')


