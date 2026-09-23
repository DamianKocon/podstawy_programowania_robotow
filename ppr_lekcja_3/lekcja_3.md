# Pętla while, break, cykl główny

## Nowe elementy języka

* import
* funkcja `random.randint`
* pętla while
* zaprzeczenie logiczne not
* przerwanie pętli przez break

## Zgadnij liczbę

Uruchom poniższy kod w edytorze Thonny.

```python
import random  # Biblioteka do generowania liczb losowych

print("=== GRA: ZGADNIJ LICZBĘ STEROWNIKA ===")
print("Komputer wosował liczbę od 1 do 10. Spróbuj ją odgadnąć!\n")

# ==============================================================================
# KROK 1: INICJALIZACJA ZMIENNYCH
# - random.randint(1, 10) losuje liczbę całkowitą (int) z przedziału <1, 10>
# - licznik_prob (int) zlicza, ile podejść wykonał uczeń
# - czy_zgadnal (bool) to flaga sterująca pętlą while
# ==============================================================================

tajna_liczba = random.randint(1, 10)

# ZADANIE 1: Ustaw początkową wartość licznika prób na 0 (typ int)
licznik_prob = <uzupełnij>

# Flaga logiczna (bool) – na początku False, bo użytkownik jeszcze nie zgadł
czy_zgadnal = False


# ==============================================================================
# KROK 2: PĘTLA WHILE (Działa tak długo, jak czy_zgadnal wynosi False)
# ==============================================================================

# Pętla wykonuje się, dopóki NIE zgadniesz (not czy_zgadnal)
while not czy_zgadnal:
    
    # Pobieramy strzał użytkownika i zamieniamy na liczbę całkowitą (int)
    strzal = int(input("Podaj swoją liczbę (1-10): "))
    
    # ZADANIE 2: Zwiększ licznik prób o 1 przy każdym podejściu (inkrementacja)
    licznik_prob = <uzupełnij>
    
    # ZADANIE 3: Sprawdź warunki wygranej / podpowiedzi
    if strzal == tajna_liczba:
        print(f"\n[BRAWO!] Trafiłeś! Tajna liczba to rzeczywiście {tajna_liczba}.")
        # Zmień flagę na True, co spowoduje zakończenie pętli while
        czy_zgadnal = <uzupełnij>
        
    elif strzal < tajna_liczba:
        print("[PODPOWIEDŹ] Za mało! Spróbuj większej liczby.")
        
    else:
        print("[PODPOWIEDŹ] Za dużo! Spróbuj mniejszej liczby.")


# ==============================================================================
# KROK 3: PODSUMOWANIE (Wykonuje się po wyjściu z pętli)
# ==============================================================================
print("\n" + "=" * 40)
print(f"KONIEC GRY! Odgadłeś liczbę za {licznik_prob} razem.")
print("=" * 40)
```

### Break

Przekształć wcześniejszy kod z wykorzystaniem słowa kluczowego `break`.

```python
import random  # Biblioteka do losowania liczb

print("=== GRA: ZGADNIJ LICZBĘ STEROWNIKA (Wersja z BREAK) ===")
print("Komputer wylosował liczbę od 1 do 10. Spróbuj ją odgadnąć!\n")

# ==============================================================================
# KROK 1: LOSOWANIE I INICJALIZACJA LICZNIKA (int)
# ==============================================================================

# Losujemy liczbę całkowitą (int) z zakresu 1 do 10
tajna_liczba = random.randint(1, 10)

# ZADANIE 1: Zapisz początkową wartość licznika prób (typ int, zaczynamy od 0)
licznik_prob = <uzupełnij>


# ==============================================================================
# KROK 2: PĘTLA GŁÓWNA (while True - pętla działająca bez końca)
# Wyjście z pętli nastąpi TYLKO po wykonaniu instrukcji break!
# ==============================================================================

while True:
    # Pobieramy propozycję użytkownika i konwertujemy na liczbę całkowitą (int)
    strzal = int(input("Podaj swoją liczbę (1-10): "))
    
    # ZADANIE 2: Zwiększ licznik prób o 1 przy każdym podejściu (inkrementacja)
    licznik_prob = <uzupełnij>
    
    # ZADANIE 3: Logika sprawdzania wyniku
    if strzal == tajna_liczba:
        print(f"\n[BRAWO!] Trafiłeś! Tajna liczba to rzeczywiście {tajna_liczba}.")
        print("AKCJA: Wykonuję polecenie break, aby natychmiast opuścić pętlę<uzupełnij>")
        
        # Użyj odpowiedniego słowa kluczowego do natychmiastowego przerwania pętli
        <uzupełnij>
        
    elif strzal < tajna_liczba:
        print("[PODPOWIEDŹ] Za mało! Spróbuj większej liczby.\n")
        
    else:
        print("[PODPOWIEDŹ] Za dużo! Spróbuj mniejszej liczby.\n")


# ==============================================================================
# KROK 3: PODSUMOWANIE (Kod poniżej pętli wykonuje się po instrukcji break)
# ==============================================================================

print("\n" + "=" * 40)
print(f"KONIEC GRY! Odgadłeś liczbę za {licznik_prob} razem.")
print("=" * 40)
```
