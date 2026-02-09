
import random

def format_case(t, cases):
    # cases: list of (n, a_list, w_list)
    out = [str(t)]
    for n, a, w in cases:
        out.append(str(n))
        out.append(" ".join(map(str, a)))
        out.append(" ".join(map(str, w)))
    return "\n".join(out)

random.seed(123456)

inputs = []

# Input 1: n=1 minimal (answer always 0)
inputs.append(format_case(1, [
    (1, [42], [-999999])
]))

# Input 2: n=2, huge w1 to catch off-by-one (w1 must not matter)
inputs.append(format_case(1, [
    (2, [5, 1], [10**6, -10**6])
]))

# Input 3: n=3, only w2 nonzero to catch indexing shift bugs
inputs.append(format_case(1, [
    (3, [10, 20, 30], [0, 7, 0])
]))

# Input 4: all aura equal, varied weights (answer must be 0)
inputs.append(format_case(1, [
    (5, [7, 7, 7, 7, 7], [5, -3, 0, 100, -100])
]))

# Input 5: many duplicates with extremes; negative early, positive late (delay range growth)
inputs.append(format_case(1, [
    (5, [1, 5, 5, 5, 100], [-10, -10, -10, 100, 100])
]))

# Input 6: strictly increasing, all weights positive (encourages early range growth)
inputs.append(format_case(1, [
    (6, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
]))

# Input 7: strictly increasing, all weights negative (encourages delaying range growth)
inputs.append(format_case(1, [
    (6, [1, 2, 3, 4, 5, 6], [-1, -2, -3, -4, -5, -6])
]))

# Input 8: clustered values with a huge gap; negative then small positive weights
inputs.append(format_case(1, [
    (6, [1, 2, 3, 1000, 1001, 1002], [-100, -100, -100, 1, 1, 1])
]))

# Input 9: one huge outlier; many equal small values; mixed weights
inputs.append(format_case(1, [
    (10, [5] * 9 + [10**9], [-50, -50, -50, -50, -50, 10, 10, 10, 10, 10])
]))

# Input 10: one small outlier; many equal huge values; mixed weights
inputs.append(format_case(1, [
    (10, [1] + [999_999_999] * 9, [-10, -10, -10, -10, -10, 50, 50, 50, 50, 50])
]))

# Input 11: alternating sign weights; distinct unsorted a-values
inputs.append(format_case(1, [
    (8,
     [40, 10, 70, 20, 60, 30, 80, 50],
     [10, -10, 10, -10, 10, -10, 10, -10])
]))

# Input 12: reversed input order (shouldn't matter if sorting is correct); mixed weights
inputs.append(format_case(1, [
    (7,
     [7, 6, 5, 4, 3, 2, 1],
     [3, -1, 4, -1, 5, -9, 2])
]))

# Input 13: multi-test input to catch per-test reset issues
inputs.append(format_case(3, [
    (1, [123456789], [999999]),
    (4, [8, 8, 8, 8], [1, -2, 3, -4]),
    (5, [9, 1, 4, 1, 5], [0, -7, 2, -3, 11]),
]))

# Input 14: overflow-stress (requires 64-bit intermediates); n=50, large range and weights
n14 = 50
a14 = [1 + (10**9 - 1) * i // (n14 - 1) for i in range(n14)]
w14 = [10**6] * n14
inputs.append(format_case(1, [
    (n14, a14, w14)
]))

# Input 15: max n stress (n=2000), duplicates + mixed small weights to keep sum safe
n15 = 2000
a15 = []
w15 = []
for i in range(n15):
    # Many duplicates: only 100 distinct "base" buckets * small offsets
    base = (i % 100) * 10_000_000  # up to 990,000,000
    offset = (i % 5)              # duplicates within bucket
    a15.append(base + offset + 1) # keep within [1, 1e9]
    w15.append(random.randint(-1000, 1000))

# Shuffle to ensure input is unsorted (sorting step is required)
perm = list(range(n15))
random.shuffle(perm)
a15 = [a15[i] for i in perm]
w15 = [w15[i] for i in perm]
inputs.append(format_case(1, [
    (n15, a15, w15)
]))

# Print in the required labeled format
print("**Test Cases: **")
for idx, s in enumerate(inputs, 1):
    print(f"Input {idx}:")
    print(s)
    if idx != len(inputs):
        print()
