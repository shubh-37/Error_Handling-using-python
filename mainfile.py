'''
This is the main py file that will be providing for unit testing in test.py
'''

def cap_first(str): #this function capatilizes the first letter of the first word in the string
    return str.capitalize()

def cap_all(str): #this function capatilizes the first letter of all the words in the string
    return str.title()

cap_first('shubh is great')
cap_all('shubh is great')