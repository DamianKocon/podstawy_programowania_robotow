# Anatomia listy – indeksy, modyfikacja i przeglądanie pętlą for

## Nowe elementy języka

* indeksy list (od zera `dane[0]`, `dane[1]`, `dane[-1]`)
* nadpisywanie wartości `dane[0] = nowa_wartosc`
* dodawanie pod konkretny indeks `dane.insert(indeks, wartosc)`
* usuwanie z indeksu: `del dane[indeks]` oraz `dane.pop()`
* przeglądanie listy przy pomocy pętli for (`for element in dane`)

## Stacje metra

Uruchom poniższy kod w edytorze Thonny.

```python
print("Aktualizacja rozkładu stacji metra w pamięci pokładowej pociągu\n")

# Lista kolejnych stacji na planowanej trasie
# Pamiętaj, że pierwszy element listy ma indeks 0, kolejny 1, itd.
stacje = ["Centrum", "Dworzec Główny", "Remontowana Stacja", "Politechnika"]

print(f"Początkowy plan trasy: {stacje}")

# ==============================================================================
# KROK 1: POBRANIE NAZWY PIERWSZEJ STACJI
# ZADANIE 1: Odczytaj stację pod indeksem 0 do zmiennej 'stacja_startowa'
# ==============================================================================
stacja_startowa = stacje[<uzupelnij>]
print(f"Pociąg rozpoczyna kurs ze stacji: {stacja_startowa}")

# ==============================================================================
# KROK 2: PODMIANA STACJI WYŁĄCZONEJ Z RUCHU (Nadpisywanie)
# Stacja pod indeksem 2 jest zamknięta z powodu prac torowych.
# Pociąg pojedzie objazdem przez stację "Objazd - Stadion".
# ZADANIE 2: Nadpisz element pod indeksem 2 tekstem "Objazd - Stadion"
# ==============================================================================
stacje[<uzupelnij>] = "Objazd - Stadion"
print(f"Po wyznaczeniu objazdu na pozycji 2: {stacje}")

# ==============================================================================
# KROK 3: DODANIE NOWEJ STACJI POCZĄTKOWEJ (.insert)
# Kurs zostaje wydłużony – pociąg wyruszy z bazy technicznej "Zajezdnia" (indeks 0).
# ZADANIE 3: Użyj metody .insert(indeks, wartosc), aby wstawić "Zajezdnia" na indeks 0
# ==============================================================================
stacje.insert(<uzupelnij>, <uzupelnij>)
print(f"Po dodaniu stacji początkowej na pozycję 0: {stacje}")

# ==============================================================================
# KROK 4: SKRÓCENIE TRASY O OSTATNIĄ STACJĘ (.pop)
# Ostatnia stacja została tymczasowo odcięta od zasilania trakcji.
# ZADANIE 4: Usuń ostatnią stację z listy za pomocą metody .pop()
# ==============================================================================
stacje.pop()
print(f"Końcowy, zatwierdzony plan trasy: {stacje}")
```

## System pomiaru liczby pasażerów

Uruchom poniższy kod w edytorze Thonny.

```python
print("=== POKŁADOWY SYSTEM POMIARU LICZBY PASAŻERÓW ===")
print("Weryfikacja obciążenia składu przed odjazdem ze stacji\n")

# Z góry zarejestrowana liczba pasażerów w 5 kolejnych wagonach
pasazerowie_w_wagonach = [45, 120, 110, 30, 95]

print(f"Liczba pasażerów w wagonach: {pasazerowie_w_wagonach}\n")
print("--- RAPORT KONTROLI BEZPIECZEŃSTWA (LIMIT: 100 OSÓB) ---")

# ==============================================================================
# KROK 1: BEZPOŚREDNIA ITERACJA PO ELEMENTACH LISTY
# ZADANIE 1: Uzupełnij pętlę for, aby przeszła po liście 'pasazerowie_w_wagonach'
# Składnia: for zmienna in nazwa_listy:
# ==============================================================================
for liczba_osob in <uzupełnij>:
    
    # ==========================================================================
    # KROK 2: WERYFIKACJA LIMITU PASAŻERÓW
    # Maksymalna bezpieczna pojemność wagonu to 100 osób.
    # ZADANIE 2: Sprawdź, czy liczba osób przekracza limit (> 100)
    # ==========================================================================
    if liczba_osob > <uzupełnij>:
        print(f"Wagon mieści {liczba_osob:3d} pasażerów -> [ALARM: PRZEPEŁNIENIE!]")
    else:
        print(f"Wagon mieści {liczba_osob:3d} pasażerów -> [STATUS: W NORMIE]")

print("\n[SYSTEM] Kontrola składu zakończona. Drzwi zablokowane.")
```
