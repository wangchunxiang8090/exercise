#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
def password(length=12):
    code = []
    for i in range(length):
        r = random.randint(1,9)
        if r == i:
            code.append(str(random.randint(0,9)))
        elif r > 5:
            code.append(chr(random.randrange(97,122)))
        else:
            code.append(chr(random.randrange(65,90)) )
    print(''.join(code))

if __name__ == "__main__":
    number=input('please input generator password length default length 12:')
    if len(number) == 0:
        password()
    else:
        if number.isdigit():
            number = int(number)
            password(number)
        else:
            exit('invalid input')
