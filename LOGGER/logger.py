import logging
import sys

# Utworzenie loggera o nazwie 'krzyzowki'
logger = logging.getLogger('krzyzowki')
logger.setLevel(logging.DEBUG)  # Ustawienie poziomu logowania na DEBUG

# Konfiguracja handlera do wyświetlania logów w konsoli
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Ustalenie formatu logów
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Dodanie handlera do loggera
logger.addHandler(console_handler)
