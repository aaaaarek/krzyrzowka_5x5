from DATA.data_downloader import ScrabbleDownloader
from USER_INPUT.user_input import Input
from WORD_GUESSING.word_guesser import WordGuesser
from CROSSWORD_MATRIX.crossword import CrossWordGrid

def main():
    test_grid = [
    [2, 10, 7, 12, 1],
    [11, 'X', 5, 'X', 5],
    [8, 10, 7, 12, 'C'],
    [11, 'X', 2, 'X', 3],
    ['C', 3, 5, 9, 4]
]

    test_available_letters = list("ABCEHIJKLORT")

    # 1. Pobieranie słów z internetu
    downloader = ScrabbleDownloader()
    words_by_letter = downloader.download_words()

    # 2. Tworzenie listy słów
    word_list = [] #to jest okej, tu jest jakies 25000 slow
    
    for letter, data in words_by_letter.items():
        word_list.extend(data["words"])  # Pobieramy wszystkie słowa dla każdej litery

    # 3. Pobranie danych od użytkownika (krzyżówka + dostępne litery)
    #crossword, available_letters = Input.get_user_input()
    #print(f"🔹 Dostępne litery: {available_letters}")

    crossword = CrossWordGrid()  # Utwórz pustą krzyżówkę
    crossword.grid = test_grid  # Przypisz gotową macierz
    available_letters = test_available_letters  # Przypisz dostępne litery


    # 4. Tworzenie obiektu WordGuesser
    solver = WordGuesser(crossword.grid, word_list, available_letters)

    print()

    filtered_words = solver.match_words_to_position()
    print(f"🧐 Możliwe słowa do użycia ({len(filtered_words)}): {filtered_words}")

    # 5. Uruchamiamy algorytm rozwiązujący krzyżówkę
    if solver.solve_crossword():
        print("✅ Krzyżówka rozwiązana!")
        crossword.display()  # Wyświetlamy finalną krzyżówkę
    else:
        print("❌ Nie udało się rozwiązać krzyżówki.")

if __name__ == '__main__':
    main()
