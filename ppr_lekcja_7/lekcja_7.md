# Zaawansowane przetwarzanie i metody list

## Nowe elementy języka

* metody listy `count`, `remove`, `clear`, `sort`, `reverse`

## Dziennik zasobnika geologicznego

Uruchom poniższy kod w edytorze Thonny.

```python
print("=== ŁAZIK MARSJAŃSKI: DZIENNIK ZASOBNIKA GEOLOGICZNEGO ===")
print("Zarządzanie zebranymi próbkami skał w kraterze\n")

# Początkowa zawartość zasobnika
probki = ["BAZALT", "KRZEMIEŃ", "PIRYT"]
print(f"Stan początkowy zasobnika: {probki}")

# ==============================================================================
# KROK 1: POWTÓRKA - ZBIERANIE NOWYCH PRÓBEK (.append())
# Ramię mechaniczne pobrało dwie kolejne próbki skał: "BAZALT" oraz "LÓD".
# ZADANIE 1: Dodaj obie próbki na koniec listy za pomocą metody .append()
# ==============================================================================
probki.append(<uzupelnij>)
probki.append(<uzupelnij>)

print(f"Zasobnik po zebraniu próbek: {probki}")


# ==============================================================================
# KROK 2: NOWOŚĆ - ZLICZANIE WYSTĄPIEŃ (.count())
# Centrum kontroli pyta, ile łącznie próbek bazaltu znajduje się w zasobniku.
# ZADANIE 2: Zlicz wystąpienia napisu "BAZALT" metodą .count()
# ==============================================================================
liczba_bazaltu = probki.<uzupelnij>("BAZALT")
print(f"Liczba próbek bazaltu w zasobniku: {liczba_bazaltu}")


# ==============================================================================
# KROK 3: NOWOŚĆ - USUWANIE PO NAZWIE (.remove())
# Próbka "LÓD" wyparowała w słońcu – usuwamy jej wpis z pamięci.
# ZADANIE 3: Usuń wartość "LÓD" z listy metodą .remove()
# ==============================================================================
probki.<uzupelnij>("LÓD")
print(f"Po usunięciu sublimowanego lodu:     {probki}")


# ==============================================================================
# KROK 4: RESET ZASOBNIKA (.clear())
# ZADANIE 4: Opróżnij listę do zera metodą .clear() po przekazaniu próbek do bazy
# ==============================================================================
probki.<uzupelnij>()
print(f"Zasobnik po zrzucie próbek:         {probki}")
```

## Bieg na 100 metrów

Uruchom poniższy kod w edytorze Thonny.

```python
print("=== SPRAWDZIAN SPORTOWY: BIEG NA 100 METRÓW ===")
print("Elektroniczny pomiar i klasyfikacja wyników na mecie [sekundy]\n")

# ==============================================================================
# KROK 1: POWTÓRKA - REJESTRACJA CZASÓW W PĘTLI FOR (.append())
# ZADANIE 1A: Utwórz pustą listę o nazwie 'czasy_biegu' (użyj nawiasów [])
# ZADANIE 1B: Ustaw pętlę range na 4 kolejnych zawodników (od 1 do 4)
# ZADANIE 1C: Dodaj odczytany czas 't' na koniec listy metodą .append()
# ==============================================================================
czasy_biegu = <uzupelnij>

for numer_zawodnika in range(<uzupelnij>, <uzupelnij>):
    t = float(input(f"Podaj czas zawodnika #{numer_zawodnika} [s]: "))
    
    # Dodaj wynik do listy:
    czasy_biegu.<uzupelnij>(<uzupelnij>)

print("\n" + "=" * 55)
print(f"Zarejestrowane czasy w kolejności startu: {czasy_biegu}")
print("=" * 55)


# ==============================================================================
# KROK 2: NOWOŚĆ - TWORZENIE PODIUM ZAWODÓW (.sort() i .reverse())
# UWAGA: W biegu WYGRYWA ten, kto ma NAJMNIEJSZY czas!
# ZADANIE 2A: Posortuj listę rosnąco (.sort()), aby mistrz był na początku
# ZADANIE 2B: Odwróć listę (.reverse()), aby zobaczyć kolejność od najwolniejszego
# ==============================================================================
czasy_biegu.<uzupelnij>()
print(f"Klasyfikacja medalowa (od złota do najsłabszego): {czasy_biegu}")

czasy_biegu.<uzupelnij>()
print(f"Kolejność odwrócona (od najwolniejszego biegacza): {czasy_biegu}")


# ==============================================================================
# KROK 3: BILANS BIEGU (min, max, sum, len)
# ZADANIE 3: Uzupełnij wbudowane funkcje wyliczające statystyki
# Pamiętaj: rekord to NAJMNIEJSZY czas (funkcja min)!
# ==============================================================================
rekord_biegu = min(<uzupelnij>)
najslabszy_czas = max(<uzupelnij>)
sredni_czas = sum(<uzupelnij>) / len(<uzupelnij>)

print("\n--- PROTOKÓŁ ZAWODÓW ---")
print(f"Złoty medal (rekord biegu):    {rekord_biegu:.2f} s")
print(f"Najsłabszy czas w serii:       {najslabszy_czas:.2f} s")
print(f"Średni czas całej grupy:       {sredni_czas:.2f} s")
```
