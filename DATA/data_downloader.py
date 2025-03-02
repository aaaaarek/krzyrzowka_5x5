import requests
from bs4 import BeautifulSoup
import logging

class ScrabbleDownloader:
    def __init__(self, letters=None, base_url=None):
        # Konfiguracja loggera dla klasy
        self.logger = logging.getLogger('ScrabbleDownloader')
        self.logger.setLevel(logging.INFO)
        # Jeśli nie ma handlera, dodajemy go
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        # Domyślna lista liter
        if letters is None:
            self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                            "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "W", "Y", "Z"]
        else:
            self.letters = letters
        
        # Bazowy URL – zakładamy, że adres ma następujący format
        if base_url is None:
            self.base_url = "https://scrabblemania.pl/słowa-na-literę-{}/5-literowe/strona-{}"
        else:
            self.base_url = base_url

    def download_words(self):
        """
        Pobiera ze stron słowa 5-literowe i zwraca słownik,
        gdzie kluczem jest litera, a wartością lista wyrazów.
        """
        words_by_letter = {}
        
        for letter in self.letters:
            words = []
            page = 1
            while True:
                url = self.base_url.format(letter, page)
                self.logger.info(f"Pobieram dane dla litery {letter} z {url}")
                
                try:
                    response = requests.get(url)
                    response.raise_for_status()  # Sprawdzenie poprawności odpowiedzi

                except requests.RequestException as e:
                    self.logger.error(f"Błąd pobierania strony dla litery {letter}: {e}")
                    break

                soup = BeautifulSoup(response.text, "html.parser")
                menu_container = soup.find("div", class_="menu-container")
                
                if not menu_container:
                    self.logger.warning(f"Nie znaleziono kontenera 'menu-container' dla litery {letter}")
                    words_by_letter[letter] = []
                    break # jezeli nie ma kontenera to nie bedzie slow na stronie

                new_words = [a.get_text(strip=True) for a in menu_container.find_all("a") if len(a.get_text(strip=True)) == 5]

                if not new_words:
                    self.logger.info(f"Brak nowych slów na stronie {page} dla litery {letter}")
                    break

                words.append(new_words)
                page += 1
                    
            self.logger.info(f"Znaleziono {len(words)} wyrazów 5-literowych dla litery {letter}")
            words_by_letter[letter] = words

        return words_by_letter
