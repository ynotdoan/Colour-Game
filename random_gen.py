
import random


def get_random_num(arr):
  '''
  Generates random number within length of list given.
  '''
  random_num = random.randint(0, len(arr) - 1)
    
  return random_num