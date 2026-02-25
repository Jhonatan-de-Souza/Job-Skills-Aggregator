from time import sleep
from random import randint

def sleep_random(min=2,max=4):
    sleep(randint(min,max))