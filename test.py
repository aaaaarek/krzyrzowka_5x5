from DATA.data_downloader import ScrabbleDownloader
from USER_INPUT.user_input import Input
def main():
    #downloader = ScrabbleDownloader()
    #words_by_letter = downloader.download_words()
    
    # Wyświetlenie wyników pobierania słów
    """
    for letter, data in words_by_letter.items():
            print(f"Litera {letter}:")
            if data["words"]:  # Jeśli są znalezione słowa
                print(", ".join(data["words"][:10]))  # Wypisz pierwsze 10 dla przejrzystości
            else:
                print("Brak słów dla tej litery.")
            print("-" * 40)
    """

    crossword, available_letters = Input.get_user_input()
    print(f"Dostępne litery: {available_letters}")

if __name__ == '__main__':
    main()
