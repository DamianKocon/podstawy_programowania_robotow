print("=== SPRAWDZIAN SPORTOWY: BIEG NA 100 METRÓW ===")
print("Elektroniczny pomiar i klasyfikacja wyników na mecie [sekundy]\n")

# ==============================================================================
# KROK 1: POWTÓRKA - REJESTRACJA CZASÓW W PĘTLI FOR (.append())
# ==============================================================================
czasy_biegu = []

for numer_zawodnika in range(1, 5):
    t = float(input(f"Podaj czas zawodnika #{numer_zawodnika} [s]: "))
    czasy_biegu.append(t)

print("\n" + "=" * 55)
print(f"Zarejestrowane czasy w kolejności startu: {czasy_biegu}")
print("=" * 55)


# ==============================================================================
# KROK 2: NOWOŚĆ - TWORZENIE PODIUM ZAWODÓW (.sort() i .reverse())
# ==============================================================================
# Sortowanie rosnąco: najkrótszy czas (najlepszy biegacz) trafia na indeks [0]
czasy_biegu.sort()
print(f"Klasyfikacja medalowa (od złota do najsłabszego): {czasy_biegu}")

# Odwrócenie listy: czasy malejąco (najwolniejszy na początku)
czasy_biegu.reverse()
print(f"Kolejność odwrócona (od najwolniejszego biegacza): {czasy_biegu}")


# ==============================================================================
# KROK 3: BILANS BIEGU (min, max, sum, len)
# ==============================================================================
rekord_biegu = min(czasy_biegu)
najslabszy_czas = max(czasy_biegu)
sredni_czas = sum(czasy_biegu) / len(czasy_biegu)

print("\n--- PROTOKÓŁ ZAWODÓW ---")
print(f"Złoty medal (rekord biegu):    {rekord_biegu:.2f} s")
print(f"Najsłabszy czas w serii:       {najslabszy_czas:.2f} s")
print(f"Średni czas całej grupy:       {sredni_czas:.2f} s")
