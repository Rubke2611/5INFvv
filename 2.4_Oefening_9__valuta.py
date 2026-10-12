# Vaste wisselkoers: 1 EUR = 1.12 USD op 12/10/2026
wisselkoerrs_EUR_naar_USD = 1.12

bedrag = float(input("Bedrag: "))
bronvaluta = input("Bronvaluta (EUR of USD): ").strip().upper()
if bronvaluta == "EUR":
    doelvaluta = "USD"
    resultaat = bedrag * wisselkoerrs_EUR_naar_USD
if bronvaluta == "USD":
    doelvaluta = "EUR"
    resultaat = bedrag / wisselkoerrs_EUR_naar_USD

print(f"{bedrag:.2f} {bronvaluta} is gelijk aan {resultaat:.2f} {doelvaluta}")
