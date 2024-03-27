import random 

words = ['abacate', 'domingos', 'palindromo', 'python', 'javascript']

word = random.choice(words)
print('Seja Bem-Vindo ao Jogo Da Forca')
shot = 0
chance = []

while shot < 5:
        hidden_word = ['_' for _ in word]
        print(" ".join(hidden_word))

        if "".join(hidden_word) == word:
            print("Você acertou!")
            break
        if chance:
            print(f"letras tentadas: {''.join(chance)}")
            wordp = input("digite uma letra: ")

        if wordp not in word:
            shot -= 1
            chance.append(wordp)
            print("letra incorreta!")
        else:
            for i in range(len(word)):
                if word[i] == wordp:
                    hidden_word[i] = wordp
else:
    print(f"Você não tem mais tentativas. A palavra era: {word}")