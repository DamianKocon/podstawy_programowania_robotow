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
print("=== KALKULATOR DO OBLICZANIA MOCY REZYSTORÓW ===")
print("Wprowadź dane techniczne komponentów:\n")

# ==============================================================================
# KROK 1: POBIERANIE DANYCH WEJŚCIOWYCH
# Pamiętaj: input() zawsze pobiera TEKST (str).
# Używamy float(), aby zamienić tekst na LICZBĘ ZMIENNOPRZECINKOWĄ (float).
# Uwaga: Ułamki w Pythonie wpisujemy z KROPKĄ (np. 11.1), a nie z przecinkiem!
# ==============================================================================

# PRZYKŁAD:
napiecie_v = float(input("Podaj napięcie na rezystorze [V]: "))

# ZADANIE 1: Pobierz prąd płynący przez rezystor [mA]
prad_mA = <uzupelnij>

# ==============================================================================
# KROK 2: OBLICZENIA INŻYNIERYJNE
# ==============================================================================

# PRZYKŁAD: Konwersja pprądu z mA na A (1 A = 1000 mA)
prad_A = prad_mA / 1000

# ZADANIE 2: Oblicz moc na rezystorze w Watach [W] (Wzór: P = U * I)
moc_wat = <uzupelnij>

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

# ZADANIE 3: Wyświetl moc w W (zaokrągloną do 2 miejsc: :.2f)
print(f"Moc na rezystorze:  {<uzupelnij>:.1f} W")

print("=" * 40)
```
