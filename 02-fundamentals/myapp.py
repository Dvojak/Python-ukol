import physics


print("=== Physics Calculations ===\n")

    # Váha na Zemi a na Měsíci
hmotnost = float(input("Zadej svou hmotnost na Zemi (v kg): "))
vaha_zeme = physics.vaha_na_planete(hmotnost, physics.EARTH_GRAVITY)
vaha_mesic = physics.vaha_na_planete(hmotnost, physics.MOON_GRAVITY)
print(f"\nTvoje váha:")
print(f" - Na Zemi: {vaha_zeme:.2f} N")
print(f" - Na Měsíci: {vaha_mesic:.2f} N")

    # Pád z výšky 10 metrů
vyska = 10  # metrů
cas_zeme = physics.cas_padu(vyska, physics.EARTH_GRAVITY)
cas_mesic = physics.cas_padu(vyska, physics.MOON_GRAVITY)
print(f"\nPád z výšky {vyska} metrů:")
print(f" - Na Zemi: {cas_zeme:.2f} sekund")
print(f" - Na Měsíci: {cas_mesic:.2f} sekund")

    # Světlo a vzdálenost
vzdalenost = float(input("\nZadej vzdálenost, kterou má světlo urazit (v metrech): "))
cas_svetla = physics.svetlo(vzdalenost)
print(f"Světlo urazí {vzdalenost:.2f} m za {cas_svetla:.12f} sekund.")

    # Zvuk a vzdálenost
cas_zvuku = float(input("\nZadej čas šíření zvuku (v sekundách): "))
vzdalenost_zvuku = physics.zvuk(cas_zvuku)
print(f"Zvuk urazí za {cas_zvuku:.2f} sekund {vzdalenost_zvuku:.2f} m.")