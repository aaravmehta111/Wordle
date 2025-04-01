import random


def main():
    print("Welcome to Word 500. Your goal is to")
    print("correct guess a randomized 5-letter word.")
    print("You will have 10 guesses.")
    print("After every guess, you will be given a 3-digit code.")
    print("The first digit corresponds to how many letters of")
    print("your guess are in the correct spot. The second digit")
    print("corresponds to how many letters of your guess are in")
    print("the goal word, however in the wrong spot.")
    print("The third digit corresponds to how many letters of your")
    print("guess are not in the goal word at all.")
    word_list = list()
    with open('text.txt') as file:
        content_without_newline = file.read().replace('\n', ' ')
        word_list = content_without_newline.split()
    num = random.randint(1, len(word_list))
    word = word_list[num]
    num_guesses = 0
    win = False
    
    while num_guesses < 10:
        guess = input('Guess a 5 letter word:')
        count_green = 0
        count_yellow = 0
        count_red = 0
        for i in range(5):
            if guess[i] == word[i]:
                count_green += 1
            elif guess[i] in word:
                count_yellow += 1
            else:
                count_red += 1
        num_guesses += 1
        if count_green == 5:
            print("CONGRATULATIONS, YOU WIN!!!")
            win = True
            break
        print("Your guess total is", count_green, count_yellow, count_red)
    if win == False:
        print("GAME OVER!!!", "The word was", word)
    
if __name__ == '__main__':
    main()
