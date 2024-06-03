import sys
import math

def calculate_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)

def find_closest_planes(planes):
    min_distance = float('inf')
    closest_pairs = []

    for i in range(len(planes)):
        for j in range(i + 1, len(planes)):
            dist = calculate_distance(planes[i][0], planes[j][0])
            if dist < min_distance:
                min_distance = dist
                closest_pairs = [(planes[i][1], planes[j][1])]
            elif dist == min_distance:
                closest_pairs.append((planes[i][1], planes[j][1]))

    return min_distance, closest_pairs

if __name__ == "__main__":
    print("Zadejte souřadnice a označení letadel:")
    planes = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        try:
            coords, name = line.split(':')
            x, y = map(int, coords.split(','))
            planes.append(([x, y], name))
        except ValueError:
            print("Chyba: nesprávný formát vstupu", file=sys.stderr)

    if len(planes) < 2:
        print("Chyba: méně než dvě letadla na vstupu", file=sys.stderr)
    else:
        min_distance, pairs = find_closest_planes(planes)
        print(f"Vzdálenost nejbližších letadel: {min_distance:.6f}")
        print(f"Nalezených dvojic: {len(pairs)}")
        for pair in pairs:
            print(f" - {' - '.join(pair)}")
