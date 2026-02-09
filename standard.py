import sys


def solve_test_case(artifact_auras: list[int], prefix_weights: list[int]) -> int:
    """
    Compute the maximum achievable weighted score for one test case.

    The algorithm:
    1) Build the deterministic sorted lineup v from (a_i, i).
    2) Run interval DP where each state is a contiguous segment [L, R] of v,
       grown by one element per step.

    Args:
        artifact_auras: Aura values a_1..a_n.
        prefix_weights: Weights w_1..w_n (may be negative).

    Returns:
        The maximum possible score as an integer.
    """
    artifact_count = len(artifact_auras)
    if artifact_count == 1:
        return 0

    sorted_pairs = sorted(
        (artifact_auras[position], position)
        for position in range(artifact_count)
    )
    sorted_auras = [aura_value for aura_value, _ in sorted_pairs]

    negative_infinity = -10**60

    current_dp = [0] * artifact_count

    for current_length in range(1, artifact_count):
        weight_value = prefix_weights[current_length]
        next_dp_size = artifact_count - current_length
        next_dp = [negative_infinity] * next_dp_size

        left_index_limit = artifact_count - current_length + 1
        for left_index in range(left_index_limit):
            current_score = current_dp[left_index]
            if current_score == negative_infinity:
                continue

            right_index = left_index + current_length - 1

            if left_index > 0:
                new_left_index = left_index - 1
                new_spread = (
                    sorted_auras[right_index] - sorted_auras[new_left_index]
                )
                candidate_score = current_score + weight_value * new_spread
                if candidate_score > next_dp[new_left_index]:
                    next_dp[new_left_index] = candidate_score

            if right_index + 1 < artifact_count:
                new_spread = (
                    sorted_auras[right_index + 1] - sorted_auras[left_index]
                )
                candidate_score = current_score + weight_value * new_spread
                if candidate_score > next_dp[left_index]:
                    next_dp[left_index] = candidate_score

        current_dp = next_dp

    return current_dp[0]


def main() -> None:
    """
    Read input, solve all test cases, and print the result for each one.

    Input:
        t
        n
        a_1..a_n
        w_1..w_n
        (repeated t times)

    Output:
        For each test case, one line with the maximum achievable score.
    """
    tokens = sys.stdin.buffer.read().split()
    token_index = 0

    test_count = int(tokens[token_index])
    token_index += 1

    output_lines: list[str] = []

    for _ in range(test_count):
        artifact_count = int(tokens[token_index])
        token_index += 1

        artifact_auras = [
            int(tokens[token_index + offset])
            for offset in range(artifact_count)
        ]
        token_index += artifact_count

        prefix_weights = [
            int(tokens[token_index + offset])
            for offset in range(artifact_count)
        ]
        token_index += artifact_count

        output_lines.append(
            str(solve_test_case(artifact_auras, prefix_weights))
        )

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()