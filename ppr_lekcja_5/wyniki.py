print("=== TABLICA WYNIKÓW MECZU (4 GRACZY) ===")

wyniki = []

# KROK 1:
for numer_gracza in range(1, 5):
    punkty = int(input(f"Podaj wynik gracza #{numer_gracza}: "))
    wyniki.append(punkty)

print("\n" + "=" * 40)
print(f"Wszystkie wyniki meczu: {wyniki}")
print("=" * 40)

# KROK 2:
najlepszy_gracz = max(wyniki)
najslabszy_gracz = min(wyniki)
srednia_meczu = sum(wyniki) / len(wyniki)

print(f"Rekord meczu:       {najlepszy_gracz} pkt")
print(f"Najniższy wynik:    {najslabszy_gracz} pkt")
print(f"Średnia na gracza:  {srednia_meczu:.1f} pkt")
