def are_collinear(x1, y1, x2, y2, x3, y3):
    return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) == 0

def main():
    try:
        # Načtení vstupních souřadnic bodů
        points = []
        for i in range(3):
            x, y = map(float, input(f"Zadejte souřadnice {i+1}. bodu oddělené mezerou: ").split())
            points.append((x, y))

        # Kontrola, zda jsou body všechny různé
        if len(set(points)) != 3:
            print("Dva nebo všechny tři body splývají.")
            return

        # Kontrola, zda body leží na společné přímce
        if are_collinear(*points[0], *points[1], *points[2]):
            print("Zadané 3 body leží na jedné přímce.")
            # Prostřední bod
            middle_point = (sum(p[0] for p in points) / 3, sum(p[1] for p in points) / 3)
            print(f"Prostřední bod: {middle_point}")
        else:
            print("Zadané 3 body neleží na jedné přímce.")
    except ValueError:
        print("Chyba: Neplatný vstup. Zadejte prosím platné desetinné číslo.")

if __name__ == "__main__":
    main()