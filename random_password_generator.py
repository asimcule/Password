# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:14:34 2021

@author: Asim Upreti
"""
import random
import sys

list_of_characters = "abcdefghijklmnopqrstuvwxy!@#$%^&*zABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789>!@#$%^&*"
password_collector = ""

ask = input("Do you wanna generate a random password(y/n):").lower()



if ask == 'n':
    sys.exit(0)
    
n = int(input("How long do you want your password to be (8-12): "))


while 1:
    for i in range(n):
        character_collector = random.choice(list_of_characters)
        password_collector += character_collector
        
    print("\nYour password is:", password_collector, sep = "")
    check = input("Do you wanna generate another password(y/n):").lower()
    password_collector = ""
    
    if check == 'y':
        continue
    
    else:
        print("Thank you for using this service!!!!!")
        break
        
    

    

