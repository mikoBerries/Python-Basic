# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2]

    

def gameon_choice():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y','N']:
            
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False

def display_game(game_list):
    print("Here is the current list")
    print(game_list)

def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at the position")
    
    game_list[position] = user_placement
    
    return game_list

def position_choice():
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['0','1','2']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace (0,1,2): ")
        
        if choice not in ['0','1','2']:
            
            print("Sorry, but you did not choose a valid position (0,1,2)")

    
    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)

def display_game(game_list):
    print("Here is the current list")
    print(game_list)



while game_on:
    

    display_game(game_list)
    
    # Have player choose position
    position = position_choice()
    
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list,position)

    display_game(game_list)
    
    # Ask if you want to keep playing
    game_on = gameon_choice()