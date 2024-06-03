def find_pairs(sequence_string):
    if len(sequence_string) > 2000 or len(sequence_string) < 2:
        print("Chyba: vstupní posloupnost je prázdná nebo příliš dlouhá")
        return

    try:
        sequence = [int(num) for num in sequence_string.split()]
    except ValueError:
        print("Chyba: hodnota na vstupu není platné celé číslo")
        return

    sums = {}
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            interval_sum = sum(sequence[i:j + 1])
            if interval_sum not in sums:
                sums[interval_sum] = 1
            else:
                sums[interval_sum] += 1

    pairs = sum((val * (val - 1)) // 2 for val in sums.values() if val > 1)

    print(f"Počet párů: {pairs}")

if __name__ == "__main__":
    sequence_string = input("Zadejte posloupnost čísel oddělených mezerou: ")
    find_pairs(sequence_string)