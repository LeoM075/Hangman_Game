import tkinter as tk
import random
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

wordlist_path = os.path.join(script_dir, "wordlist.txt")

with open (wordlist_path, "r") as file:
    content = file.readlines()
    
striped_words = [word.strip() for word in content]

#Attempt Tracker
failed_attempts = 0 
max_attempts = 5



#LISTEN

random_word = random.choice(striped_words)

hidden_word = ['*' for _ in random_word]

user_inputs = []



letters_random_word_in_list = list(random_word)
#GAMESCHLEIFE
while failed_attempts < max_attempts:
    guess = input("Bitte rate einen Buchstaben oder gibt exit ein um das Spiel zu beenden: " ).lower()
    
    if guess.lower() == "exit":
        print ("Das Spiel wurde beendet")
        break
    user_inputs.append(guess)
    guess_found = False
    #buchstaben vom randomword werden index zugeordnet und mit forschleife durchgegangen, wenn der guess dem Wert/buchstaben entspricht wird bei dem index beim hiddenword der guess eingetragen und guess found auf true gesetzt wenn nicht wird ist guess found false und attemt tracker geht ein hoch
    for index, wert in enumerate(letters_random_word_in_list):
        if wert == guess:
            hidden_word[index] = guess
            guess_found = True
            print ("geilo")
    if not guess_found:
        failed_attempts += 1
        
    #geratenen Buchstaben, der lösungsfortschritt und die fehlgeschlagenen verusche werden angezeigt
    print("Geratene Buchstaben:", " ".join(user_inputs))
    print("Lösung:", " ".join(hidden_word))
    print("Fehlgeschlagene Versuche:", failed_attempts)
        
    #wenn failed attempts gleich max attempts sind ist das spiel vorbei und lösung wird angezeigt
    if failed_attempts == max_attempts:
            print ("Sorry du hast verloren")
            print ("Die Lösung war:", random_word)
            break
    #print("Zufälliges Wort:", random_word)
    #print("Anzahl der Buchstaben:",len(random_word))