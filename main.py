# File:main.py
# Author:Abdullah Navaid
# Date:2/7/24
# Description: Adding mistakes count for the player if the word is guessed incorrectly and keep count.




import random
import os
# This function will shuffle your word list, which can be used to shuffle board.
# INPUTS:
# list - passed by assignment, which means it does not need to be returned.
# When the list is passed in, changes made to the list will persist outside
# of the function.
def shuffle(list):
    random.seed(10)
    n = len(list)
    new_list = []
    while len(list) != 0: # randomly select words until list is empty
        ind = random.randint(0, len(list) - 1)
        new_list.append(list[ind])
        list.pop(ind) # remove from original list
    for i in range(n): # since passed by assignment, we must update list
        list.append(new_list.pop())

# This function reads in data from the file named filename.
# (e.g. words, solution = readFile("Day0.txt")
# sets up list of words and solution for Day 0 board
# INPUT:
# filename - a string, e.g. "Day0.txt."
# OUTPUTS:
# words - a list of words (strings) that will make up the 4 by 4 gameboard
# solution - a dictionary of the solution, e.g. solution = {"data types": {"int",
# "float", "string", "boolean"}, ...}
def readFile(filename):
    file = open(filename)
    list = file.readlines()
    words = []  # list of all words
    solution = {}  # dictionary of solution
    for line in range(1, len(list) + 1): # line is line number
        if line % 2 == 1: # odd, 1, 3, 5, 7 (categories)
            category = list[line - 1]
        else:  # even, 2, 4, 6, 8 (words)
            tokens = list[line - 1].split(", ")
            tokens[-1] = tokens[-1].strip()
            solution[category] = set(tokens)
            words.extend(tokens)  # clean up new line character
    return words, solution
# Checks if wordsSelected match a category in solution.
# If they do, returns the category.  If not, returns empty string.
# Assumes all words are lower case (in solution and wordsSelected).
# INPUTS:
# solution - a dictionary that pairs the category with the set of four words
# wordsSelected - a set of four words entered by player
# OUTPUT:
# category - a string that represents the category found
def checkSolution(solution, wordsSelected):
    for category, word_set in solution.items():
        if set(wordsSelected) == word_set:
            return category
    return ""



# My Code
gameboard = ["for", "while", "do", "sentinel", "int", "float", "string", "boolean", "list", "dictionary", "set", "tuple", "input", "output", "comments", "header"]
print('Connections')
print('Group words that share a common thread.')
username = input('Enter your username: \n')
if len(username) >= 2:
    if username[0].isdigit() and username[1].isdigit():
        print('Username must start with a letter, please try again: ')
        username = input()
        if username[0].isdigit() and username[1].isdigit():
            print('Goodbye.')
            exit()
        else:
            print('Welcome,', username + '!')
    elif len(username) != 8 :
        print('Username must be 8 characters, please try again: ')
        username = input()
        if len(username) != 8 or (username[0].isdigit() and username[1].isdigit()) :
            print('Goodbye.')
            exit()
        print('Welcome,', username + '!')
    else:
        print('Welcome,', username + '!')
elif len(username) < 1:
    username_no_letters = input('Username must be 8 characters, please try again: \n')
    print('Welcome,', username_no_letters + '!')
else:
    print('Username must start with a letter, please try again.')

# Continuing with the rest of the code


enter_to_start = input('Press enter to start: \n')
board_number = input('Enter number (0-99): \n')
if board_number.isdigit() and int(board_number) and 6<int(board_number)<100:
    print('Sorry, that board is unavailable, setting up the default board.\n')
elif board_number.isdigit() and 0 <= int(board_number) <= 6:
    print('',end='')
else:
    print('Enter number (0-99), please try again: ')
    board_number = input()
    if board_number.isdigit() and 0 <= int(board_number) <= 6:
        print('',end='')
    else:
        print('Sorry, that board is unavailable, setting up the default board.\n')
       


#Names Files
if board_number.isdigit() and 0 <= int(board_number) <= 6:
    filename = 'Day' + board_number + '.txt'
    gameboard, solution = readFile(filename)
    shuffle(gameboard)


#Keeps count of # of mistakes
mistakes = int()



print("Create four groups of four!")


#Turn gameboard into seperate non list strings and use gameboard_capitalized as the new list with all capitalized words 

gameboard_strings = ' '.join(gameboard)
gameboard_strings = gameboard_strings.upper()
gameboard_capitalized = list(gameboard_strings.split())
gameboard_capitalized = gameboard_capitalized

first_part = gameboard_capitalized[0:4]
second_part = gameboard_capitalized[4:8]
third_part = gameboard_capitalized[8:12]
fourth_part = gameboard_capitalized[12:16]


#Formats the output of words
print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')
print('| {:10}'.format(fourth_part[0]), '| {:10}'.format(fourth_part[1]), '| {:10}'.format(fourth_part[2]),'| {:10}'.format(fourth_part[3]),  '|')
print()

#First part check

# APPLIES A CERTAIN FORMAT AND CONSTRAINS FOR EACH WORD
first_word = input("Enter first word: \n").lower()



second_word = input("Enter second word: \n").lower()

if second_word in first_word or (second_word.upper() not in gameboard_capitalized):
    second_attempt = input('Not a valid game board word, try again: \n')
    
        


third_word = input("Enter third word: \n").lower()
if third_word.upper() not in gameboard_capitalized:
    second_attempt = input('Not a valid game board word, try again: \n')
    third_word = second_attempt.lower()

forth_word = input("Enter fourth word: \n").lower()
if forth_word in third_word or (forth_word.upper() not in gameboard_capitalized):
    second_attempt = input('Not a valid game board word, try again: \n')
    forth_word = second_attempt.lower().strip()


first_word = first_word.lower().strip()
second_word = second_word.lower().strip()
third_word = third_word.lower().strip()
forth_word = forth_word.lower().strip()


print('Create four groups of four!')


user_words = (first_word,second_word,third_word,forth_word)
result = checkSolution(solution,user_words)

first_part_word = first_word
second_part_word = second_word
third_part_word = third_word
fourth_part_word = forth_word
if result:
    # Removes the words of input from the gameboard list and saves it into this new list
    gameboard_capitalized.remove(first_word.upper())
    gameboard_capitalized.remove(second_word.upper())
    gameboard_capitalized.remove(third_word.upper())
    gameboard_capitalized.remove(forth_word.upper())
    first_part = gameboard_capitalized[0:4]# Have 4 words from the list in each line
    second_part = gameboard_capitalized[4:8]
    third_part = gameboard_capitalized[8:12]
    fourth_part = gameboard_capitalized[12:16]
    
    if mistakes == 1:
        print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')

    #Formats all four lines of the output seperately
    print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
    print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
    print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')
    #Checks the solution for category with all four user input words and prints it in the required format
    category = checkSolution(solution, {first_word, second_word, third_word, forth_word})
    category = category.upper()
    category = category.strip()
    
    print(category + ':', first_word.upper()+',' , second_word.upper()+ ',' , third_word.upper()+',' , forth_word.upper())
    print('Mistakes:', mistakes)
    print()
else:
    print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
    print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
    print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')
    print('| {:10}'.format(fourth_part[0]), '| {:10}'.format(fourth_part[1]), '| {:10}'.format(fourth_part[2]),'| {:10}'.format(fourth_part[3]),  '|')
    print('Mistakes:', mistakes + 1)
    mistakes = mistakes + 1
    print()
mistakes = mistakes



category = checkSolution(solution, {first_word, second_word, third_word, forth_word})
category = category.upper()
category = category.strip()
category_first_part = category

#SECOND PART CHECK

# APPLIES A CERTAIN FORMAT AND CONSTRAINS FOR EACH WORD
first_word = input("Enter first word: \n").lower().strip()
if first_word.upper() not in gameboard_capitalized:
    second_attempt = input('Not a valid game board word, try again: \n')


second_word = input("Enter second word: \n").lower().strip()

if second_word in first_word or (second_word.upper() not in gameboard_capitalized):
    second_attempt = input('Not a valid game board word, try again: \n')
    second_word = second_attempt
    second_word = second_word.strip()

third_word = input("Enter third word: \n").lower().strip()

if third_word in second_word or (third_word.upper() not in gameboard_capitalized):
    input('Not a valid game board word, try again: \n')

forth_word = input("Enter fourth word: \n").lower().strip()
if forth_word in third_word or (forth_word.upper() not in gameboard_capitalized):
    second_attempt = input('Not a valid game board word, try again: \n')
    forth_word = second_attempt.lower()
print('\nCreate four groups of four!')


user_words = (first_word,second_word,third_word,forth_word)

result = checkSolution(solution,user_words)


if result:
    # Removes the words of input from the gameboard list and saves it into this new list
    gameboard_capitalized.remove(first_word.upper())
    gameboard_capitalized.remove(second_word.upper())
    gameboard_capitalized.remove(third_word.upper())
    gameboard_capitalized.remove(forth_word.upper())
    first_part = gameboard_capitalized[0:4]# Have 4 words from the list in each line
    second_part = gameboard_capitalized[4:8]
    third_part = gameboard_capitalized[8:12]

    #Formats all four lines of the output seperately
    print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
    print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
    if mistakes == 1:
        print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')

    #Checks the solution for category with all four user input words and prints it in the required format
    category = checkSolution(solution, {first_word, second_word, third_word, forth_word})
    category = category.upper()
    category = category.strip()
    if mistakes == 0:
        print(category + ':', first_word.upper()+',' , second_word.upper()+ ',' , third_word.upper()+',' , forth_word.upper())
        print(category_first_part + ':', first_part_word.upper()+',' , second_part_word.upper()+ ',' , third_part_word.upper()+',' , fourth_part_word.upper())
    elif mistakes >= 1:
        print(category + ':', first_word.upper()+',' , second_word.upper()+ ',' , third_word.upper()+',' , forth_word.upper())
    print('Mistakes:', mistakes)
    print()
    print('Goodbye.')
elif mistakes == 1:
    print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
    print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
    print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')
    print('| {:10}'.format(fourth_part[0]), '| {:10}'.format(fourth_part[1]), '| {:10}'.format(fourth_part[2]),'| {:10}'.format(fourth_part[3]),  '|')
    print('Mistakes:', mistakes + 1)
    print()
    print('Goodbye.')
else:
    print('| {:10}'.format(first_part[0]), '| {:10}'.format(first_part[1]), '| {:10}'.format(first_part[2]),'| {:10}'.format(first_part[3]), '|')
    print('| {:10}'.format(second_part[0]), '| {:10}'.format(second_part[1]), '| {:10}'.format(second_part[2]),'| {:10}'.format(second_part[3]),  '|')
    print('| {:10}'.format(third_part[0]), '| {:10}'.format(third_part[1]), '| {:10}'.format(third_part[2]),'| {:10}'.format(third_part[3]),  '|')
    mistakes = 1
    if mistakes == 1:
        print(category_first_part + ':', first_part_word.upper()+',' , second_part_word.upper()+ ',' , third_part_word.upper()+',' , fourth_part_word.upper())
    print('Mistakes:', mistakes)
    print()
    print('Goodbye.')





