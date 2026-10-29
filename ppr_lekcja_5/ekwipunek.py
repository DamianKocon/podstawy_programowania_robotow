print("=== EKWIPUNEK GRACZA: HISTORIA ZDOBYTYCH MONET ===")

# KROK 1:
sakiewka = []

# KROK 2:
sakiewka.append(50)
sakiewka.append(120)
sakiewka.append(15)

print(f"\nZawartość Twojej sakiewki: {sakiewka}")

# KROK 3:
liczba_skrzynek = len(sakiewka)
najwiekszy_skarb = max(sakiewka)
najmniejszy_skarb = min(sakiewka)
suma_monet = sum(sakiewka)

print("\n--- RAPORT ZE SKARBÓW ---")
print(f"Otwarto skrzynek:    {liczba_skrzynek}")
print(f"Największy drop:     {najwiekszy_skarb} monet")
print(f"Najmniejszy drop:    {najmniejszy_skarb} monet")
print(f"Razem w sakiewce:    {suma_monet} monet")
