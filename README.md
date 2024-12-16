# NIDUC2
## Rzeczy do zrobienia

### Lista 16.12.2024
- Podzielić kod na pakiety jak w Javie.
- Pozmieniać nazwy plików, aby wpasować to do modelu:

![image](https://github.com/user-attachments/assets/24888e81-2186-472e-ac65-22720aa2b23f)

### Pytania na 17.12
- Przeplot robiony jest na całych danych z pliku, czy tak może być?
- Czy przeplot ma być po zakodowaniu (DVB)? <br/>
- **EPORTAL:** `Symulacyjna ocena skuteczności transmisji dla różnych parametrów kanałów (model i parametry błędów) i różnych sposobów transmisji.`
    - Czy mamy przetestować różne ilości np. bitów parzystości dla Reeda-Salomona i wybrać najlepsze, albo wywnioskować coś?
    - Czy modyfikować prawdopodobieństwo błędów i jakoś wizualizować?

## Plany

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
