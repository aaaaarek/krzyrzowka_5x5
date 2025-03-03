from DATA.data_downloader import ScrabbleDownloader
from USER_INPUT.user_input import Input
from WORD_GUESSING.word_guesser import WordGuesser

def main():
    # 1. Pobieranie słów z internetu
    downloader = ScrabbleDownloader()
    words_by_letter = downloader.download_words()

    # 2. Tworzenie listy słów
    word_list = []
    for letter, data in words_by_letter.items():
        word_list.extend(data["words"])  # Pobieramy wszystkie słowa dla każdej litery

    # 3. Pobranie danych od użytkownika (krzyżówka + dostępne litery)
    crossword, available_letters = Input.get_user_input()
    print(f"🔹 Dostępne litery: {available_letters}")

    # 4. Tworzenie obiektu WordGuesser
    solver = WordGuesser(crossword.grid, word_list, available_letters)

    # 5. Uruchamiamy algorytm rozwiązujący krzyżówkę
    if solver.solve_crossword():
        print("✅ Krzyżówka rozwiązana!")
        crossword.display()  # Wyświetlamy finalną krzyżówkę
    else:
        print("❌ Nie udało się rozwiązać krzyżówki.")

if __name__ == '__main__':
    main()
