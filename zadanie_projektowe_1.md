# Zadanie projektowe 1: Automatyczny skaner bagaży na lotnisku

Twoim zadaniem jest zaprojektowanie od zera kompletnego oprogramowania wagi bagażowej na lotnisku. Program ma rejestrować wagi walizek pasażerów aż do zakończenia odprawy, oczyszczać dane z błędów pomiarowych, obliczać łączne obciążenie luku bagażowego oraz przydzielać odpowiednie strefy bagażowe.

## Zakres materiału

* Zmienne i operacje wejścia/wyjścia (`input()`, `print()`, f-stringi)
* Pętle `while` (pętla nieskończona `while True:` z `break` oraz pętla warunkowa `while ... in ...:`)
* Pętla `for` z bezpośrednią iteracją po elementach listy (`for element in lista:`)
* Instrukcje warunkowe `if / elif / else`
* Operacje na listach: tworzenie pustej listy `[]`, `.append()`, modyfikacja po indeksie `lista[0]`, `.count()`, `.remove()`, `.sort()`
* Wbudowane funkcje analityczne: `len()`, `sum()`, `max()`, `min()`

## Zadanie do wykonania

### Część 1: Ważenie bagaży w pętli `while`

1. Utwórz pustą listę o nazwie `walizki`.
2. Uruchom nieskończoną pętlę `while True:`, która w kółko pyta obsługę o wagę kolejnej walizki w kilogramach (liczba całkowita `int`).
3. **Warunek zakończenia odprawy:** Jeśli użytkownik wpisze `-1`, przerwij pętlę instrukcją `break` (**nie dodawaj `-1` do listy!**).
4. Każdą inną podaną wartość (w tym `0` – oznaczające pusty przejazd taśmy) dodawaj na koniec listy `walizki` za pomocą metody `.append()`.
5. Po zakończeniu pętli wyświetl listę wszystkich zarejestrowanych odczytów.

### Część 2: Korekta wagi i czyszczenie pustych przejazdów
1. **Tarowanie wagi:** Okazało się, że pierwszy pomiar (indeks `0`) był zakłócony – nadpisz wagę pierwszej walizki bezpośrednio w liście na `15` kg (pamiętaj o sprawdzeniu, czy lista nie jest pusta).
2. **Wykrywanie pustych przejazdów:** Sprawdź za pomocą metody `.count()`, ile razy w liście pojawiła się wartość `0` (pusty przejazd taśmy) i wypisz ten komunikat na ekran.
3. **Usuwanie wszystkich zer pętlą `while`:** Używając pętli `while 0 in walizki:`, usuwaj wszystkie wystąpienia wartości `0` za pomocą metody `.remove(0)`.
4. Posortuj listę `walizki` od najlżejszej do najcięższej (`.sort()`), a następnie wyświetl oczyszczoną i uporządkowaną listę.

### Część 3: Raport załadunkowy i decyzja odprawy
1. Oblicz i wypisz podsumowanie załadunku (wykorzystaj funkcje `len()`, `sum()`, `max()`, `min()`):
   * Liczbę wszystkich zatwierdzonych walizek,
   * Łączną wagę całego luku bagażowego,
   * Najcięższą walizkę,
   * Najlżejszą walizkę,
   * Średnią wagę jednego bagażu (zaokrągloną do 1 miejsca po przecinku).
2. Używając bezpośredniej pętli `for waga in walizki:`, przejdź przez każdą sztukę bagażu i wypisz decyzję odprawy:
   * Powyżej `23 kg` $\rightarrow$ `Waga X kg -> [NADBAGAŻ - WYMAGANA DOPŁATA]`
   * Od `10 kg` do `23 kg` $\rightarrow$ `Waga X kg -> [BAGAŻ REJESTROWANY - OK]`
   * Poniżej `10 kg` $\rightarrow$ `Waga X kg -> [BAGAŻ PODRĘCZNY - DO KABINY]`

### Część 4: Dopłata za nadbagaż
Dodaj w części 3 zmienną licznikową (np. `liczba_nadbagazy = 0`), która podczas przeglądania listy w pętli `for` policzy, ile walizek waży powyżej `23 kg`. Na samym końcu programu wypisz komunikat:  
`Liczba walizek wymagających dopłaty za nadbagaż: [wynik]`.


## Przykładowy przebieg działania programu w konsoli

```text
=== AUTOMATYCZNY SKANER BAGAŻY NA LOTNISKU ===
Wprowadzaj wagi walizek [kg]. Wpisz -1, aby zakończyć odprawę.

Podaj wagę walizki [kg] (-1 kończy): 22
Podaj wagę walizki [kg] (-1 kończy): 0
Podaj wagę walizki [kg] (-1 kończy): 28
Podaj wagę walizki [kg] (-1 kończy): 8
Podaj wagę walizki [kg] (-1 kończy): 0
Podaj wagę walizki [kg] (-1 kończy): 19
Podaj wagę walizki [kg] (-1 kończy): -1

==================================================
Surowe odczyty z taśmy bagażowej: [22, 0, 28, 8, 0, 19]
==================================================
Wykryto pustych przejazdów taśmy (0 kg): 2
Oczyszczona i posortowana lista bagaży: [8, 15, 19, 28]

--- RAPORT OBCIĄŻENIA LUKU BAGAŻOWEGO ---
Zatwierdzone walizki:  4 szt.
Łączna waga ładunku:   70 kg
Najcięższa walizka:    28 kg
Najlżejsza walizka:    8 kg
Średnia waga bagażu:   17.5 kg

--- DECYZJA ODPRAWY BAGAŻOWEJ ---
Waga  8 kg -> [BAGAŻ PODRĘCZNY - DO KABINY]
Waga 15 kg -> [BAGAŻ REJESTROWANY - OK]
Waga 19 kg -> [BAGAŻ REJESTROWANY - OK]
Waga 28 kg -> [NADBAGAŻ - WYMAGANA DOPŁATA]

Liczba walizek wymagających dopłaty za nadbagaż: 1
```