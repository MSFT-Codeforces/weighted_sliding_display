
import sys

def is_valid_int_token(tok: str) -> bool:
    if tok == "":
        return False
    if tok[0] == "-":
        return len(tok) > 1 and tok[1:].isdigit()
    return tok.isdigit()

def check_line_strict(line: str) -> bool:
    # Strict formatting:
    # - no empty lines
    # - no leading/trailing spaces
    # - no tabs
    # - no multiple spaces between tokens
    if line == "":
        return False
    if line != line.strip():
        return False
    if "\t" in line:
        return False
    if "  " in line:
        return False
    return True

def validate(data: str) -> bool:
    lines = data.splitlines()

    if not lines:
        return False

    for ln in lines:
        if not check_line_strict(ln):
            return False

    idx = 0

    # t
    first = lines[idx].split(" ")
    if len(first) != 1 or not is_valid_int_token(first[0]):
        return False
    t = int(first[0])
    if not (1 <= t <= 20):
        return False
    idx += 1

    total_n = 0

    for _ in range(t):
        if idx + 2 >= len(lines):
            return False

        # n
        parts = lines[idx].split(" ")
        if len(parts) != 1 or not is_valid_int_token(parts[0]):
            return False
        n = int(parts[0])
        if not (1 <= n <= 2000):
            return False
        total_n += n
        if total_n > 2000:
            return False
        idx += 1

        # a_1..a_n
        a_parts = lines[idx].split(" ")
        if len(a_parts) != n:
            return False
        for tok in a_parts:
            if not is_valid_int_token(tok):
                return False
            val = int(tok)
            if not (1 <= val <= 10**9):
                return False
        idx += 1

        # w_1..w_n
        w_parts = lines[idx].split(" ")
        if len(w_parts) != n:
            return False
        for tok in w_parts:
            if not is_valid_int_token(tok):
                return False
            val = int(tok)
            if not (-10**6 <= val <= 10**6):
                return False
        idx += 1

    return idx == len(lines)

def main():
    data = sys.stdin.read()
    print("True" if validate(data) else "False")

if __name__ == "__main__":
    main()
