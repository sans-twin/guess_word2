from random import choice

words = ["ПЕЛЬМЕНИ", "ДРЕЛЬ", "РУЛЕТКА", "КИРПИЧ"]

guess_word = choice(words)

guessed_words = []

while (word := input().lower()) != guess_word.lower():
    if word != guess_word:
        guessed_words.append(word)
    elif word == guess_word:
        print("Вы угадли слово!")
