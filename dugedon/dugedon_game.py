import os
import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for monster
# draw player in grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/los
# clear screen and redraw grid

CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
	 (0,1),(1,1),(2,1),(3,1),(4,1),
 	 (0,2),(1,2),(2,2),(3,2),(4,2),
	 (0,3),(1,3),(2,3),(3,3),(4,3),
 	 (0,4),(1,4),(2,4),(3,4),(4,4)]


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
	
	
def get_locations():
    return random.sample(CELLS, 3)


def move_player(player,move):
    x,y=player
    if move=="LEFT":
        x-=1
    if move=="RIGHT":
        x-=1
    if move=="UP":
        y-=1
    if move=="DOWN":
        y+=1
    return x,y
    # get the player's location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y-1
    # if move == DOWN, y+1



def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]
    x, y = player
    if x==0:
            moves.remove("LEFT")
    if x==4:
            moves.remove("RIGHT")
    if y==0:
            moves.remove("UP")
    if y==4:
            moves.remove("DOWN")
    # if player's y==0, they can't move up
    # if player's y==4, they can't move down
    # if player's x==0, they can't move left
    # if player's x==4, they can't moze tight
    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x,y=cell
        if x<4:
            line_end=""
            if cell==player:
                output=tile.format("X")
            else:
                output=tile.format("_")
        else:
            line_end="\n"
            if cell==player:
                output=tile.format("X|")
            else:
                output=tile.format("_|")
        print(output,end=line_end)
                        

def game_loop():
    monster,door,player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves=get_moves(player)
        print("You're currently in room {}".format(player)) # fill with player position
        print("You can move {}".format(". ".join(get_moves(player)))) # fill with avaliable moves
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move == "QUIT":
            print("\n ** See you next time! **\n")
                break
        if move in valid_moves:
            player = move_player(player, move)

            if player==monster:
                print("\n ** Oh no monster got You!")
                paying = False
            if player == door:
                print("\n ** You escaped! Congratiulations!")
                paying = False
        else:
            input("\n ** Walls are hard! Don't run into hem! **\n")
    else:
        if input("Play aain? [Y/n] ").lower() != "n":
            game_loop()
        
        # Good move? Change the player position
        # Bad move? Don't change anything!
        # On the door? They win!
        # On the monster? They lose!
        # Otherwise, loop back around
	



clear_screen
print("Welcome to the dugedon!")
input("Press return to start!")
clear_screen()
game_loop()

