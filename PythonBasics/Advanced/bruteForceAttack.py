import pyautogui
import random

numbers = '1234567890'

char_list = list(numbers)
password = pyautogui.password('Enter password: ')

guess_password = ''

while guess_password != password:
    guess_password = random.choices(char_list, k=len(password))

    print(f"Decripting {guess_password} password")

    if guess_password == list(password):
        print(f"Your password is: {''.join(guess_password)}")
        break