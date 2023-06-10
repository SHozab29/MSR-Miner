import webbrowser
import random



#Final Draft

with open('words.txt','r') as file:
    allWords = file.read()
    words = list(map(str,allWords.split()))

def miner():
    word = random.choice(words)
    print(word + '\n')
    webbrowser.open(f'https://www.bing.com/search?q={word}')

for i in range(0,34):
    miner()



'''
Accurately doing random and non repeating searches on bing
dated: 11/06/2024 00:20
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