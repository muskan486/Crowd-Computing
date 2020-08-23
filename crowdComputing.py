import random

def choose():
    list=["rainbow","computer","science","programming","player","condition","water","board"]
    pick=random.choice(list)
    return pick
    
    

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled


def thank(pl1,pl2,p1,p2):
    print(pl1,'your score is',p1)
    print(pl2,'your score is',p2)
    print('thankyou for playing')
    

def play():
   play1=input('enter your name player 1')
   play2=input('enter player2 your name')
   pp1=0
   pp2=0
   turn=0
   while(1):
       word=choose()
       qn=jumble(word)
       print(qn)
       if turn%2==0:
           #player1
           print(play1, 'your turn!')
           ans=input('enter whats in your mind player 1')
           if ans==word:
               pp1=pp1+1
               print('your score is ',pp1)
           else:
               print('sorry better luck next time',play1)
               c=input('enter 1 to continue and 0 to quit')
               if c==0:
                    thank(play1,play2,pp1,pp2)
                    break
       else:
            #player2
            print('your turn',play2)
            ans=input('enter whats in your mind')
            if ans==word:
                pp2=pp2+1
                print('your score is',pp2)
            else:
                print('better luck next time',play2)
                c=input('enter 1 to continue and 0 to quit')
                if c==0:
                    thank(play1,play2,pp1,pp2)
                    break
       turn=turn+1            
            
                 
play()
                   
               
           
        