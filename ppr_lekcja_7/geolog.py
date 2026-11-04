print("=== ŁAZIK MARSJAŃSKI: DZIENNIK ZASOBNIKA GEOLOGICZNEGO ===")
print("Zarządzanie zebranymi próbkami skał w kraterze\n")

probki = ["BAZALT", "KRZEMIEŃ", "PIRYT"]
print(f"Stan początkowy zasobnika: {probki}")

# KROK 1: Powtórka .append()
probki.append("BAZALT")
probki.append("LÓD")
print(f"Zasobnik po zebraniu próbek: {probki}")

# KROK 2: .count()
liczba_bazaltu = probki.count("BAZALT")
print(f"Liczba próbek bazaltu w zasobniku: {liczba_bazaltu}")

# KROK 3: .remove()
probki.remove("LÓD")
print(f"Po usunięciu sublimowanego lodu:     {probki}")

# KROK 4: .clear()
probki.clear()
print(f"Zasobnik po zrzucie próbek:         {probki}")
