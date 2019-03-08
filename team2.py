import random

'''team_name = 'Big bubbas'
strategy_name = 'BBCC'
strategy_description = 
Random choice first round. If the opponent betrays in the first round, betray second round.If the opponent betrays in the first round, and we collide, betray second round. If the opponent collides in the first round, collide second round.
Something else, collide

def moveA(my_history, their_history, my_score, their_score):
    if (my_score==0 and their_score==0) and ( ' ' in their_history[0]):
        return random.choice['c','b'] 
    elif (my_score==0 and their_score==0) and ('b' in their_history[-1]):
        return 'b'
    elif (my_score== -100 and their_score==300) and ( 'b' in their_history[-1]):
        return 'b'
    elif (my_score== 300 and their_score==-100) and ( 'c' in their_history[-1]):
        return 'c'
    else:
        return 'c'

team_name = 'Big bubbas'
strategy_name = 'Idk'
strategy_description = Produces a random choice disregaurding their score or history
    
def moveB(my_history, their_history, my_score, their_score):
    
    return random.choice(['c','b'])'''
    
team_name = 'Big bubbas'
strategy_name = 'Friends with Benefits'
strategy_description = '''\If the opponent collides, we collide. If the opponent betrays, betray'''

def moveC(my_history, their_history, my_score, their_score):
  
    if 'c' in (their_history): 
        return 'c'
    elif 'b' in (their_history): 
        return 'b'
    else:
        return 'c'
    
