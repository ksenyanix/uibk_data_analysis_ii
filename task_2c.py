import os
import re


email = input("Please enter your email: ")

def solution(em):
    email_check = re.compile(r"@student.uibk.ac.at", re.IGNORECASE)
    result = re.search(email_check, em)
    if result:
        print('You are a student of UIBK :)')
    else:
        print('You are not a student of UIBK :(')

solution(email)