import numpy as np
import pandas as pd

#class scoresheet():
def card():
    
#combinations=['Ones','Twoes','Thres','Foures','Fives','Sixes']
#scorecard=pd.DataFrame(columns=['Points'],index=combinations)
#def the_sheet():
    combinations=['Ones','Twoes','Threes','Foures','Fives','Sixes','Pair','Two pairs','Three of kind','Four of kind','Full house', 'Small straight', 'Large straight', 'Chance','Yathzee']
    scorecard=pd.DataFrame(columns=['Points'],index=combinations)
    #scorecard['Points'] = scorecard['Points'].fillna(0)
    #df['DataFrame Column'].fillna(0)
    #print(scorecard)
    return(scorecard)



