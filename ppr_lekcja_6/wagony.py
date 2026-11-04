print("=== POKŁADOWY SYSTEM POMIARU LICZBY PASAŻERÓW ===")
print("Weryfikacja obciążenia składu przed odjazdem ze stacji\n")

# Z góry zarejestrowana liczba pasażerów w 5 kolejnych wagonach
pasazerowie_w_wagonach = [45, 120, 110, 30, 95]

print(f"Liczba pasażerów w wagonach: {pasazerowie_w_wagonach}\n")
print("--- RAPORT KONTROLI BEZPIECZEŃSTWA (LIMIT: 100 OSÓB) ---")

# ==============================================================================
# KROK 1: BEZPOŚREDNIA ITERACJA PO ELEMENTACH LISTY
# ZADANIE 1: Uzupełnij pętlę for, aby przeszła po liście 'pasazerowie_w_wagonach'
# Składnia: for zmienna in nazwa_listy:
# ==============================================================================
for liczba_osob in pasazerowie_w_wagonach:
    
    # ==========================================================================
    # KROK 2: WERYFIKACJA LIMITU PASAŻERÓW
    # Maksymalna bezpieczna pojemność wagonu to 100 osób.
    # ZADANIE 2: Sprawdź, czy liczba osób przekracza limit (> 100)
    # ==========================================================================
    if liczba_osob > 100:
        print(f"Wagon mieści {liczba_osob:3d} pasażerów -> [ALARM: PRZEPEŁNIENIE!]")
    else:
        print(f"Wagon mieści {liczba_osob:3d} pasażerów -> [STATUS: W NORMIE]")

print("\n[SYSTEM] Kontrola składu zakończona. Drzwi zablokowane.")
