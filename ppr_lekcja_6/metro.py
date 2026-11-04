print("Aktualizacja rozkładu stacji w pamięci pokładowej pociągu\n")

# Lista kolejnych stacji na planowanej trasie
# Pamiętaj, że pierwszy element listy ma indeks 0, kolejny 1, itd.
stacje = ["Centrum", "Dworzec Główny", "Remontowana Stacja", "Politechnika"]

print(f"Początkowy plan trasy: {stacje}")

# ==============================================================================
# KROK 1: POBRANIE NAZWY PIERWSZEJ STACJI
# ZADANIE 1: Odczytaj stację pod indeksem 0 do zmiennej 'stacja_startowa'
# ==============================================================================
stacja_startowa = stacje[0]
print(f"Pociąg rozpoczyna kurs ze stacji (indeks 0): {stacja_startowa}")

# ==============================================================================
# KROK 2: PODMIANA STACJI WYŁĄCZONEJ Z RUCHU (Nadpisywanie)
# Stacja pod indeksem 2 jest zamknięta z powodu prac torowych.
# Pociąg pojedzie objazdem przez stację "Objazd - Stadion".
# ZADANIE 2: Nadpisz element pod indeksem 2 tekstem "Objazd - Stadion"
# ==============================================================================
stacje[2] = "Objazd - Stadion"
print(f"Po wyznaczeniu objazdu na pozycji 2: {stacje}")

# ==============================================================================
# KROK 3: DODANIE NOWEJ STACJI POCZĄTKOWEJ (.insert)
# Kurs zostaje wydłużony – pociąg wyruszy z bazy technicznej "Zajezdnia" (indeks 0).
# ZADANIE 3: Użyj metody .insert(indeks, wartosc), aby wstawić "Zajezdnia" na indeks 0
# ==============================================================================
stacje.insert(0, "Zajezdnia")
print(f"Po dodaniu stacji początkowej na pozycję 0: {stacje}")

# ==============================================================================
# KROK 4: SKRÓCENIE TRASY O OSTATNIĄ STACJĘ (.pop)
# Ostatnia stacja została tymczasowo odcięta od zasilania trakcji.
# ZADANIE 4: Usuń ostatnią stację z listy za pomocą metody .pop()
# ==============================================================================
stacje.pop()
print(f"Końcowy, zatwierdzony plan trasy: {stacje}")
