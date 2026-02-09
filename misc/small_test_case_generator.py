
# Generates 15 small, diverse inputs for the "Weighted Sliding Display" problem.
# Prints in the exact requested format.

def build_input(testcases):
    # testcases: list of (n, a_list, w_list)
    out = []
    out.append(str(len(testcases)))
    for n, a, w in testcases:
        out.append(str(n))
        out.append(" ".join(map(str, a)))
        out.append(" ".join(map(str, w)))
    return "\n".join(out)

inputs = []

# Input 1: n=1 boundary; score must be 0 regardless of w1
inputs.append(build_input([
    (1, [5], [1000000]),
]))

# Input 2: n=2 with extreme aura gap; simple adjacency mechanics
inputs.append(build_input([
    (2, [1, 1000000000], [0, 1]),
]))

# Input 3: Off-by-one trap: only w1 nonzero; correct answer must be 0
inputs.append(build_input([
    (3, [3, 1, 2], [999999, 0, 0]),
]))

# Input 4: All aura values equal; answer must be 0 with any weights
inputs.append(build_input([
    (5, [7, 7, 7, 7, 7], [-5, 3, 0, 10, -2]),
]))

# Input 5: Many duplicates in middle + extremes; early negatives encourage delaying range growth
inputs.append(build_input([
    (6, [1, 5, 5, 5, 5, 100], [-5, -5, -5, 10, 10, 10]),
]))

# Input 6: Strictly increasing (already sorted input); all weights positive
inputs.append(build_input([
    (6, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
]))

# Input 7: Reversed input order (bug-catcher for missing sort); mixed weights
inputs.append(build_input([
    (6, [6, 5, 4, 3, 2, 1], [3, -1, 2, -2, 1, -3]),
]))

# Input 8: Two clusters with huge gap; negative then positive weights to test timing
inputs.append(build_input([
    (6, [1, 2, 3, 1000, 1001, 1002], [-10, -10, 5, 5, 5, 5]),
]))

# Input 9: Single huge outlier; tests delaying inclusion of outlier under negative early weights
inputs.append(build_input([
    (5, [10, 11, 12, 13, 1000000000], [-100, -100, 1, 1, 1]),
]))

# Input 10: Alternating weights; order choices should align range changes with positive weights
inputs.append(build_input([
    (7, [4, 1, 7, 2, 6, 3, 5], [10, -10, 10, -10, 10, -10, 10]),
]))

# Input 11: All weights negative; duplicates allow zero-range steps early
inputs.append(build_input([
    (6, [5, 5, 5, 6, 7, 8], [-1, -2, -3, -4, -5, -6]),
]))

# Input 12: Multiple testcases in one input (t>1) to catch state leakage/reset issues
inputs.append(build_input([
    (1, [42], [-999999]),
    (2, [2, 1], [5, 5]),
    (5, [3, 3, 1, 2, 2], [0, 1, -1, 2, -2]),
]))

# Input 13: Weights include zeros and extreme magnitudes; also tests sign handling
inputs.append(build_input([
    (5, [1, 100, 101, 102, 103], [0, 1000000, 0, -1000000, 1]),
]))

# Input 14: Many duplicates interleaved in input; tie-break irrelevant but duplicates are key
inputs.append(build_input([
    (5, [2, 1, 2, 1, 2], [7, -3, 7, -3, 7]),
]))

# Input 15: Large aura gap + large weights to force 64-bit intermediates (still small n)
inputs.append(build_input([
    (8,
     [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997],
     [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]),
]))

print("Test Cases:")
for i, s in enumerate(inputs, 1):
    print(f"Input {i}:")
    print(s)
    if i != len(inputs):
        print()
