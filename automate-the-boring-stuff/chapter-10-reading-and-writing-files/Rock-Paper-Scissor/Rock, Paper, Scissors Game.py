# Rock, Paper, Scissors with Saved Games

import random, sys, shelve, datetime

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
with shelve.open('rps_stats') as stats:
    wins = stats.get('wins', 0)
    losses = stats.get('losses', 0)
    ties = stats.get('ties', 0)
    game_history = stats.get('history', [])

while True:  # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
             # CHANGED: Save stats before quitting instead of just sys.exit()
            with shelve.open('rps_stats') as stats:
                stats['wins'] = wins
                stats['losses'] = losses
                stats['ties'] = ties
                stats['history'] = game_history
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
    # After determining result, store the game
    if player_move == computer_move:
        result = 'tie'
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        result = 'win'
    else:
        result = 'loss'
    
    game_record = {
        'timestamp': str(datetime.datetime.now()),
        'player': player_move,
        'computer': computer_move,
        'result': result
    }
    game_history.append(game_record)