# NIDUC2
## Changelog
### 30.12.2024
- naprawione obliczanie poprawnie zdekodowanych bloków
### 21.12.2024
- Podzielone pliki na pakiety i foldery
- Dodane enumy do przeplotów, kodów i kanałów, żeby nie pisać wszystkiego jako string
- transmitter.py: teraz na wejście trzeba podać rozmiar bloku informacji, koder, rodzaj przeplotu i ilosc symboli parzystości, ale chyba do LDPC jeszcze trzeba zrobić parę poprawek
- Do kanalow BSC dodałem enumy jako konstruktory klasy
- skrypty testujące w folderze simulations od teraz lepiej dawac, bo potem jak coś będzie się chciało powtórzyć to trzeba od nowa kod wymyślać
- sattelite.py dodane enumy
- testing.py zmiana metody do sukcesów dekodowania, porównywania bitów i bajtów danych w kanale BSC: bsc_noise_comparison. Wszystko uniwersalne
- file_operations uniwersalna metoda write_decoding_ratio, write_bsc_noise_comparison: wpisuje albo do pliku z bitami albo bajtami i wybór kodu i kanału
- **w testing i file_operations i gec nic związanego z kanałem gilberta nie zmieniałem**, więc trzeba pewnie będzie poprawić parę rzeczy
## Plany
- bits_to_bytes i bytes_to_bits z klas **Transmitter i Satellite** dac do nowego common (unit_operations)
- Z zajęć **17.12.2024**
    - Testy transmisji z naszymi parametrami kanałów
    - Testy, które doprowadziły do wybrania tych parametrów (wybór BER)
    - Testy dla LDPC i RS
        - Jak wybrano symbole parzystości, czyli np dla RS:
        - 1 błąd do korekcji (2 symbole) nie ma sensu bo nic nie poprawi w złym kanale
        - x błędów dopasować tak, aby niemal każde błędy były poddane korekcji nawet w błędnym kanale
    -  W przeplocie dorobić zdjęcie GEC (jak STATE_LIST_Visualization), ale dla odwróconego przeplotu
    -  algorytm Viterbiego: może pomóc w kodach LDPC

## Użyte biblioteki:
- reedsolo
- PIL
- [...]

## Parametry
### Reeda-Solomona
- GF(2^8)
    - symbol: 8 bitów
    - n: 2^8-1 = 255
    - k = 249
    - 2t = 6 (3 bledy do korekcji)

## Do sprawka
- Coś na styl tego:
![image](https://github.com/user-attachments/assets/637026ba-04a4-4c2e-9930-0fcd72230b21)
