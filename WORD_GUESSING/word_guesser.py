class WordGuesser:
    def __init__(self, grid, word_list, available_letters):
        self.grid = grid
        self.word_list = self.filer_words_by_alphabet(word_list, available_letters)
        self.available_letters = available_letters
        self.initial_positions = self.find_initial_letters(grid)

    def filer_words_by_alphabet(self, word_list, available_letters):
        return [word for word in word_list if all(letter in available_letters for letter in word)]
    
    def find_initial_letters(self, grid):
        import string
        initial_positions = {}
        alphabet = set(string.ascii_uppercase)  # Zestaw liter A-Z

        for x in range(5):
            for y in range(5):
                cell = grid[x][y]
                if isinstance(cell, str) and cell in alphabet:  # Sprawdzamy, czy to litera
                    initial_positions[(x, y)] = cell
        return initial_positions
    
    def match_words_to_position(self):
        matching_words=[]
        for word in self.word_list:
            valid = True
            for (x,y), letter in self.initial_positions.items():
                index = self.get_index_in_word(x, y)
                if index is not None and word[index] != letter:
                    valid = False
                    break
            if valid:
                matching_words.append(word)
        return matching_words
    
    def get_index_in_word(self, x, y):
        if x % 2 == 0: #słowa poziome
            return y
        elif y % 2 == 0: #słowa pionowe
            return x
        return None
    
    def check_completion(self):
        for row in self.grid:
            for cell in row:
                if cell is None or isinstance(cell, int):
                    return False
        return True
    
    def try_place_word(self, word):
        for x in range(5):
            for y in range(5):
                if self.is_valid_placement(x, y, word):
                    print(f"Próbujemy umieścić: {word} na ({x}, {y})")
                    self.place_word(x, y, word)
                    return True
        return False
    
    def solve_crossword(self, position=0):
        if position >= len(self.word_list):
            return self.check_completion()
        
        for word in self.word_list:
            if self.try_place_word(word):
                if self.solve_crossword(position+1):
                    return True
                self.remove_word(word)

        return False
    
    def is_valid_placement(self, x, y, word):
        for i, letter in enumerate(word):
            pos_x, pos_y = self.get_position_in_grid(x,y,i)
            
            if pos_x is None or pos_y is None:
                return False
            
            if self.grid[pos_x][pos_y] not in (None, letter):
                print(f"❌ Konflikt na ({pos_x}, {pos_y}): {self.grid[pos_x][pos_y]} != {letter}")
                return False
        return True
    

    def get_position_in_grid(self, x, y, i):
        if x % 2 == 0:
            return x, y+1
        if y % 2 == 0:
            return x+i, y
        return None, None

    def place_word(self, x, y, word):
        for i, letter in enumerate(word):
            pos_x, pos_y = self.get_position_in_grid(x,y,i)
            if pos_x is not None and pos_y is not None:
                self.grid[pos_x][pos_y] = letter

    def remove_word(self, word):
        for x in range(5):
            for y in range(5):
                if isinstance(self.grid[x][y], str) and self.grid[x][y] in word:
                    self.grid[x][y] = None
