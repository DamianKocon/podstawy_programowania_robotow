# Wprowadzenie do Pythona, środowisko Thonny IDE, zmienne oraz kalkulator zasilania

## Konfiguracja środowiska

1. Zainstaluj lub/i uruchom program [Thonny](https://thonny.org/). Przy pierwszym uruchomieniu wybierz standardowy układ (Language: polski, Initial settings: Standard).
2. Włącz podgląd zmiennych: z menu górnego wybierz `Podgląd` → `Zmienne`.
3. Utwórz folder w którym będziesz przechowywać skrypty pythona np. `ppr`, w Thonny w edytorze wpisz:
```python
print("Hello World!")
```
i zapisz we wcześniej stworzonym katalogu jako `test.py`. Kliknij zielony przycisk ze strzałką ("Uruchom") na górnym pasku lub naciśnij klawisz F5.

## Pierwszy program

```python
print("=== KALKULATOR ZASILANIA ROBOTA MOBILNEGO ===")
print("Wprowadź dane techniczne komponentów:\n")

# ==============================================================================
# KROK 1: POBIERANIE DANYCH WEJŚCIOWYCH
# Pamiętaj: input() zawsze pobiera TEKST (str).
# Używamy float(), aby zamienić tekst na LICZBĘ ZMIENNOPRZECINKOWĄ (float).
# Uwaga: Ułamki w Pythonie wpisujemy z KROPKĄ (np. 11.1), a nie z przecinkiem!
# ==============================================================================

# PRZYKŁAD:
napiecie_v = float(input("Podaj napięcie akumulatora [V]: "))

# ZADANIE 1A: Pobierz pojemność akumulatora w miliamperogodzinach [mAh]
pojemnosc_mah = <uzupełnij>

# ZADANIE 1B: Pobierz szacowany pobór prądu przez silniki w Amperach [A]
pobor_pradu_a = <uzupełnij>


# ==============================================================================
# KROK 2: OBLICZENIA INŻYNIERYJNE
# ==============================================================================

# PRZYKŁAD: Konwersja pojemności z mAh na Ah (1 Ah = 1000 mAh)
pojemnosc_ah = pojemnosc_mah / 1000

# ZADANIE 2A: Oblicz moc znamionową układu w Watach [W] (Wzór: P = U * I)
moc_wat = <uzupełnij>

# ZADANIE 2B: Oblicz czas pracy na baterii w godzinach (Wzór: Czas_h = Pojemność_Ah / Prąd_A)
czas_pracy_h = <uzupełnij>

# ZADANIE 2C: Przelicz czas pracy z godzin na minuty (Przemnóż czas w godzinach przez 60)
czas_pracy_min = <uzupełnij>


# ==============================================================================
# KROK 3: RAPORT WYJŚCIOWY (f-stringi)
# Uzupełnij nawiasy klamrowe {} odpowiednimi nazwami zmiennych.
# Symbol :.1f zaokrągla wynik do 1 miejsca po przecinku.
# Symbol :.0f wyświetla pełną liczbę całkowitą bez ułamka.
# ==============================================================================

print("\n" + "=" * 40)
print("       RAPORT DIAGNOSTYCZNY ZASILANIA     ")
print("=" * 40)

# PRZYKŁAD:
print(f"Napięcie zasilania: {napiecie_v:.1f} V")

# ZADANIE 3A: Wyświetl pojemność w Ah (zaokrągloną do 2 miejsc: :.2f) oraz mAh (:.0f)
print(f"Pojemność baterii:  {<uzupełnij>:.2f} Ah ({<uzupełnij>:.0f} mAh)")

# ZADANIE 3B: Wyświetl moc w Watach (zaokrągloną do 1 miejsca: :.1f)
print(f"Moc znamionowa:     {<uzupełnij>:.1f} W")

# ZADANIE 3C: Wyświetl czas pracy w minutach (:.0f) oraz godzinach (:.2f)
print(f"Szacowany czas:     {<uzupełnij>:.0f} minut ({<uzupełnij>:.2f} h)")

print("=" * 40)
```
