# NIDUC2
## Rzeczy do zrobienia

### Lista 16.12.2024
- Podzielić kod na pakiety jak w Javie. **[DONE]**
```
project/ 
│
├── model/
│   ├── BSC.py
│   ├── GilbertElliotChannel.py
│   ├── rs_coder.py
│   ├── LDPC.py
│
├── Transmission/
│   ├── transmitter.py
|   ├── satellite.py
│
├── utils/
│   ├── file_operations.py
│
├── visualization/
│   ├── image_operations (podzielić to na więcej plików dla czytelności)
|
├── output/
│   ├── zdjęcia
│   ├── pliki tekstowe
│
|── main.py
```
- Pozmieniać nazwy plików, aby wpasować to do modelu:

![image](https://github.com/user-attachments/assets/24888e81-2186-472e-ac65-22720aa2b23f)

### Pytania na 17.12
- Przeplot robiony jest na całych danych z pliku, czy tak może być? **TAK**
- Czy przeplot ma być po zakodowaniu (DVB)? <br/> **TAK**
- **EPORTAL:** `Symulacyjna ocena skuteczności transmisji dla różnych parametrów kanałów (model i parametry błędów) i różnych sposobów transmisji.`
    - Czy mamy przetestować różne ilości np. bitów parzystości dla Reeda-Salomona i wybrać najlepsze, albo wywnioskować coś?
    - Czy modyfikować prawdopodobieństwo błędów i jakoś wizualizować?
- Czy jakieś dodatkowe techniki zaimplementować? (np. modulacja)

## Plany
- Stworzenie różnych funkcji do testowania
    - 1 odpalenie GEC, BSC
    - Wielokrotne odpalenie z zapisem danych
    - [...]
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
