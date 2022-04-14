from random import randint
from art import logo, vs
from game_data import data
import os

answer = None

while not answer == "n":
    print(logo)
    choice_a = data[randint(0, len(data) - 1)]
    choice_b = data[randint(0, len(data) - 1)]

    while choice_a == choice_b:
        choice_b = data[randint(0, len(data) - 1)]

    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

    choice_player = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    score = 0

    if choice_player == "a":
        if choice_a['follower_count'] > choice_b['follower_count']:
            print("You are right!")
            score += 1
            print(f"You are right! Your score = {score}")
        elif choice_a['follower_count'] < choice_b['follower_count']:
            print("Sorry, that's wrong.")

    if choice_player == "b":
        if choice_b['follower_count'] > choice_a['follower_count']:
            score += 1
            print(f"You are right! Your score = {score}")
        elif choice_b['follower_count'] < choice_a['follower_count']:
            print("Sorry, that's wrong.")

    answer = input("Do you want to continue? Type 'Y' or 'N': ").lower()

print("Thank you!")
