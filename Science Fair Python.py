#importing modules to use their held functions

import itertools
from string import ascii_lowercase , digits

'''
setting constant variables, the set of characters
that are going to be used in the bruteforce , and
the password to attempt a crack upon.
'''

CHAR_SET = ascii_lowercase + digits
PASSWORD = "abcd1"

def crack_password(password):
        '''
        writing a main function to call it later
        '''

        attempt = 0 #start initial value of attempts
        
        for _ in range(1,9): #for every item in [1,2,3,4,5,6,7,8] (excluding 9)
                
                for i in itertools.product(CHAR_SET , repeat = _): # take items from char set and have the reapeat as the
                                                                   #item of current value in range

                        attempt += 1 # new value of attempt rises up by 1
                        i = ''.join(i) # turns all the values in an array into a single string.
                        
                        if i == PASSWORD: #if the current attempt is the right password:
                                return f"Password Crack Successful - {i} Attemts : {attempt}"
                        
                        else: #if the current attempt is *not* the right password:
                                print("Password '{}' Failed.".format(i))

print(crack_password(PASSWORD)) #start the function with the paramater as the variable PASSWORD

