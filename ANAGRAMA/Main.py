def message_welcome():
    print(" _________   ___       _   _________   ________   _________   _________   ____   ____   _________")
    print("|   ___   | |   \     | | |   ___   | |   _____| |   ___   | |   ___   | |    \_/    | |   ___   |")
    print("|  |   |  | |  _ \    | | |  |   |  | |  |       |  |___|  | |  |   |  | |           | |  |   |  |")
    print("|  |___|  | | | \ \   | | |  |___|  | |  |       |   _   __| |  |___|  | |  |\   /|  | |  |___|  |")
    print("|  _____  | | |  \ \  | | |  _____  | |  |_____  |  | \  \   |  _____  | |  | \_/ |  | |  _____  |")
    print("| |     | | | |   \ \ | | | |     | | |   __   | |  |  \  \  | |     | | |  |     |  | | |     | |")
    print("| |     | | | |    \ \| | | |     | | |  |__|  | |  |   \  \ | |     | | |  |     |  | | |     | |")
    print("|_|     |_| |_|     \___| |_|     |_| |________| |__|    \__\|_|     |_| |__|     |__| |_|     |_|")


def check_continue():
    print("¿Desea probar con otra pareja de palabras?")
    print("\n1.SI\n2.NO")
    return int(input("-->"))


def request_words():
    first_word = str(input("\nIntroduce la primera palabra:"))
    first_word_lower = first_word.lower()

    second_word = str(input("\nIntroduce la segunda palabra:"))
    second_word_lower = second_word.lower()

    return first_word_lower,second_word_lower


def check_anagram(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        print("\n\U00002705 La palabra ", second_word, " es anagrama de la palabra", first_word, "\U00002705")
    else:
        print("\n\U0000274C La palabra ", second_word, " NO es anagrama de ", first_word, "\U0000274C")

        
def main():
    message_welcome()
    print("\t\t\U0001F449 En el siguiente programa podra conocer si un palabra es anagrama de otra \U0001F448")
    repeat = 1
    while repeat == 1:
        word_one, word_two = request_words()
        check_anagram(word_one,word_two)
        repeat = check_continue()


main()
