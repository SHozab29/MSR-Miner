import webbrowser
import random
import time


#Final Draft after adding timer to reduce RAM load


with open('words.txt','r') as file:
    allWords = file.read()
    words = list(map(str,allWords.split()))

def miner():
    word = random.choice(words)
    print(word + '\n')
    webbrowser.open(f'https://www.bing.com/search?q={word}')



seconds_to_delay_search = 1 # <----------------- SET TO 0 IF SYSTEM RAM > 8GB

for i in range(0,34):
    time.sleep(seconds_to_delay_search)
    print('Search no: ',i+1)
    miner()


'''
Timer working accurately1   
dated: 20/09/2023 22:24     
'''

'''   
#Final Draft of 11/06/2023 00:20

with open('words.txt','r') as file:
    allWords = file.read()
    words = list(map(str,allWords.split()))

def miner():
    word = random.choice(words)
    print(word + '\n')
    webbrowser.open(f'https://www.bing.com/search?q={word}')

for i in range(0,34):
    print('Search no: ',i+1)
    miner()

'''

'''
Accurately doing random and non repeating searches on bing
dated: 11/06/2023 00:20
'''










#1st Draft
'''
wordArray = [ 'leave', 'lane', 'quit', 'belly', 'share', 'source', 'speech', 'medieval', 'tribe', 'pumpkin', 'elephant', 'education', 'cave', 'laundry', 'deep',' develop', 'veil', 'increase',' achieve', 'orbit', 'direct', 'move', 'fortune', 'consumer', 'revise', 'bleed', 'lonely', 'produce', 'illusion', 'miracle', 'wreck', 'heel', 'bargain', 'clue' ]

def miner():
    word = wordArray[random.randint(0,33)]
    webbrowser.open(f'https://www.bing.com/search?q={word}')

for i in range(0,34):
    miner()
'''