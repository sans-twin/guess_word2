from random import choice

words = ["ПЕЛЬМЕНИ", "ДРЕЛЬ", "РУЛЕТКА", "КИРПИЧ"]

guess_word = choice(words)

guessed_words = []
print("Добро пожаловать!")

while (word := input().lower()) != guess_word.lower():
    if word != guess_word and word not in guessed_words:
        guessed_words.append(word)
        print("Вы не отгадали слово!")
    elif word == guess_word:
        print("Вы угадали слово!")
