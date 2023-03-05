"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""

import random as r
import os
from colorama import Fore, Style

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/   
                   '''
print(f"\nWelcome to \n {logo}")

word_list = ["Dog","Cow","Cat","Horse","Donkey","Tiger","Lion","Panther","Leopard","Cheetah"	
,"Bear","Elephant","Turtle","Tortoise","Crocodile","Rabbit","Porcupine","Hare","Hen","Pigeon"	
,"Albatross","Crow"	,"Fish","Dolphin","Frog","Whale","Alligator","Eagle","Squirrel","Ostrich"	
,"Fox","Goat","Jackal","Emu","Armadillo","Eel","Goose","Arctic","Wolf","Beagle"	
,"Chimpanzee","Monkey","Beaver","Orangutan","Antelope","Bat","Badger","Giraffe","Crab","Giant" 
,"Panda","Hamster","Cobra","Shark","Camel","Hawk","Deer","Chameleon","Hippopotamus","Jaguar"	
,"Chihuahua","King" ,"Cobra","Ibex","Lizard","Koala","Kangaroo"	,"Iguana","Llama","Dodo"	
,"Jellyfish","Rhinoceros","Hedgehog","Zebra","Possum","Bison","Bull","Buffalo","Sheep","Meerkat"	
,"Mouse","Otter","Sloth","Owl","Flamingo","Racoon","Mole","Duck","Swan","Lizard"	
,"Elk","Boar","Mule","Baboon","Mammoth","Whale","Rat","Snake","Peacock","Gorilla"]

word_list_length = len(word_list)

while(True):
    chosen_word = word_list[r.randint(0,word_list_length-1)]

    chosen_word_length = len(chosen_word)

    guess_letter_list = []
    for i in range(chosen_word_length):
        guess_letter_list.append('_')

    print(f"\nWord to complete: ", *guess_letter_list, sep = ' ')

    correct_guess_letter_count = 0

    for i in range(chosen_word_length):
        guess_letter = input(f"\nGuess a letter ({chosen_word_length - i} Attempts left): ").lower()

        for i in range(chosen_word_length):
            if chosen_word[i].lower() == guess_letter:
                guess_letter_list[i] = chosen_word[i].lower()

        os.system('clear')
        print(f"\nWord to complete: ", *guess_letter_list, sep = ' ')
        
        
    guess_word = ''
    for i in range(len(guess_letter_list)):
        guess_word += guess_letter_list[i]

    for i in range(len(guess_word)):
        if guess_word[i].lower() == chosen_word[i].lower():
            correct_guess_letter_count += 1

    if guess_word.capitalize() == chosen_word.capitalize():
        print(Fore.GREEN + f"\nYou won! You guessed <<< {correct_guess_letter_count} >>> out of {chosen_word_length} letters!")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + f"\nYou lost! The word was <<< {chosen_word} >>>, You guessed {correct_guess_letter_count} out of {chosen_word_length} letters!")
        print(Style.RESET_ALL)





