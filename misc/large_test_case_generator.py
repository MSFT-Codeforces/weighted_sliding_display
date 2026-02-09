
import random

def emit_input(cases):
    # cases: list of tuples (n, a_list, w_list)
    lines = [str(len(cases))]
    for n, a, w in cases:
        assert n == len(a) == len(w)
        lines.append(str(n))
        lines.append(" ".join(map(str, a)))
        lines.append(" ".join(map(str, w)))
    return "\n".join(lines)

inputs = []

# Input 1: n=2000, wide distinct-ish values, all weights +1e6 (maximize early growth; overflow stress)
random.seed(1)
n = 2000
a = random.sample(range(1, 10**9), n)
w = [10**6] * n
inputs.append(emit_input([(n, a, w)]))

# Input 2: n=2000, wide distinct-ish values, all weights -1e6 (delay growth; negative stress)
random.seed(2)
a = random.sample(range(1, 10**9), n)
w = [-10**6] * n
inputs.append(emit_input([(n, a, w)]))

# Input 3: n=2000, huge duplicate plateau + two extremes placed adversarially; weights: first half negative, second half positive
# (tests "burn steps with no range change" and timing of including extremes)
n = 2000
a = [500_000_000] * 999 + [1_000_000_000] + [500_000_000] * 999 + [1]
w = [-10**6] * 1000 + [10**6] * 1000
inputs.append(emit_input([(n, a, w)]))

# Input 4: n=2000, 4 clusters with big gaps + small jitter; alternating weights +/-1e6 (timing is crucial)
random.seed(4)
clusters = []
for base in [100_000, 200_000, 500_000_000, 900_000_000]:
    clusters.extend([base + random.randint(0, 99) for _ in range(500)])
a = clusters[:]
random.shuffle(a)  # ensure unsorted input to catch missing sort
w = [(10**6 if i % 2 == 0 else -10**6) for i in range(n)]
inputs.append(emit_input([(n, a, w)]))

# Input 5: n=2000, near-constant values + one huge outlier; weights: long negative prefix then positive suffix
# (optimal should delay including outlier until weights become positive)
random.seed(5)
a = [1_000_000_000] + [100_000_000 + random.randint(0, 1000) for _ in range(1999)]  # outlier placed first
w = [-10**6] * 1500 + [10**6] * 500
inputs.append(emit_input([(n, a, w)]))

# Input 6: n=2000, two outliers (1 and 1e9) + random middle; w1/w2 extreme to catch off-by-one (w1 irrelevant in correct sol)
random.seed(6)
mid = random.sample(range(10**7, 10**9 - 10**7), 1998)
a = mid + [1, 1_000_000_000]
random.shuffle(a)  # unsorted
w = [0] * n
w[0] = 10**6        # should not matter (range at i=1 is always 0)
w[1] = -10**6       # should matter (range at i=2)
for i in range(2, n):
    w[i] = random.randint(-10**6, 10**6)
inputs.append(emit_input([(n, a, w)]))

# Input 7: n=2000, already sorted increasing with quadratic gaps hitting 1e9 exactly; mixed weights (tests solutions that skip sorting)
random.seed(7)
a = [(i * i * 250) for i in range(1, n + 1)]  # max at i=2000 => 1,000,000,000
w = [random.randint(-10**6, 10**6) for _ in range(n)]
inputs.append(emit_input([(n, a, w)]))

# Input 8: n=2000, reversed version of Input 7 (strongly catches "forgot to sort")
random.seed(8)
a = [(i * i * 250) for i in range(n, 0, -1)]  # descending
w = [10**6] * n
inputs.append(emit_input([(n, a, w)]))

# Input 9: multi-test input (t=4), total n=2000; varied patterns to catch per-test DP reset/state leakage
random.seed(9)
cases = []

# 9.1 all equal
n1 = 500
a1 = [7] * n1
w1 = [random.randint(-10**6, 10**6) for _ in range(n1)]
cases.append((n1, a1, w1))

# 9.2 duplicates with extremes, adversarial placement
n2 = 500
a2 = [123456789] * 248 + [1_000_000_000] + [123456789] * 250 + [1]
w2 = [-10**6] * 250 + [10**6] * 250
cases.append((n2, a2, w2))

# 9.3 random wide
n3 = 500
a3 = random.sample(range(1, 10**9), n3)
w3 = [random.randint(-10**6, 10**6) for _ in range(n3)]
cases.append((n3, a3, w3))

# 9.4 clustered + alternating weights
n4 = 500
a4 = []
for base in [10_000, 20_000, 900_000_000, 950_000_000]:
    a4.extend([base + random.randint(0, 50) for _ in range(125)])
random.shuffle(a4)
w4 = [(10**6 if i % 2 == 0 else -10**6) for i in range(n4)]
cases.append((n4, a4, w4))

inputs.append(emit_input(cases))

# Input 10: n=2000, many ties (values 1..50 repeated), unsorted; weights mostly 0 with spikes (tests weight indexing + interval range)
random.seed(10)
vals = []
for x in range(1, 51):
    vals.extend([x] * 40)  # 50*40 = 2000
a = vals[:]
random.shuffle(a)
w = [0] * n
w[0] = 10**6  # should be irrelevant if implemented correctly
for i in range(1, n):
    if (i + 1) % 100 == 0:
        w[i] = (10**6 if ((i // 100) % 2 == 0) else -10**6)
for idx in random.sample(range(1, n), 20):
    w[idx] = random.choice([-10**6, 10**6])
inputs.append(emit_input([(n, a, w)]))

# Print in the required format
print("Test Cases:")
for i, s in enumerate(inputs, 1):
    print(f"Input {i}:")
    print(s)
    if i != len(inputs):
        print()
