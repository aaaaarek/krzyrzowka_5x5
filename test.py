from DATA.data_downloader import ScrabbleDownloader

def main():
    downloader = ScrabbleDownloader()
    words_by_letter = downloader.download_words()
    
    # Wyświetlenie wyników
    for letter, words in words_by_letter.items():
        print(f"Litera {letter}:")
        for word in words:
            print(word)
        print("-" * 40)

if __name__ == '__main__':
    main()
