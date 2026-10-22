# Pętla while, break, cykl główny

## Nowe elementy języka

* pętla for
* funkcja `range`
* funkcja `time.sleep`

## Start drona

Uruchom poniższy kod w edytorze Thonny.

```python
import time  # Biblioteka do obsługi opóźnień czasowych (pauz)

print("=== SYSTEM DIAGNOSTYKI PRZEDSTARTOWEJ DRONA ===")
print("Rozpoczynanie rutynowej procedury sprawdzania 5 systemów...\n")

komenda = input("Wpisz 'TEST', aby rozpocząć procedurę: ").strip().upper()

if komenda == "TEST":
    print("\n[SYSTEM] Rozpoczynam diagnostykę systemów pokładowych...")
    print("=" * 50)
    
    # ZADANIE 1: Uzupełnij funkcję range(start, stop), aby policzyć od 1 do 5
    # Pamiętaj: druga wartość (stop) musi być o 1 większa niż docelowa liczba!
    for krok in range(<uzupełnij>, <uzupełnij>):
        print(f"  [TEST {krok}/5] Sprawdzanie czujnika nr {krok}... STATUS: OK")
        
        # Wstrzymanie programu na 1 sekundę
        time.sleep(1)
        
    print("=" * 50)
    print("STATUS: [100%] Wszystkie 5 systemów sprawne!")
    print("AKCJA:  DRON GOTOWY DO STARTU!")

else:
    print("\n[BŁĄD] Przerwano procedurę. Wprowadzono nieznaną komendę.")
```
