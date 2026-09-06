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
Skopiuj poniższy kod do edytora Thonny i zamień `<uzupełnij>` na właściwy kod programu.
```python
print("=== KALKULATOR DO OBLICZANIA KOSZTU ENERGII ELEKTRYCZNEJ ===")
print("Wprowadź dane techniczne:\n")

# ==============================================================================
# KROK 1: POBIERANIE DANYCH WEJŚCIOWYCH
# Pamiętaj: input() zawsze pobiera TEKST (str).
# Używamy float(), aby zamienić tekst na LICZBĘ ZMIENNOPRZECINKOWĄ (float).
# Uwaga: Ułamki w Pythonie wpisujemy z KROPKĄ (np. 11.1), a nie z przecinkiem!
# ==============================================================================

# PRZYKŁAD:
napiecie_v = float(input("Podaj napięcie na urządzeniu [V]: "))

# ZADANIE 1A: Pobierz prąd płynący przez urządzenie [A]
prad_A = <uzupełnij>

# ZADANIE 1B: Pobierz czas pracy urządzenia [min]
czas_min = <uzupełnij>

# ==============================================================================
# KROK 2: OBLICZENIA INŻYNIERYJNE
# ==============================================================================

# PRZYKŁAD: Konwersja czasu z minut na godziny (1 h = 60 min)
czas_h = czas_min / 60

# ZADANIE 2A: Oblicz moc na urządzeniu w Watach [W] (Wzór: P = U * I)
moc_wat = <uzupełnij>

# ZADANIE 2B: Zamień waty na kilowaty (1 kW = 1000 W)
moc_kwat = <uzupełnij>

# ZADANIE 2C: Oblicz pracę prądu elektrycznego w kWh (Wzór: W = P * t)
praca_kwath = <uzupełnij>

# ZADANIE 2D: Oblicz koszt energii elektrycznej pobieranej przez urządzenie (1 kWh = 0.6585 zł)
cena = <uzupełnij>
koszt_zl = <uzupełnij>

# ==============================================================================
# KROK 3: RAPORT WYJŚCIOWY (f-stringi)
# Uzupełnij nawiasy klamrowe {} odpowiednimi nazwami zmiennych.
# Symbol :.1f zaokrągla wynik do 1 miejsca po przecinku.
# Symbol :.0f wyświetla pełną liczbę całkowitą bez ułamka.
# ==============================================================================

print("\n" + "=" * 40)
print("       RAPORT KOSZTÓW PRACY URZĄDZENIA     ")
print("=" * 40)

# PRZYKŁAD:
print(f"Napięcie zasilania: {napiecie_v:.1f} V")

# ZADANIE 3A: Wyświetl koszt energii elektrycznej w zł (zaokrąglony do 2 miejsc: :.2f)
print(f"Koszt energii elektrycznej:  {<uzupełnij>:.2f} zł")

print("=" * 40)
```
