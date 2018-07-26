'''
Created on 26‏/05‏/2018

@author: imed.cherifa@gmail.com
'''

import numpy as np
from enum import Enum
class Strategie(Enum):
    switch = 1
    keep = 2

def play(strategie,n):
    
    prizedoors= np.random.randint(0, 3, size=n)
    guesses= np.random.randint(0, 3, size=n)
    goatdoors=[np.setdiff1d([0, 1, 2], [prizedoors[i], guesses[i]])[0] for i in range(len(prizedoors))]
    switch_guess=[np.setdiff1d([0, 1, 2], [guesses[i], goatdoors[i]])[0] for i in range(len(guesses))]
    
    if strategie == Strategie.switch:
        return np.equal(prizedoors,switch_guess)
        #print(res2[res2==True])
        #print( "Wins with switching: %f" % res2[res2==True].size)
    else:
        return np.equal(guesses,prizedoors)
        #print(res1[res1==True])
        #print( "Wins without switching %f" % res1[res1==True].size)

play(Strategie.switch,10)
play(Strategie.keep,10)


