from Die import dice
import numpy as np
import pandas as pd
from scoresheet import card
import math
#import scoresheet


'''
#Test case, roll one die
test_die =dice()
print(test_die)
print(test_die.roll())
'''
#Checks for yathzee
def Yathzee(hand_df):   
    compare_array = hand_df['Dice'].to_numpy()
    comp = (compare_array[0] == compare_array).all()
    return comp

#Create hand of dice
def hand_of_dice(number_of_dice):
    #number_of_dice = 5
    gen_dice = [dice() for Die in range(number_of_dice)]
    #print(die.roll())
    return gen_dice

#Roll hand of dice
def roll(dice):
    if len(dice)>1:
        values = [die.roll() for die in dice]
    else:
        new_die = dice()
        values = new_die.roll()
    return values

#Function that throws the five dices, mainly the first throw
def throw1(number_of_dice):  
    # Function creates a dataframe in which the value of the five dice are stored. 
    # In order to later keep track of which die to re-roll a True/False column is added to the df.  
    truefalse_column= [True,True,True,True,True]    #All dies are open for re-roll after first throw.
    #print(truefalse_column)
    hand_df = pd.DataFrame({'Re_roll':truefalse_column})    #Create dataframe with the array of trues
    #print(hand_df)
    #Creates five dice
    my_hand = hand_of_dice(number_of_dice)

    #Rolls the dice
    rolling=np.array(roll(my_hand))
    #print(type(rolling))
    hand_df['Dice']=rolling     # Add the thrown dice to the df

    return(hand_df)

# Function that checks if needed input is an integer
def check_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
    return number

# Saves the wanted dice
def dice_to_save(hand):
    numberofdice = check_input("Enter the number of dies you want to save:")
    all_saved = 0   # Variable used to see if all dice are saved or not

    while numberofdice>5:
        print('You only have five dice!')
        numberofdice = check_input("Enter the number of dies you want to save:") #int(input("Enter the number of dies you want to save:"))           

    saved_index_list = []

    if numberofdice <5:
        for i in range(numberofdice):
            print('Choose which dice to sav,e one at a time. Use the index to the left to indicate.')
            saved_dice = check_input('Which dice do you want to save: ') #int(input('Which dice do you want to save, use index to the left to indicate: '))
            while saved_dice>4:
                print('The index goes from 0 to 4!')
                saved_dice = check_input('Which dice do you want to save, use index to the left to indicate: ') #int(input('Which dice do you want to save, use index to the left to indicate: '))

            saved_index_list.append(saved_dice)
    else: 
        saved_index_list = [0,1,2,3,4]  # If all dice are saved, this list is created
        #all_saved = 1

    for i in saved_index_list:
        hand.loc[i,"Re_roll"] = False   # The dice that are saved are set to False in the re-roll column
        #print(hand)

    return (hand)
    
'''
#Old function, not used anymore. Originally this funciton was ment to save dice and calculated points
def saving_hand(hand): #This function looks for what you have thrown and save the index. DOes not work with full house
    #print(hand['Dice'].value_counts())

    #ones = hand.where(hand['Dice']==1)
    #twoes = hand.where(hand['Dice']==2)
    #Threes = hand.where(hand['Dice']==3)
    #foures = hand.where(hand['Dice']==4)
    #fives = hand.where(hand['Dice']==5)
    #sixes = hand.where(hand['Dice']==6)


    #print(".................")
    #print(ones)

    #Gets the index in the df of the different values
    one_index=hand.index[hand['Dice'] == 1].tolist()
    two_index=hand.index[hand['Dice'] == 2].tolist()
    three_index=hand.index[hand['Dice'] == 3].tolist()
    four_index=hand.index[hand['Dice'] == 4].tolist()
    five_index=hand.index[hand['Dice'] == 5].tolist()
    six_index=hand.index[hand['Dice'] == 6].tolist()
    #one_index = hand.columns.tolist().index(1)
    #print(one_index)
    
    counting_values = hand['Dice'].value_counts()
    #print(type(counting_values))
    print("""
        Below you can see the sum of the values of your dies, 
        so you do not have to count the numbers yourself""")
    print("Dice Number of dice")
    print(counting_values)

    print('---------------')
    #saved_dice = int(input(("""
    #What would you like to save, "1", "2", "3", "4", "5", or "6"?
    #      """)))
    saved_dice=100
    counter=0
    while saved_dice>6:
        #print('Remember, you only have five dice!')
        saved_dice = int(input(("""
        What would you like to save, "1", "2", "3", "4", "5", "6" or none ("0")?
          """)))
        counter+=1
        if saved_dice>6:
            print('Remember, the dice can only count to six!')
        #Add something to make certain that a number that exists is picked
    
    if saved_dice==1:
        #Gör foor loop bääää
        hand[one_index[0],"Re_roll"]=False
        
    #elif saved_dice==2:
     #   hand["Re_roll"][two_index]=False


'''

# Re-rolls the dice not saved, the ones set to True in the Re_roll column of the df
def other_throws(hand):

    for i in range(5):
        if hand.loc[i,"Re_roll"]==True: 
            #hand.loc[i,"Dice"]=roll(1)
            new_die = dice()
            hand.loc[i,"Dice"]=new_die.roll()
    #print(hand)

    return(hand)

#def scoring(hand):
    #counting_values = hand['Dice'].value_counts()
    #count = hand.groupby('Dice').size()[1] #Använd detta för att hitta ettor etc...
    #print()

# Controlls one round
def one_round(scorecard):
    all_saved = 0       # Variable used when all dice are saved. If all dice are saved it is set to 1.
    throw = throw1(5)
    print("Your first hand: ")
    print(throw['Dice'])
    #scorecard = card()
    #see_card = input("Would you like to see the scorcard y/n? ")
    #if see_card == "y":
    #    print(scorecard)

    yatzy = Yathzee(throw) #Check for Yathzee
    if yatzy == True:
        if math.isnan(scorecard.loc["Yathzee","Points"]):
            print('YATHZEEEEEEEE!')
            #scorecard.loc["Yathzee","Points"]=50
        else:
            print('Yathzee again?! You do not get more extra points for it.')
    

    #print(dice_to_save(throw))

    first_hand=dice_to_save(throw)
    counting_False1 = first_hand['Re_roll'].value_counts()
    if counting_False1.iloc[0]==5 and first_hand["Re_roll"][0]==False:  #If all are saved other throws canceled
        all_saved = 1
    #print(first_hand)
    if all_saved == 0:
        #print(f_hand)
        print(" ")
        print("Your second hand")
        s_hand= other_throws(first_hand)
        s_hand = s_hand.replace({'Re_roll': {False: True}})
        #print(first_hand)
        #test_throw= roll(1)
        print(s_hand["Dice"])
        #scorecard = card()
        #see_card = input("Would you like to see the scorcard y/n? ")
        #if see_card == "y":
        #    print(scorecard)
        yatzy = Yathzee(s_hand)
        if yatzy == True:
            if math.isnan(scorecard.loc["Yathzee","Points"]):
                print('YATHZEEEEEEEE!')
                #scorecard.loc["Yathzee","Points"]=50
            else:
                print('Yathzee again?! You do not get more extra points for it.')
        second_save = dice_to_save(s_hand)
        #print("second_save",second_save)
    else:
        s_hand = first_hand

    
    counting_False2 = s_hand['Re_roll'].value_counts()  #If all are saved last throw is canceled
    if counting_False2.iloc[0]==5 and s_hand["Re_roll"][0]==False:
        all_saved = 1
    if all_saved == 0:
        print(" ")
        print("Your third and final hand")
        f_hand= other_throws(second_save)
        print(f_hand["Dice"])
        #scorecard = card()
        #see_card = input("Would you like to see the scorcard y/n? ")
        #if see_card == "y":
        #    print(scorecard)
        yatzy = Yathzee(f_hand)
        if yatzy == True:
            if math.isnan(scorecard.loc["Yathzee","Points"]):
                print('YATHZEEEEEEEE!')
                #scorecard.loc["Yathzee","Points"]=50   #Used when 50 points was automatically given
            else:
                print('Yathzee again?! You do not get more points for it.')   
                #calling_score = scoring(scorecard,f_hand)
                #print(calling_score) 
        #else:
        calling_score = scoring(scorecard,f_hand)
        print(calling_score) 
    else:
        f_hand = s_hand
        calling_score = scoring(scorecard,f_hand)
        print(calling_score) 
    
    return f_hand

# 
def scoring (scorecard,hand):
    combinations=['Ones','Twoes','Threes','Foures','Fives','Sixes','Pair','Two pairs','Three of kind','Four of kind','Full house', 'Small straight', 'Large straight', 'Chance','Yathzee']
    print('Here is the scorecard as it is currently: ')
    print(scorecard)
    #print("What would you like to? Save or do you want to remove something?")
    ask_score = input('Where would you like to save the points? ')
    while (ask_score not in combinations) or (math.isnan(scorecard.loc[ask_score,"Points"])==False): #or ask_score not in combinations: 
        #while ask_score not in combinations: 
        ask_score = input('Not a valid input, pick another!')
    point = calculate_score(hand,ask_score)

    scorecard.loc[ask_score,"Points"]=point
    '''
    if ask_score=="remove":
        remove_this = input('What would you like to remove? ')
        while math.isnan(scorecard.loc[remove_this,"Points"])==False:
        #if math.isnan(scorecard.loc[remove_this,"Points"]):
            remove_this = input('You cannot remove that! Pick another: ')
        scorecard.loc[remove_this,"Points"]=0

    else:
        while ask_score not in combinations:
            if ask_score=="remove":
                remove_this = input('What would you like to remove? ')
                scorecard.loc[remove_this,"Points"]=0
            else: ask_score = input("Not available, pick again! ")
        while math.isnan(scorecard.loc[ask_score,"Points"])==False: #This check does not work
            ask_score = input("Not avaiable, pick again! ")
            while ask_score not in combinations:
                ask_score = input('You cannot put it there, pick another: ')
        if math.isnan(scorecard.loc[ask_score,"Points"]):
            print("Calculate points")
            point = 5
            scorecard.loc[ask_score,"Points"]=point
    '''
    return scorecard

# Calculate score based on where to save the diece
def calculate_score(hand,which_save):
    #Calculates the score depending on the dice.
    #['Ones','Twoes','Threes','Foures','Fives','Sixes',
    # 'Pair','Two pairs','Three of kind','Four of kind',
    # 'Full house', 'small straight', 'large straight', 'Chance'
    if which_save == 'Ones':
        if 1 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[1]
            point = count*1
        else:
            point = 0
    elif which_save == 'Twoes':
        if 2 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[2]
            point = count*2
        else:
            point = 0
    elif which_save == 'Threes':
        if 3 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[3]
            point = count*3
        else:
            point = 0
    elif which_save == 'Foures':
        if 4 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[4]
            point = count*4
        else:
            point = 0
    elif which_save == 'Fives':
        if 5 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[5]
            point = count*5
        else:
            point = 0
    elif which_save == 'Sixes':
        if 6 in hand['Dice'].values:
            count = hand.groupby('Dice').size()[6]
            point = count*6
        else:
            point = 0

    elif which_save == 'Pair':
        pair = hand['Dice'].duplicated()
        counting_values = hand['Dice'].value_counts()
        if len(hand['Dice'][pair])<3 and len(hand['Dice'][pair]) !=0:  #If at least two are the same
            point = max(hand['Dice'].mode())*2
            #print(max(hand['Dice'].mode()))
        elif len(counting_values) <4:
            #point = max(hand['Dice'])*2
            point = hand['Dice'].mode()[0]*2
        else:
            point = 0

    elif which_save == 'Two pairs': 
        pairs = hand['Dice'].duplicated()
        if len(hand['Dice'][pairs])==3:
            hand_sort = hand.sort_values(by=['Dice'])
            copies = hand.duplicated()
            #pairs = hand['Dice'].duplicated()
            count1 = hand_sort['Dice'][copies].iloc[0]*2
            count2 = hand_sort['Dice'][copies].iloc[-1]*2
            point = count1+count2
        elif len(hand['Dice'][pairs])==2:
            count1 = hand['Dice'][pairs].iloc[0]*2
            count2 = hand['Dice'][pairs].iloc[1]*2
            point = count1+count2
        else:
            point = 0

    elif which_save == 'Three of kind':
        counting_values = hand['Dice'].value_counts()
        if counting_values.iloc[0]>2:
            number = hand['Dice'].mode()[0]
            point = 3*number
        else:
            point = 0

    elif which_save == 'Four of kind':
        counting_values = hand['Dice'].value_counts()
        if counting_values.iloc[0]>3:
            number = hand['Dice'].mode()[0]
            point = 4*number
        else:
            point = 0

    elif which_save == 'Full house':
        pairs = hand['Dice'].duplicated()
        if len(hand['Dice'][pairs])==3:
            counting_values = hand['Dice'].value_counts()
            if counting_values.iloc[0]==3:
                point = sum(hand['Dice'])
            else:
                point = 0
        else:
            point = 0

    elif which_save == 'Small straight':
        counting_values = hand['Dice'].value_counts()
        if len(counting_values)==5:
            #print("It is longer")
            if max(hand['Dice'])==5 and min(hand['Dice'])==1:
                point = sum(hand['Dice'])
            else:
                point = 0
        else:
            point = 0

    elif which_save == 'Large straight':
        counting_values = hand['Dice'].value_counts()
        if len(counting_values)==5:
            print("It is longer")
            if max(hand['Dice'])==6 and min(hand['Dice'])==2:
                point = sum(hand['Dice'])
            else:
                point = 0
        else:
            point = 0

    elif which_save == 'Chance':
        point = sum(hand['Dice'])

    elif which_save == 'Yathzee':
        yatzy = Yathzee(hand)
        if yatzy == True:
            #print('YATHZEEEEEEEE!')
            point = 50
        else:
            point = 0

    else: 
        print("No idea what is happening now")


    return point

# Main function that controls the game
def main():
    scorecard = card()
    round_counter = 1   # Variable is increased in loop below.
    #print('Welcome to this sad lonely game of Yathzee!')
    print("""
    -------------------------------------------
    Welcome to this sad lonely game of Yathzee! 
    -------------------------------------------
    We play with swedish rules. This means five dice and you can roll them 
    tree times. You need to fill the scorecard but if you do not want to play 
    anymore you can write q when asked for. 
          
    If you get 63 points or more in the top categry (1-6) then you get an 
    additional 50 points. If you get Yathzee 50 point will automatically 
    be given. If you already have a yathzee you get to pick where to save 
    possible points.
          
    You cannot fill an invalid result, for example if you try to fill 
    "Three of kind" and you only have a pair you will get 0 points. 
    If you cannot save your points anywhere to the scorecard then pick
    an invalid type and it will be set to 0.
          
    There is 16 "rounds" because there are 16 possibilities on the scorecard.
    Because lazy coding, when you indicate which dice to save you should give
    the index of the die.
    Lets play!
    -------------------------------------------------------------------------
""")
    while round_counter<16: #There is 16 rounds
        cheat_mode = input('Write "test" for cheat mode and "q" for quiting: ')
        if cheat_mode =="test":     #Used for cheating or for testing the code
            print("Write your whised for dice")
            dice_list = []
            ok_dice = [1,2,3,4,5,6]
            for i in range(5):
                ele = check_input("") #int(input())
                while ele not in ok_dice:
                    ele = int(input("Pick a number 1 to 6! "))
                # adding the element
                dice_list.append(ele)
            print(dice_list)
            truefalse_column= [True,True,True,True,True]
            #print(truefalse_column)
            f_hand = pd.DataFrame({'Re_roll':truefalse_column}) 
            f_hand['Dice']=dice_list
            yatzy = Yathzee(f_hand)
            if yatzy == True:
                if math.isnan(scorecard.loc["Yathzee","Points"]):
                #if scorecard.loc['Yathzee','Points']==0:
                    #scorecard.loc["Yathzee","Points"]=50
                    print(scorecard)
                    print('**************')
                    print('YATHZEEEEEEEE!')
                    print('**************')
                    #calling_score = scoring(scorecard,f_hand)
                else:
                    print('Yathzee again?! You do not get more bonus points for it.') 
                    #calling_score = scoring(scorecard,f_hand)
                    #print(calling_score)   
            #else:
            calling_score = scoring(scorecard,f_hand)
            print(calling_score)
        elif cheat_mode =="q":
            scorecard['Points'] = scorecard['Points'].fillna(0)
            round_counter = 16
            
        else:
            f_hand=one_round(scorecard)
        
        round_counter+=1
        
        #print(scorecard)

    selected = ['Ones','Twoes','Threes','Foures','Fives','Sixes']
    bonus = scorecard[scorecard.index.isin(selected)].sum()
    bonus = bonus.to_numpy()
    #print(type(bonus))
    if bonus>=63:
        total_score = sum(scorecard['Points'])+50
        print("You got over 63 point in the top category, therfore you get extra 50 points!")
    else:
        total_score = sum(scorecard['Points'])
    print('**************************')
    print('Your total score is: ',total_score)
    print('*************************')
    '''
#Test case, roll one die
test_die =dice()
print(test_die)
print(test_die.roll())
'''
'''
    # Obsolete part of code. Can be used for future testing 
    #Creates five dice
    my_hand = hand_of_dice(5)


    #Rolls the dice
    rolling=np.array(roll(my_hand))
    print(type(rolling))

    hand_df = pd.DataFrame({'Dice':rolling})
    truefalse_column = np.full((5, 1), True)
    print(truefalse_column)
    hand_df['re_roll']=truefalse_column
    print(hand_df['Dice'])

    numberofdice = input("Enter the number of dies you want to save:")
    #Create array with the number of dice and then put in the index from the whsed for dices
    saved_dice = input('Which dice do you want to save, use index to the left to indicate')



    #row_to_be_added = [True,True,True,True,True] #np.full((1, 5), True)
    #print(row_to_be_added)
    #hand = np.r_[rolling,[row_to_be_added]]
    print("Your first hand: ",rolling)

    
    #Code that rolls three time only, no saving of dice or rolling fewer
    max_number_of_rolls = 3
    current_roll = max_number_of_rolls
    while current_roll !=0:
        my_hand = hand_of_dice(5)
        rolling=roll(my_hand)
        print(current_roll)
        print("You got: ",rolling)
        current_roll-=1
    '''


if __name__== '__main__':
    main()

