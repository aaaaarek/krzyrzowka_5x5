class CrossWordGrid:
    def __init__(self):
        self.grid = [[None for _ in range(5)] for _ in range(5)]

        # Ustawiamy domyślne blokady (X)
        empty_positions = [(1,1), (3,3), (3,1), (1,3)]
        for x, y in empty_positions:
            self.grid[x][y] = 'X'

    def set_letter(self, x, y, letter):
        if self.is_valid_position(x, y):
            self.grid[x][y] = letter.upper()
        else:
            print("Nie można umieścić litery w tym miejscu")
    
    def is_valid_position(self, x, y):
        return 0 <= x < 5 and 0 <= y < 5 and self.grid[x][y] is None
    
    def set_id(self, x, y, letter_id):
        if self.is_valid_position(x, y):
            self.grid[x][y] = letter_id
        else:
            print("Nie mozna umieścić ID w tym miejscu")

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) if cell is not None else "." for cell in row))
        print("\n")