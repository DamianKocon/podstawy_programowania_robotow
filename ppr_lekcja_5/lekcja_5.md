# Lista

## Nowe elementy języka

* lista
* metoda listy `append`
* funkcje `len()`, `max()`, `min()`, `sum()`

## Ekwipunek gracza

Uruchom poniższy kod w edytorze Thonny.

```python
print("=== EKWIPUNEK GRACZA: HISTORIA ZDOBYTYCH MONET ===")

# ==============================================================================
# KROK 1: PUSTA LISTA
# ZADANIE 1: Stwórz pustą listę o nazwie 'sakiewka' używając nawiasów []
# ==============================================================================
sakiewka = <uzupełnij>

# ==============================================================================
# KROK 2: DODAWANIE PRZEDMIOTÓW / MONET METODĄ .append()
# Bohater otwiera po kolei 3 skrzynki ze skarbami.
# ZADANIE 2: Dodaj liczby monet (50, 120, 15) do listy 'sakiewka'
# ==============================================================================
sakiewka.append(<uzupełnij>)
sakiewka.append(<uzupełnij>)
sakiewka.append(<uzupełnij>)

print(f"\nZawartość Twojej sakiewki: {sakiewka}")

# ==============================================================================
# KROK 3: STATYSTYKI Z WBUDOWANYCH FUNKCJI
# ZADANIE 3: Uzupełnij wbudowane funkcje: len(), max(), min(), sum()
# ==============================================================================

# Ile skrzynek otwarto? (długość listy)
liczba_skrzynek = len(<uzupełnij>)

# Największy znaleziony skarb
najwiekszy_skarb = max(<uzupełnij>)

# Najmniejszy znaleziony skarb
najmniejszy_skarb = min(<uzupełnij>)

# Łączna liczba zebranych monet
suma_monet = sum(<uzupełnij>)

print("\n--- RAPORT ZE SKARBÓW ---")
print(f"Otwarto skrzynek:    {liczba_skrzynek}")
print(f"Największy drop:     {najwiekszy_skarb} monet")
print(f"Najmniejszy drop:    {najmniejszy_skarb} monet")
print(f"Razem w sakiewce:    {suma_monet} monet")
```

## Tablica wyników meczu

Uruchom poniższy kod w edytorze Thonny.

```python
print("=== TABLICA WYNIKÓW MECZU (4 GRACZY) ===")

wyniki = []

# ==============================================================================
# KROK 1: PĘTLA FOR ZAPISUJĄCA WYNIKI DO LISTY
# ZADANIE 1: Ustaw range, aby pętla zapytała o graczy od 1 do 4
# ZADANIE 2: Dodaj wpisany 'punkty' do listy 'wyniki'
# ==============================================================================
for numer_gracza in range(<uzupełnij>, <uzupełnij>):
    punkty = int(input(f"Podaj wynik gracza #{numer_gracza}: "))
    
    # Dodaj wynik do listy:
    wyniki.append(<uzupełnij>)

print("\n" + "=" * 40)
print(f"Wszystkie wyniki meczu: {wyniki}")
print("=" * 40)

# ==============================================================================
# KROK 2: PODSUMOWANIE TURNIEJU
# ZADANIE 3: Wykorzystaj poznane w Zadaniu 1 funkcje max, min, sum, len
# ==============================================================================
najlepszy_gracz = max(<uzupełnij>)
najslabszy_gracz = min(<uzupełnij>)
srednia_meczu = sum(<uzupełnij>) / len(<uzupełnij>)

print(f"Rekord meczu:       {najlepszy_gracz} pkt")
print(f"Najniższy wynik:    {najslabszy_gracz} pkt")
print(f"Średnia na gracza:  {srednia_meczu:.1f} pkt")
```
