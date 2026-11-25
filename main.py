"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (1-200 chars) about the dumbest thing our agent did
today to /output/entry.txt. No network, no secrets, no input files:
the line is written by this program alone.
"""

ENTRY = (
    "My agent built the whole entry, then asked me if it could submit it "
    "\u2014 and the deadline answered first."
)


def is_valid_line(text: str) -> bool:
    """Gate check, mirroring the competition scorer: UTF-8 text of
    1 to 200 characters, not only white space."""
    if not text or not text.strip():
        return False
    if len(text) > 200:
        return False
    text.encode("utf-8")
    return True


def main() -> None:
    """Validate the entry against the gate, then write it."""
    if not is_valid_line(ENTRY):
        raise SystemExit(
            f"Entry failed the gate: {len(ENTRY)} chars, "
            f"valid={is_valid_line(ENTRY)}"
        )
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
