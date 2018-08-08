TITLE = 'Cmpt103S17_Milestone3_GO.py 2017/6/12 Oleksandra Guzovska'
'''-----------------------------------------------------------------------------
Purpose: 
     - Draw the board for the IceBreaker game consisting of 40x40 pixel squares 
     - Draw two players each on the opposite sides of the board
     - Each player is able to move to any legal square
     - Any legal square of ice turns blue when clicked
     - The game terminates if the "Quit Game" button is clicked
     - The game restarts if the "Restart Game" button is clicked
     - The first player to not be able to move loses the game
-----------------------------------------------------------------------------'''
print (TITLE)

from graphics import *
import random
from time import sleep

SQ_LEFT, SQ_TOP = 0, 0                 #start positions: square left, square top 
SQ_VRT, SQ_HRZ, SQ_SZ = 7, 10, 40      #vertical, horizontal and square size

ICE_COLORS = ['white', color_rgb(0, 176, 240)]  # window ice/broken ice color
PLAYER_COLORS = ['red', 'yellow']

player_list = []
square_list = []  # broken/unbroken ice squares
win, pt, move, ice = None,None,None,None  #main screen; mouse click; while loops 
game_message = Text(Point(200, 300), "")  #messages during the game

#below: list containing all the legal moves for each player at the beginning
#of the game
COMBOS = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
          [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
          [[0, 3], [9, 3]]]

#Part I: splash screen, main screen, board, players, menu buttons            
'''-----------------------------------------------------------------------------
Purpose: Draw a splash screen 
Syntax: splash screen()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def splash_screen_1():
    for i in range (0,160, 10):
        intro_rec_1 = Rectangle(Point(0, 0), Point(i, 360))
        intro_rec_1.setFill(color_rgb(197, 251, 255))
        intro_rec_1.setOutline(color_rgb(197, 251, 255)) 
        intro_rec_1.draw(win)
        
        intro_pol_1 = Polygon (Point(i,0), Point (i+100, 100), Point (i, 200))
        intro_pol_1.setFill(color_rgb(197, 251, 255))
        intro_pol_1.setOutline(None)
        intro_pol_1.draw(win)
        
        intro_pol_2 = Polygon (Point(i,200), Point (i+100, 280), Point (i, 360))
        intro_pol_2.setFill(color_rgb(197, 251, 255))
        intro_pol_2.setOutline(None)
        intro_pol_2.draw(win)      
        
        splash_screen_2 (i)
        sleep(0.05)
    
        intro_rec_1.undraw()
        intro_pol_1.undraw()
        intro_pol_2.undraw()
        
    splash_screen_3()

'''-----------------------------------------------------------------------------
Purpose: Draw rectangles and triangles; used by splash_screen_1() 
Syntax: splash screen_2()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def splash_screen_2(i):
    global win 
    intro_rec_2 = Rectangle(Point(400, 360), Point(400 - i , 0))
    intro_rec_2.setFill(color_rgb(197, 251, 255))
    intro_rec_2.setOutline(color_rgb(197, 251, 255))
    intro_rec_2.draw(win)
    
    intro_pol_3 = Polygon (Point(400-i-100,0), Point (400-i, 0),\
                           Point (400-i, 100))
    intro_pol_3.setFill(color_rgb(197, 251, 255))
    intro_pol_3.setOutline(None)
    intro_pol_3.draw(win)
    
    intro_pol_4 = Polygon (Point(400-i,100), Point (400-i-100, 200),\
                           Point (400-i, 280))
    intro_pol_4.setFill(color_rgb(197, 251, 255))
    intro_pol_4.setOutline(None)
    intro_pol_4.draw(win)  
    
    intro_pol_5 = Polygon (Point(400-i,280), Point (400-i-100, 360),\
                           Point (400-i, 360))
    intro_pol_5.setFill(color_rgb(197, 251, 255))
    intro_pol_5.setOutline(None)
    intro_pol_5.draw(win)     

'''-----------------------------------------------------------------------------
Purpose: Display the game's title, used by splash_screen_1()
Syntax: splash screen_3()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def splash_screen_3():
    global win
    try:
        screen = 'screen.gif'
        image_screen = Image(Point(200,180), screen)
        image_screen.draw(win)
    except:
        pass
        
    text = Text (Point(200,180), "IceBreaker")
    text.setSize(36)
    text.setFace('courier')
    text.setTextColor('black')
    text.setStyle('bold italic')
    text.draw(win)
    
    sleep (1.5)
    try:
        image_screen.undraw()
    except:
        pass
    text.undraw()
    
'''-----------------------------------------------------------------------------
Purpose: Draw main menu: Play Game and Quit Game Buttons, game rules, signature
Syntax: splash_screen_2()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def main_menu():
    global win
    
    for i in range (30, 71, 40):
        button = Rectangle (Point (10, i), Point (150, i+30))
        button.setFill(color_rgb(252, 255, 229))
        button.draw(win)
        
    play_text = Text(Point (80, 45), "Play Game")
    play_text.setStyle('bold')
    play_text.setSize(10)
    play_text.draw(win)
    
    quit_text = Text(Point (80, 85), "Quit Game")
    quit_text.setStyle('bold')
    quit_text.setSize(10)
    quit_text.draw(win)    
    
    main_menu_2()
    
'''-----------------------------------------------------------------------------
Purpose: Draw game rules, signature. Used by main_menu()
Syntax: splash_screen_2()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def main_menu_2():
    global win
    
    line = Line(Point(0, 300), Point (400,300))
    line.setFill('black')
    line.draw(win)
     
    try:
        rules = 'rules.png'
        image_rules = Image(Point(200,200), rules)
        image_rules.draw(win)
    except:
        pass  
    
    signature_1 = Text(Point(90, 320), "Name: Oleksandra Guzovska")
    signature_1.setSize(10)
    signature_1.draw(win)
    signature_2 = Text(Point(80,340), " Project: IceBreaker Game")
    signature_2.setSize(10)
    signature_2.draw(win)     
    
'''-----------------------------------------------------------------------------
Purpose: Draw a "Quit Game" button
Syntax: quit_button()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def quit_button():
    global win

    quit = Rectangle(Point(200, 320), Point(400, 360))
    quit.setFill(color_rgb(53, 129, 253))
    quit.setOutline('black')
    quit.draw(win)

    quit_message = Text(Point(300, 340), 'Quit Game')
    quit_message.setTextColor('white')
    quit_message.setStyle('bold')
    quit_message.draw(win)

'''-----------------------------------------------------------------------------
Purpose: Draw one white square at x,y position with the size 40x40 pixels. 
Append object's coordinates and color to a list. 
Syntax: one_square(x, y)
Parameters: 
	x: x coordinate of top-left corner of the square
	y: y coordinate of top-left corner of the square
Return value: None
-----------------------------------------------------------------------------'''
def draw_window(x, y):
    global square_list

    left = SQ_LEFT + x * SQ_SZ
    top = SQ_TOP + y * SQ_SZ
    square = Rectangle(Point(left, top), Point(left + SQ_SZ, top
                       + SQ_SZ))

    square_list[x][y].append(square)  # Rectangle at [x][y][0]
    square_list[x][y].append(ICE_COLORS[0])
    square_list[x][y][0].setFill(ICE_COLORS[0])
    square_list[x][y][0].setOutline('gray')
    square_list[x][y][0].draw(win)

'''-----------------------------------------------------------------------------
Purpose: Draw all the squares to complete the board
Syntax: all_squares ()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def draw_windows():
    global square_list

    for i in range(SQ_HRZ):
        square_list.append([])  # list for column of squares
        for j in range(SQ_VRT):
            square_list[i].append([])
            draw_window(i, j)
            
'''-----------------------------------------------------------------------------
Purpose: Draw 2 players and place them on the opposite sides of the board
Syntax: players()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def draw_players():
    global win, player1, player2, player_list

    player1 = Circle(Point(20, 140), 10)
    player1.setFill(PLAYER_COLORS[0])
    player1.draw(win)

    player2 = Circle(Point(380, 140), 10)
    player2.setFill(PLAYER_COLORS[1])
    player2.draw(win)

    player_list = [player1, player2]

'''-----------------------------------------------------------------------------
Purpose: Draw the board including players, quit and restart buttons, and message
box
Syntax: draw_board()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def draw_board():
    
    quit_button()
    restart_button()
    draw_windows()
    draw_players()
    message_box()

'''-----------------------------------------------------------------------------
Purpose: Draw "Restart Game" button.
Syntax: restart_button()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def restart_button():
    global win

    restart = Rectangle(Point(0, 320), Point(200, 360))
    restart.setFill(color_rgb(53, 129, 253)) 
    restart.draw(win)

    restart_message = Text(Point(100, 340), 'Restart Game')
    restart_message.setTextColor('white')
    restart_message.setStyle('bold')
    restart_message.draw(win)

'''-----------------------------------------------------------------------------
Purpose: Draw a message box to display messages about the game
Syntax: message_box()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def message_box():
    global win
    
    message = Rectangle(Point(0, 280), Point(400, 320))
    message.setFill(color_rgb(213, 229, 255)) 
    message.draw(win)    
 
'''-----------------------------------------------------------------------------
Purpose: Display messages such as whose move it is, which kind of move should 
be made (move piece or break ice)
Syntax: display_message()
Parameters: None
Return value: None
-----------------------------------------------------------------------------''' 
def display_message(text):
    global win, game_message
    
    game_message.undraw()
    game_message = Text(Point(200, 300), text)
    game_message.setTextColor('black')
    game_message.setStyle('bold')
    game_message.draw(win) 

#Part II: move player pieces, break ice, determine the winner        
'''-----------------------------------------------------------------------------
Purpose: Determine a random player to start the game
Syntax: first_player()
Parameters: None
Return value: player to start the game
-----------------------------------------------------------------------------'''
def first_player():
    player = random.randint(0, 1)

    if player == 0:
        for i in range(7):
            player1.setFill('black')
            sleep(0.10)
            player1.setFill(PLAYER_COLORS[0])
            sleep(0.10)
        display_message ("Red, make the first move! Move your piece")
    else:
        for i in range(7):
            player2.setFill('black')
            sleep(0.10)
            player2.setFill(PLAYER_COLORS[1])
            sleep(0.10)
        display_message ("Yellow, make the first move! Move your piece")
    
    return player

'''-----------------------------------------------------------------------------
Purpose: Convert mouse(x,y) coordinates to grid coordinates. Append to a list 
mouse coordinates, p1, p2, grid
Syntax: convert_pix_to_grid(pt)
Parameters: pt: mouse click
Return value: alist: list containing coordinates
-----------------------------------------------------------------------------'''
def convert_pix_to_grid(pt):  
    alist = []
    c = int((pt.x - 5) / 40)  # column
    r = int((pt.y - 5) / 40)  # row
    p1, p2 = square_list[c][r][0].getP1(), square_list[c][r][0].getP2()
    alist.append([pt.x, pt.y, p1, p2, [c, r]])
    
    return alist

'''-----------------------------------------------------------------------------
Purpose: Check where the mouse clicked: Restart Game, Quit Game or on the board
Syntax: check_click()
Parameters: None
Return value: True if clicked on the board
-----------------------------------------------------------------------------'''
def check_click():
    global pt
    
    pt = win.getMouse() 
    if pt.x <= 200 and pt.y > 320:
        restart()
    elif pt.x > 200 and pt.y > 320:
        pt = 0
    elif pt.y <= 280:
        return True

'''-----------------------------------------------------------------------------
Purpose: Check if player can move their piece (if that's a legal move). A legal
move is a move to any adjacent white square(up, down, left, right or diagonally)
Syntax: check_player_move()
Parameters: None
Return value: True if the move is legal
-----------------------------------------------------------------------------'''
def check_player_move():
    global win, square_list, player, pt
    
    player = convert_pix_to_grid(pt)
    #check the move is legal
    if square_list[player[0][4][0]][player[0][4][1]][1] \
                    != ICE_COLORS[1] and player[0][4] \
                    in COMBOS[player_turn] and player[0][4] not in COMBOS[2]:                    
        player_move(player, player_turn)
        return True
    
'''-----------------------------------------------------------------------------
Purpose: Make a single move; does not include breaking the ice. 
Syntax: player_move(player, player_turn)
Parameters: player: player's coordinates based on the mouse click
            player_turn: value 0 or 1 depending on whose turn it is to play
Return value: None
-----------------------------------------------------------------------------'''
def player_move(player, player_turn):
    global win, square_list, player_list
    
    player_list[player_turn].undraw()

    #place players (circles) in the middle of the square
    player_list[player_turn] = Circle(Point((player[0][2].x
            + player[0][3].x) / 2, (player[0][2].y + player[0][3].y)/ 2), 10)
    player_list[player_turn].setFill(PLAYER_COLORS[player_turn])
    player_list[player_turn].draw(win)

    update_combos(player, player_turn)

'''-----------------------------------------------------------------------------
Purpose: Calculate the min and max range for legal moves.Used by update_combos()
to calculate the values in between max and min
Syntax: calc_move_range (player)
Parameters: player: player's coordinates based on the mouse click
Return value: move_range
Ex: if the player is at position (grid) (0,0), the min and max for column(c) and 
    row(r) are:
            c - min: 0, max: 1; r - min: 0, max: 1
    if at position (1,3):
            c - min: 0, max: 2; r - min: 2, max: 4
-----------------------------------------------------------------------------'''
def calc_move_range(player):
    i_beg, i_end = int(player[0][4][0]) - 1, int(player[0][4][0]) + 2
    j_beg, j_end = int(player[0][4][1]) - 1, int(player[0][4][1]) + 2

    if int(player[0][4][1]) == 0 and int(player[0][4][0]) == 0:
        i_beg, j_beg = int(player[0][4][0]), int(player[0][4][1])
        
    elif int(player[0][4][0]) == 0 and int(player[0][4][1]) == 6:
        i_beg, j_end = int(player[0][4][0]), int(player[0][4][1]) + 1
                          
    elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 6:
        i_end, j_end = int(player[0][4][0]) + 1, int(player[0][4][1]) + 1
        
    elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 0:
        i_end, j_beg = int(player[0][4][0]) + 1, int(player[0][4][1])
    
    elif int(player[0][4][1]) == 0: j_beg = int(player[0][4][1])
        
    elif int(player[0][4][0]) == 0: i_beg = int(player[0][4][0])
        
    elif int(player[0][4][1]) == 6: j_end = int(player[0][4][1]) + 1
        
    elif int(player[0][4][0]) == 9: i_end = int(player[0][4][0]) + 1

    move_range = (i_beg, i_end, j_beg, j_end)
    return move_range

'''-----------------------------------------------------------------------------
Purpose: Update the COMBOS list with all the legal moves
Syntax: update_combos(player, player_turn)
Parameters: player: player's coordinates based on the mouse click
            player_turn: value 0 or 1 depending on whose turn it is to play
Return value: COMBOS: list with all the legal moves
Ex: if the player is at position (grid) (0,0), the legal moves are:
    [0,0], [0,1], [1,0], [1,1]
    Blue (broken) squares are excluded from the list.
-----------------------------------------------------------------------------'''
def update_combos(player, player_turn):
    global COMBOS, square_list

    COMBOS[player_turn] = []
    COMBOS[2][player_turn] = player[0][4]
    move_range = calc_move_range(player)
    
    for i in range(move_range[0], move_range[1]):
        for j in range(move_range[2], move_range[3]):
             #check if the square beside the player is blue(broken) and another
            #player is on it
            if square_list[i][j][1] != ICE_COLORS[1]:
                COMBOS[player_turn].append([i, j])
    #COMBOS cleanup: remove occupied squares from the list for both players
    if COMBOS[2][player_turn] in COMBOS[player_turn]:
        COMBOS[player_turn].remove(COMBOS[2][player_turn])
    if COMBOS[2][not player_turn] in COMBOS[not player_turn]:
        COMBOS[not player_turn].remove(COMBOS[2][not player_turn]) 
    if COMBOS[2][player_turn] in COMBOS[not player_turn]:
        COMBOS[not player_turn].remove(COMBOS[2][player_turn]) 
    if len (COMBOS[player_turn]) == 1 and COMBOS[2][not player_turn]\
               in COMBOS[player_turn]:
        COMBOS[player_turn].remove(COMBOS[2][not player_turn]) 
    
    return COMBOS

'''-----------------------------------------------------------------------------
Purpose: Check if the square to be broken is still white and there is no player
(if the move is legal). 
Syntax: check_crash_ice()
Parameters: None
Return value: True if the move is legal
-----------------------------------------------------------------------------'''
def check_crash_ice():
    global win, square_list, player_turn, COMBOS, pt
    
    pt2 = pt
    break_ice = convert_pix_to_grid(pt2)                        
                            
    if square_list[break_ice[0][4][0]]\
                        [break_ice[0][4][1]][1]==ICE_COLORS[0] and \
                    COMBOS[2][0] != break_ice[0][4] and COMBOS[2][1]\
                            != break_ice[0][4]:
        crash_ice(break_ice)  
        if break_ice[0][4] in COMBOS[not player_turn]:
            COMBOS[not player_turn].remove(break_ice[0][4])
        player_turn = change_players(player_turn)
        return True
    
'''-----------------------------------------------------------------------------
Purpose: Break the ice; change the color of the square to blue. A square 
cannot be 'broken' twice.
Syntax: crash_ice(break_ice)
Parameters: break_ice: square to be broken based on the mouse click
Return value: None
-----------------------------------------------------------------------------'''
def crash_ice(break_ice):
    global COMBOS, square_list, player, player_turn
    
    square_list[break_ice[0][4][0]][break_ice[0][4][1]][0].setFill\
                                                    (ICE_COLORS[1])
    square_list[break_ice[0][4][0]][break_ice[0][4][1]][1] = ICE_COLORS[1]

    update_combos(player, player_turn)
    
'''-----------------------------------------------------------------------------
Purpose: Determine who plays next
Syntax: change_players(player_turn)
Parameters: player_turn: value 0 or 1, previous player
Return value: player_turn: value 0 or 1, next player
-----------------------------------------------------------------------------'''
def change_players(player_turn):
    
    if player_turn == 0:
        player_turn = 1
        display_message ("Yellow, move your piece")
    else:
        player_turn = 0
        display_message ("Red, move your piece")

    return player_turn

'''-----------------------------------------------------------------------------
Purpose: Restart the game: change the color of squares from blue to white; 
reset COMBOS, undraw players
Syntax: restart()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def restart():
    global square_list, COMBOS, player_turn, pt
    
    display_message ("Restart in progress...")
    
    for x in range (SQ_HRZ):
        for y in range (SQ_VRT):
            if square_list[x][y][1] == ICE_COLORS[1]:
                square_list[x][y][0].setFill(ICE_COLORS[0])
                square_list[x][y][1] = ICE_COLORS[0]
                sleep(0.1)
                
    player_list[0].undraw()
    sleep(0.2)
    player_list[1].undraw()
    sleep(0.2)
    draw_players() 
    
    COMBOS = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
          [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
          [[0, 3], [9, 3]]]

    pt = 1          #exits the while loop if "Restart" is clicked after a 
                    #player moved but before a square was broken
    player_turn = first_player()
    
'''-----------------------------------------------------------------------------
Purpose: Determine a winner: if one player still has available moves in COMBOS 
but the opponent does not. The first player to not be able to move loses the 
game. If after the move neither player has available moves, nobody wins. 
Syntax: winner()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''    
def winner():
    global COMBOS
    
    if len(COMBOS[0]) == 0 and len(COMBOS[1]) == 0:
        display_message ("The game is a draw! Restart or Quit the game")
        COMBOS = []
        return True
    elif len(COMBOS[0]) == 0:
        display_message ("Yellow has won! Restart or Quit the game")
        COMBOS = []
        return True
    elif len(COMBOS[1]) == 0:
        display_message ("Red has won! Restart or Quit the game")
        COMBOS = []
        return True

'''-----------------------------------------------------------------------------
Purpose: Display options if there is a winner: Quit or Restart
Syntax: after_winner()
Parameters: None
Return value: True if 'Quit' is pressed; otherwise False
-----------------------------------------------------------------------------'''    
def after_winner():
    if_winner = winner()
    if if_winner:                   
        
        while True: 
            if_winner_pt = win.getMouse()
            if if_winner_pt.x <= 200 and if_winner_pt.y > 320:
                restart()
                if_winner = False
                break
            elif if_winner_pt.x > 200 and if_winner_pt.y > 320: 
                return True                

'''-----------------------------------------------------------------------------
Purpose: Make a legal move ---> move a piece; check for winner
Syntax: play_game_player()
Parameters: None
Return value: True if "Quit Game" has been pressed
-----------------------------------------------------------------------------'''
def play_game_player():
    global win, pt, move, ice
    
    move = -1
    while move == -1: 
        click_1 = check_click()
        if pt == 0:         #if clicked on "Quit Game"   
            return True
        elif click_1:         #if clicked onthe board
            player_move = check_player_move()  #check the move is legal
            if player_move:
                move, ice = pt, -1
                winner = after_winner()   #if there's a winner
                if winner:                #if clicked on "Quit Game"      
                    return True
                play_game_ice()
            else:
                move = -1

'''-----------------------------------------------------------------------------
Purpose: Make a legal move ---> break a piece of ice; check for winner
Syntax: play_game_ice()
Parameters: None
Return value: True if "Quit Game" has been pressed
-----------------------------------------------------------------------------'''                           
def play_game_ice():
    global win, pt, ice
    
    while ice == -1:
        display_message("Break the ice!")
        click_2 = check_click()    
        if pt == 0:                  #if clicked on "Quit Game"   
            return True
        elif pt == 1:                
            ice = pt            #exits the while loop; properly resets the game
            break
        elif click_2:                #if clicked on the board
            crash = check_crash_ice()
            if crash:           #if the square can be broken
                pt2 = pt                            
                ice = pt2
                winner = after_winner()  #if there's a winner
                if winner:               
                    pt = 0 
            else:
                ice = -1  
                
'''-----------------------------------------------------------------------------
Purpose: Play a single game
Syntax: play_game()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''    
def play_game():
    global win, player_turn, pt 
    
    draw_board()
    player_turn = first_player()
    
    OK = True
    while OK == True: 
        quit = play_game_player()
        if quit or pt == 0:            #if clicked on "Quit Game"
            OK = False
            win.close()                            
            break
                
'''-----------------------------------------------------------------------------
Purpose: The main function of the program; launch the main menu; display the 
rules, signature, options to play and quit.
Syntax: main()
Parameters: None
Return value: None
-----------------------------------------------------------------------------'''
def main():
    global win
    
    win = GraphWin('IceBreaker', 400, 360)
    win.setBackground(color_rgb(0, 176, 240))      
    splash_screen_1()

    main_menu()    
    
    launch = True
    while launch == True:
        do = win.getMouse()
        if 10 < do.x < 150 and 30 < do.y < 60:
            play_game()
            break
        elif 10 < do.x < 150 and 70 < do.y < 100:
            win.close()
            launch = False
            break

#===============================================================================
# TEST CODE
        
if __name__ == '__main__':
    main()

    
