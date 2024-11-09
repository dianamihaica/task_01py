# Introducerea numărului de clienți pentru fiecare zi a săptămânii
luni = int(input("Numărul de clienți pentru luni: ") or 230)
marti = int(input("Numărul de clienți pentru marți: ") or 200)
miercuri = int(input("Numărul de clienți pentru miercuri: ") or 310)
joi = int(input("Numărul de clienți pentru joi: ") or 290)
vineri = int(input("Numărul de clienți pentru vineri: ") or 400)
sambata = int(input("Numărul de clienți pentru sâmbătă: ") or 150)
duminica = int(input("Numărul de clienți pentru duminică: ") or 180)

# Calcularea numărului total de clienți pentru întreaga săptămână
total_saptamana = luni + marti + miercuri + joi + vineri + sambata + duminica
print(f"Numărul total de clienți pentru întreaga săptămână: {total_saptamana}")

# Calcularea numărului total de clienți pentru zilele lucrătoare (luni - vineri)
total_lucratoare = luni + marti + miercuri + joi + vineri
print(f"Numărul total de clienți pentru zilele lucrătoare (luni - vineri): {total_lucratoare}")

# Calcularea numărului total de clienți pentru weekend (sâmbătă și duminică)
total_weekend = sambata + duminica
print(f"Numărul total de clienți pentru weekend (sâmbătă și duminică): {total_weekend}")

# Verificarea dacă duminică au fost mai mulți clienți decât sâmbătă
if duminica > sambata:
    print("Duminică au fost mai mulți clienți decât sâmbătă.")
else:
    print("Duminică NU au fost mai mulți clienți decât sâmbătă.")

# Verificarea dacă numărul total de clienți pentru zilele lucrătoare este mai mare decât pentru weekend
if total_lucratoare > total_weekend:
    print("Numărul total de clienți din zilele lucrătoare este mai mare decât numărul total de clienți din weekend.")
else:
    print("Numărul total de clienți din zilele lucrătoare NU este mai mare decât numărul total de clienți din weekend.")

# Verificarea dacă săptămâna este considerată de succes
succes = total_saptamana > 1000 or total_weekend > 500
if succes:
    print("Săptămâna este considerată de succes.")
else:
    print("Săptămâna NU este considerată de succes.")
