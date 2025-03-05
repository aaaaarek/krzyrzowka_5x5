from CROSSWORD_MATRIX.crossword import CrossWordGrid

class Input:
    @staticmethod
    def get_user_input():

        # Tworzymy krzyżówkę z podaną literą początkową
        grid = CrossWordGrid()

        print("\n Pusta krzyżówka: ")
        grid.display()

        # Wpisywanie liter początkowych
        print("Wpisz litery początkowe (format: x y litera). X odnosi się do wiersza macierzy, y do kolumny, pole początkowe to nie (1,1) tylko (0,0). Wpisz 'end', aby zakończyć: ")
        while True:
            user_input = input("> ")
            print("\n")
            if user_input.lower() == "end":
                break
            try:
                x, y, letter = user_input.split()
                x, y = int(x), int(y)
                grid.set_letter(x, y, letter)
                grid.display()
            except ValueError:
                print("Niepoprawny format! Wpisz: x y litera")

        # Wpisywanie ID liter
        print("Wpisz Id liter (format x y Id). Wpisz 'end', aby zakończyć:")
        while True:
            user_input = input("> ")
            print("\n")
            if user_input.lower() == "end":
                break
            try:
                x, y, letter_id = user_input.split()
                x, y, letter_id = int(x), int(y), int(letter_id)
                grid.set_id(x, y, letter_id)
                grid.display()
            except ValueError:
                print("Niepoprawny format! Wpisz: x y Id")

        # Pobieramy dostępne litery
        available_letters = list(input("Podaj dostępne litery (np. ABDEFGH): ").strip().upper())

        print("\nFinalna krzyżówka:")
        grid.display()

        return grid, available_letters
