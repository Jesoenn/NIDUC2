# NIDUC2

nie wiem czy excel bedzie interpretowac kropki w csv - przetestowac




Transmitter -> dodanie pare zmiennych w klasie ktore mozna wykorzystac do testow jakis
Dodalem satelite -> obior, dekodowanie i tworzenie zdjecia
testing, file_operations -> zbieranie danych z symulacji, moze do poprawy, nwm
image_operations -> zmiana pobierania calego skompresowanego zdjecia (png, 49kB na razie) na uzycie biblioteki PIL i pobranie tylko pixeli. Przez to z 3 razy wiecej bajtow danych (R,G,B), ale mozna fajnie zwizualizowac szum na zdjeciach

Dekodowanie: Na razie jak nie da sie zdekodowac jakiegos bloku (za duzo bledow) to po prostu jest zostawiany taki.
Rozmiar zdjecia w pixelach jest przechowywany jako zmienna, nie przesylany z cala reszta, nie wiem czy tez to symulowac. Bo jezeli zakloci sie rozmiar w pixelach to zdjecie sie nie stworzy i nie bedzie widac szumu
Znalazlem ze GF(2^8), wiec dalem rozumiem to tak, ze:
 kazda "litera" ma 8 bitow, czyli daje to bajt 
 maksymalna liczba slow 2^8-1 = 255
 dalem slowa wejsciowe 249 i kodowe 6 (3 bledy do poprawy)



Jeszcze nie dodalem komentarzy, beda
