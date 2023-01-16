###########################################################
    #  Computer Project #10
    #  Klondike Card Project
    #  If input Q ends the program
    #  If input H then it displays the menu
    #  If input R then it restarts the game initializing the board
    #  If input SW then it moves card from waste to a specific destination
    #  If input WT then it moves it moves card from waste to tableau
    #  If input WF then it moves card from waste to foundation 
    #  If input TT then moves card from column in tableau to another column
    #  If input TF then it moves card from tableau to the foundation
###########################################################

 
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
    
def initialize():
    """
    This function takes no parameters and returns
    the starting state of the game
    """
    d = Deck()
    #creates the deck
    d.shuffle()
    #shiffles the deck
    waste = []
    foundation = [[], [], [], []]
    tableau = [[], [], [], [], [], [], []]
    #makes the lists for waste, foundation and tableau
    for i in range(7):
        for x in range(i, 7):
            tableau[x].append(d.deal())
        #iterates through the 7 columns and appends 
        #each iteration while dealing it 
    for k in tableau:
        for j in k:
            j.flip_card()
    #flips each card in the tableau
    for u in tableau:
        u[-1].flip_card()
        #flips the last card in the tableau
    
        
    stock = d
    waste.append(stock.deal())
    #stock equal the leftover deck and its dealed

    return tableau, stock, foundation, waste



def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    """
    This function takes two paramters and returns
    the stock and returns the waste with the top card
    of the stock put in the waste
    """
    if stock.is_empty():
        return False
        #if its empty then returns False
    else:
        waste.append(stock.deal())
        return True
        #otherswise it returns True if not empty
        



def waste_to_tableau( waste, tableau, t_num ):
    """
    This function takes three paramters and returns
    the tableau with the top card of the waste put in 
    the tableau
    """
    if len(waste) > 0:
        #if length greater than 0
        y = waste[-1]
        #gets laste card of waste
        if len(tableau[t_num]) == 0:
            #if indexed tablueau equal to 0
            if y.rank() == 13:
                #if rank equal ace then it appends it by popping and returns true
                tableau[t_num].append(waste.pop())
                return True
            return False
            #else returns false
        x = tableau[t_num][-1]
        if ((x.suit() == 1 or x.suit() == 4) and (y.suit() == 2 or y.suit() == 3)) \
         or ((x.suit() == 2 or x.suit() == 3) and (y.suit() == 1 or y.suit() == 4)):
            if x.rank() - y.rank() == 1:
                #if ranks subratracted equals 1 then it appends by popping last card 
                tableau[t_num].append(waste.pop())
                return True
    return False



def waste_to_foundation( waste, foundation, f_num ):
    """
    This function takes three parameters and returns 
    the foundation with the top card of the waste put 
    into the foundation
    """
    if len(waste) > 0:
        #if length of waste greater than 0
        y = waste[-1]
        if len(foundation[f_num]) == 0:
            #if length of foundation indexed equals 0
            if y.rank() == 1:
               foundation[f_num].append(waste.pop())
               #it appends it by popping the last card of the waste
               return True
            return False
        x = foundation[f_num][-1]
        #it indexes last card of foudnation column
        if x.suit() == y.suit():
            if (y.rank() - x.rank()) == 1:
                #if suits equals together and subtracted equals 1
                foundation[f_num].append(waste.pop())
                #then appends it the last card of waste

                return True
    return False





def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    """
    This function takes four parameters and returns
    the foundation with the last card from the tableau
    in the given row into the foundation
    """
    #helped by TA at helproom
    if len(tableau) > 0:
        #if length of tableau grater than 0
        f = tableau[t_num][-1]
        if len(foundation[f_num]) == 0:
            #if indexed foudnation equals 0
            if f.rank() == 1:
                #if ranks equals 1 then appends last card of waste
                foundation[f_num].append(tableau[t_num].pop())
                if len(tableau[t_num]) != 0:
                    #if doesnt equal 0 then flips last card 
                    tableau[t_num][-1].flip_card()
                return True
            return False
        if len(foundation[f_num]) != 0:
            #if length of indexed foundation doesnt equal 0
            z = foundation[f_num][-1] 
            l = tableau[t_num][-1]
            #varaibles with last card of indexed foundation and tableau
            if l.suit() == z.suit():
                #if suits are the same
                if l.rank() - z.rank() == 1:
                    #if subtracted equals 1
                    foundation[f_num].append(tableau[t_num].pop())
                    #appends the tableau popping last card
                    if len(tableau[t_num]) != 0:
                        #if not equal to 0 then it sets the index
                        fixer = tableau[t_num]
                        if len(fixer) > 0:
                            #if greater than 0 then it flips the card
                            fixer[-1].flip_card
                            tableau[t_num] = fixer
                    return True
    return False




def tableau_to_tableau( tableau, t_num1, t_num2 ):
    """
    This function takes three parameters and returns
    tha tableau with the card from one row of the tableau
    moved into another column of the tableau
    """
    #helped by TA at helproom
    if len(tableau) > 0:
        #if length greater than 0
        f = tableau[t_num1][-1]
        if len(tableau[t_num2] ) == 0:
            #if length equals 0
            if f.rank() == 13:
                #if rank equals ace
                tableau[t_num2].append(tableau[t_num1].pop())
                #appends the indexed tableau popping last card
                if len(tableau[t_num1]) != 0:
                    tableau[t_num1][-1].flip_card()
                    #if not equal to 0 then it flips the card
                return True
            else:
                return False
        else:
            if f.suit() == 2 or f.suit() == 3:
                #if suit equals 2 or 3
                if tableau[t_num2][-1].suit() == 1 or tableau[t_num2][-1].suit() == 4:
                    #if the indexed suit equal 1 or 4 then it finds the rank
                    if tableau[t_num2][-1].rank() - 1 == f.rank():
                        tableau[t_num2].append(tableau[t_num1].pop())
                        #and appends the indexed tableaua popping the last card
                        if len(tableau[t_num1]) != 0:
                            #if length of the tableau not equals 0
                            tableau[t_num1][-1].flip_card()
                            #then it flips the last card of the tableau
                        return True
                    else:
                        return False
                        #if not returns false
                else:
                    return False
                    #if not returns false
            else:
                if tableau[t_num2][-1].suit() == 2 or tableau[t_num2][-1].suit() == 3:
                    #if indexed suit equsl 2 or 3 then itu finds the rank
                    if tableau[t_num2][-1].rank() - 1 == f.rank():
                        tableau[t_num2].append(tableau[t_num1].pop())
                        #appends the indexed tableau popping the last card
                        if len(tableau[t_num1]) != 0:
                            #if not equal to 0 then ti flips the last card
                            tableau[t_num1][-1].flip_card()
                        return True
                    else:
                        return False
                        #else it returns False
                else:
                    return False




    
def check_win (stock, waste, foundation, tableau):
    """
    This function takes in fours parameters 
    and returns True if the game is in a winning state or 
    false if the game is not in a winning state
    """
    #if waste is empty and len of tableau equals from 0 - 6 and stock is empty
    #and the length of foundation is from 0 - 3 it returns True
    if waste == [] and len(tableau[0]) == 0 and len(tableau[1]) == 0 and \
    len(tableau[2]) == 0 and len(tableau[3]) == 0 and len(tableau[4]) == 0 and \
    len(tableau[5]) == 0 and len(tableau[6]) == 0 and stock.is_empty() \
     and len(foundation[0]) == 13 and len(foundation[1]) == 13 and \
     len(foundation[2]) == 13 and len(foundation[3]) == 13:
        return True
    return False
    #else it returns False
    
        


def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    """
    This function allows the user to interact
    with the program to input certain specifications
    and to get the intended output
    """
    #helped by TA at helproom
    tableau, stock, foundation, waste = initialize()
    #initlizaises the function witgh fours variables
    print(MENU)
    #prints the menu
    while True:
        display(tableau, stock, foundation, waste)
        #displays the function
        in_str = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        #input statement to input an option
        y = parse_option(in_str)
        #checks validity of input with parse option
        if y == None:
            #if parse option equals none then it passes
            pass
        elif y[0] == "R":
            #if input R then it initializes the board
            tableau, stock, foundation, waste = initialize()
        elif y[0] == "H":
            #if input H then ti prints menu
            print(MENU)
        elif y[0] == "Q":
            #in input Q it ends the program
            break
        elif y[0] == "SW":
            #if input SW then it calls stock to waste and continues 
            #if it true else invalid move
            r = stock_to_waste(stock, waste)
            if r == True:
                continue
            else:
                print("\nInvalid move!\n")
        elif y[0] == "WT":
            #if input WT then it calls waste to tableau and says invalid
            #move if false or continues if true
            t_num4 = y[1] - 1
            #changes range form 1-7 to 0-6
            z = waste_to_tableau(waste, tableau, t_num4)
            if z == False:
                #if z is false invalid move or true then continues
                print("\nInvalid move!\n")
            else:
                continue
        elif y[0] == "WF":
            #if input WF then it calls chekc win and waste to foudnation
            t_num8 = y[1] - 1
            t = waste_to_foundation(waste, foundation, t_num8)
            win = check_win(stock, waste, foundation, tableau)
            if win == True:
                #if game in winning stte then true and break if false then continue
                print("You won!")
                break
            else:
                continue
        elif y[0] == "TT":
            #if input TT then it calls tableau to tableau
            t_num1 = y[1] - 1
            t_num2 = y[2]-1
            f = tableau_to_tableau(tableau, t_num1, t_num2)
            if f == True:
                #if true then contineus with function
                continue
            elif f == False:
                #if false then it prints invalid move
                print("\nInvalid move!\n")
        elif y[0] == "TF":
            #if input TF then it calls tableau to foundation function
            t_num = y[1]-1
            f_num = y[2]-1
            r = tableau_to_foundation( tableau, foundation, t_num, f_num )
            if r == True:
                #if true then it prints you won and breaks
                win = check_win(stock, waste, foundation, tableau)
                #checks if game is in winning state
                if win == True:
                    print("You won!")
                    break
                else:
                    #if false then continues
                    continue
            else:
                #if not true it prints invalid move
                print("\nInvalid move!\n")
    





















if __name__ == '__main__':
     main()
