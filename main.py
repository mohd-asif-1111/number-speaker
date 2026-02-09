import pygame # type: ignore
import time

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def num_to_words(num):
    if num < 1:
        return ''
    if num < 10:
        return [ones[num - 1]]
    elif num < 20:
        return [teens[num % 10]]
    elif num < 100:
        return [tens[num // 10], num_to_words(num % 10)]
    elif num < 1000:
        return [ones[num // 100 - 1], 'hundred', num_to_words(num % 100)]
    elif num < 1000000:
        return [num_to_words(num // 1000), 'thousand', num_to_words(num % 1000)]
    elif num < 1000000000:
        return [num_to_words(num // 1000000), 'million', num_to_words(num % 1000)]
    elif num < 1000000000000:
        return [num_to_words(num // 1000000000), 'billion', num_to_words(num % 1000000000)]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            if item:
                result.append(item)
    return result

def word_to_audio(words):
    for word in words:
        sound = pygame.mixer.Sound(f'sound/{word}.mp3')
        if sound:
            sound.play()
        
        while pygame.mixer.get_busy():
            time.sleep(0.1)
    print('All sounds finished!')


pygame.init()
pygame.mixer.init()

words = flatten(num_to_words(9))
word_to_audio(words)
print(' '.join(words))    
