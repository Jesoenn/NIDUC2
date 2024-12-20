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

## Plany
- Uniwersalnosc skryptow:
    - transmitterowi trzeba podaj rozmiary blokow bajtowych **[NA LAPKU ZROBIONE, DO PRZESŁANIA]**
    - transmitterowi trzeba napisac czy przeplot czy bez **[NA LAPKU ZROBIONE, DO PRZESŁANIA]**
    - uniwersalny przeplot -> bez hardcodowanego rozmiaru bloku!! **[NA LAPKU ZROBIONE, DO PRZESŁANIA]**
    - Do kanalow BSC i GEC dodac enumy jako konstruktory klasy
    - zapis plikow dac do skryptow testujacych, a nie ***testing.py*** 
    - Zrobic skrypty testujące do których będzie sie odwolywac main
    - Bardziej uniwersalne file_operations: ja podaje nazwe pliku **(moze jako enum?)**
    - bits_to_bytes i bytes_to_bits z klas **Transmitter i Satellite** dac do nowego common
    - W satelicie okreslic jakie kodowanie jest robione -> **RS CZY LDPC TEZ JAKO ENUM** -> do decode
    - 
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
