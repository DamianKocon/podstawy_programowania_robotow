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
prad_A = float(input("Podaj wartość prądu w A: "))

# ZADANIE 1B: Pobierz czas pracy urządzenia [min]
czas_min = float(input("Podaj czas pracy urządzenia w minutach: "))

# ==============================================================================
# KROK 2: OBLICZENIA INŻYNIERYJNE
# ==============================================================================

# PRZYKŁAD: Konwersja czasu z minut na godziny (1 h = 60 min)
czas_h = czas_min / 60

# ZADANIE 2A: Oblicz moc na urządzeniu w Watach [W] (Wzór: P = U * I)
moc_wat = napiecie_v * prad_A

# ZADANIE 2B: Zamień waty na kilowaty (1 kW = 1000 W)
moc_kwat = moc_wat / 1000

# ZADANIE 2C: Oblicz pracę prądu elektrycznego w kWh (Wzór: W = P * t)
praca_kwath = moc_kwat * czas_h

# ZADANIE 2D: Oblicz koszt energii elektrycznej pobieranej przez urządzenie (1 kWh = 0.6585 zł)
cena = 0.6585
koszt_zl = praca_kwath * cena

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
print(f"Koszt energii elektrycznej:  {koszt_zl:.2f} zł")

print("=" * 40)