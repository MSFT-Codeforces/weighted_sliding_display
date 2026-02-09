
import os
import re
from typing import Tuple, Optional

INT_RE = re.compile(r"^[+-]?\d+$")
I64_MIN = -(2**63)
I64_MAX = 2**63 - 1


def _to_unix_newlines(s: str) -> str:
    # Normalize Windows/old-Mac newlines to '\n'
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _parse_input_t(input_text: str) -> Tuple[Optional[int], Optional[str]]:
    """
    Parse enough of the input to obtain t and validate basic structure
    against stated constraints. Returns (t, error_message).
    """
    s = _to_unix_newlines(input_text)
    toks = s.split()
    if not toks:
        return None, "Input is empty; cannot determine number of test cases."

    if not INT_RE.fullmatch(toks[0]):
        return None, f"Input: first token must be integer t, got {toks[0]!r}"
    t = int(toks[0])
    if not (1 <= t <= 20):
        return None, f"Input: t={t} out of constraints [1..20]"

    idx = 1
    sum_n = 0
    for case in range(1, t + 1):
        if idx >= len(toks):
            return None, f"Input: case {case}: missing n"
        if not INT_RE.fullmatch(toks[idx]):
            return None, f"Input: case {case}: n is not an integer: {toks[idx]!r}"
        n = int(toks[idx])
        idx += 1
        if not (1 <= n <= 2000):
            return None, f"Input: case {case}: n={n} out of constraints [1..2000]"
        sum_n += n
        if sum_n > 2000:
            return None, f"Input: sum of n exceeds 2000 at case {case} (sum_n={sum_n})"

        # a_i
        if idx + n > len(toks):
            return None, f"Input: case {case}: missing a array (expected {n} integers)"
        for j in range(n):
            tok = toks[idx + j]
            if not INT_RE.fullmatch(tok):
                return None, f"Input: case {case}: a[{j+1}] is not an integer: {tok!r}"
            val = int(tok)
            if not (1 <= val <= 10**9):
                return None, f"Input: case {case}: a[{j+1}]={val} out of constraints [1..1e9]"
        idx += n

        # w_i
        if idx + n > len(toks):
            return None, f"Input: case {case}: missing w array (expected {n} integers)"
        for j in range(n):
            tok = toks[idx + j]
            if not INT_RE.fullmatch(tok):
                return None, f"Input: case {case}: w[{j+1}] is not an integer: {tok!r}"
            val = int(tok)
            if not (-10**6 <= val <= 10**6):
                return None, f"Input: case {case}: w[{j+1}]={val} out of constraints [-1e6..1e6]"
        idx += n

    return t, None


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    t, in_err = _parse_input_t(input_text)
    if in_err is not None:
        # If the input is malformed, we cannot meaningfully check output.
        return False, in_err
    assert t is not None

    out = _to_unix_newlines(output_text)

    # Allow exactly one trailing newline at EOF; otherwise be strict.
    if out.endswith("\n\n"):
        return False, "Output: more than one trailing newline at EOF is not allowed."
    if out.endswith("\n"):
        out = out[:-1]

    # After stripping one optional trailing newline, enforce strict line structure.
    if out == "":
        return False, f"Output: expected {t} line(s), got empty output."

    lines = out.split("\n")
    if len(lines) != t:
        return False, f"Output: expected exactly {t} line(s), got {len(lines)}."

    for case_idx, line in enumerate(lines, start=1):
        if line == "":
            return False, f"Case {case_idx}: empty line; expected one integer."
        if line != line.strip():
            return False, f"Case {case_idx}: leading/trailing whitespace is not allowed."
        parts = line.split()
        if len(parts) != 1:
            return False, f"Case {case_idx}: expected exactly 1 token on the line, got {len(parts)}."
        tok = parts[0]
        if not INT_RE.fullmatch(tok):
            return False, f"Case {case_idx}: expected an integer, got {tok!r}."
        val = int(tok)
        if not (I64_MIN <= val <= I64_MAX):
            return False, f"Case {case_idx}: integer {val} is out of signed 64-bit range."

    # Cannot verify optimality without solving; format/range checks passed.
    return True, "OK"


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH")
    out_path = os.environ.get("OUTPUT_PATH")
    if not in_path or not out_path:
        raise SystemExit("Environment variables INPUT_PATH and OUTPUT_PATH must be set.")
    with open(in_path, "r", encoding="utf-8") as f:
        input_text = f.read()
    with open(out_path, "r", encoding="utf-8") as f:
        output_text = f.read()
    ok, _reason = check(input_text, output_text)
    print("True" if ok else "False")
