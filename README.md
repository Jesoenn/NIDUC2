# NIDUC2

Do zrobienia </br>
GEC -> probabilistycznie a nie hardcode </br>
Testy -> to samo co wczesniej + bez przeplotu i z przeplotem + pisac ile bitow w kanale dobrym, ile w zlym </br>

ZROBIONE 02.12: </br>
Main -> korekta zeby testy bardziej czytelne byly moze </br>
Transmitter -> aby za parametr jakies metody okreslic czy chce robic z przeplotem czy bez </br>
*Do testów, w mainie, itd. pobierac dane po prostu z klasy, czyli zrobic tak zeby wszystko mozna bylo po prostu "wyjac z klas"* </br>
Satellite -> Tak samo zrobic zeby okreslic czy przesylamy przeplot czy bez, wiekszosc automatycznie </br>


# Stare
Transmitter -> dodanie pare zmiennych w klasie ktore mozna wykorzystac do testow jakis<br/> 
Dodalem satelite -> obior, dekodowanie i tworzenie zdjecia<br/>
testing, file_operations -> zbieranie danych z symulacji, moze do poprawy, nwm<br/>
image_operations -> zmiana pobierania calego skompresowanego zdjecia (png, 49kB na razie) na uzycie biblioteki PIL i pobranie tylko pixeli. Przez to z 3 razy wiecej bajtow danych (R,G,B), ale mozna fajnie zwizualizowac szum na zdjeciach<br/>

Dekodowanie: Na razie jak nie da sie zdekodowac jakiegos bloku (za duzo bledow) to po prostu jest zostawiany taki.<br/>
Rozmiar zdjecia w pixelach jest przechowywany jako zmienna, nie przesylany z cala reszta, nie wiem czy tez to symulowac. Bo jezeli zakloci sie rozmiar w pixelach to zdjecie sie nie stworzy i nie bedzie widac szumu<br/>


Znalazlem ze GF(2^8), wiec dalem rozumiem to tak, ze:<br/>
 kazda "litera" ma 8 bitow, czyli daje to bajt <br/>
 maksymalna liczba slow 2^8-1 = 255<br/>
 dalem slowa wejsciowe 249 i kodowe 6 (3 bledy do poprawy)<br/>



Jeszcze nie dodalem komentarzy, beda<br/>
Skrypty nie sa pogrupowane do pakietow na razie, bo robie wszystko na spontanie<br/>
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> c84b9d76a718f7dc7ecbb128c42c379bb5298584


Użyte biblieki zewnetrzne: <br/>
 PIL <br/>
 reedsolo <br/>
 moze cos jeszcze nie pamietam i potem zobacze <br/>
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> c84b9d76a718f7dc7ecbb128c42c379bb5298584
