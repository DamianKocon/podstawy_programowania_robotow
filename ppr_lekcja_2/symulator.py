print("=== SYMULATOR CZUJNIKA ODLEGŁOŚCI ===")
print("System reakcji robota na przeszkodę\n")

# ==============================================================================
# KROK 1: POBIERANIE DANYCH
# Pamiętaj: input() pobiera tekst (str).
# float() zamienia tekst na liczbę ułamkową (np. 12.5).
# ==============================================================================

# Pobieramy odległość od przeszkody w centymetrach [cm]
odleglosc_cm = float(input("Podaj odległośc od przeszkody [cm]: "))

# ==============================================================================
# KROK 2: FLAGI LOGICZNE (Typ bool)
# Zmienna typu bool przechowuje tylko wartość True (Prawda) lub False (Fałsz).
# Wynik porównania (<, >, <=, >=, ==) tworzy wartość bool.
# ==============================================================================

# Tworzymy zmienną bool 'strefa_czerwnona'.
# Zwróci True, jeśli odległość jest mniejsza niż 10 cm.
strefa_czerwona = odleglosc_cm < 10

# Tworzymy zmienną bool 'strefa_zolta'.
# Zwróci True, jeśli odległość jest mniejsza bądź równa 30 cm.
strefa_zolta = odleglosc_cm <= 30

# ==============================================================================
# KROK 3: LOGIKA DECYZYJNA (if / elif / else)
# ==============================================================================

print("\n" + "=" * 40)

# Sprawdzamy w jakiej jesteśmy strefie i wyświetlamy odpowiedni komunikat
if strefa_czerwona:
    print("[ALARM] jesteś bardzo blisko przeszkody")

elif strefa_zolta:
    print("[UWAGA] wszedłeś do strefy kolizyjnej")
    
else:
    print("[INFO] Droga wolna, jesteś w strefie bezpiecznej")

print("=" * 40)