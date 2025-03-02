import requests
from bs4 import BeautifulSoup
import logging
from collections import defaultdict

class ScrabbleDownloader:
    def __init__(self, letters=None, base_url=None):
        # Konfiguracja loggera
        self.logger = logging.getLogger('ScrabbleDownloader')
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        # Lista liter
        self.letters = letters or ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                   "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "W", "Y", "Z"]
        
        # Bazowy URL
        self.base_url = base_url or "https://scrabblemania.pl/słowa-na-literę-{}/5-literowe/strona-{}"

    def download_words(self):
        """
        Pobiera słowa i tworzy strukturę indeksowania dla szybszego wyszukiwania.
        """
        words_index = {}

        for letter in self.letters:
            words = []
            index = defaultdict(lambda: defaultdict(list))  # Indeks pozycji liter
            page = 1  # Zaczynamy od pierwszej strony

            while True:
                url = self.base_url.format(letter, page)
                self.logger.info(f"Pobieram dane dla litery {letter}, strona {page}: {url}")

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                except requests.RequestException as e:
                    self.logger.error(f"Błąd pobierania strony {page} dla litery {letter}: {e}")
                    break  # Przerywamy w przypadku błędu

                soup = BeautifulSoup(response.text, "html.parser")
                menu_container = soup.find("div", class_="menu-container")

                if not menu_container:
                    self.logger.warning(f"Nie znaleziono słów dla litery {letter}, strona {page}")
                    break  # Jeśli nie ma więcej stron, kończymy

                new_words = []
                for a in menu_container.find_all("a"):
                    word = a.get_text(strip=True)
                    if len(word) == 5:  # Filtrujemy tylko słowa 5-literowe
                        new_words.append(word)
                        for i, char in enumerate(word, start=1):  # Indeksujemy pozycje liter
                            index[i][char].append(word)

                if not new_words:
                    break  # Jeśli na stronie nie ma nowych słów, kończymy iterację

                words.extend(new_words)
                page += 1  # Przechodzimy do kolejnej strony

            words_index[letter] = {
                "words": words,
                "index": dict(index)  # Konwertujemy defaultdict na zwykły dict
            }
            self.logger.info(f"Znaleziono {len(words)} wyrazów dla litery {letter}")

        return words_index
