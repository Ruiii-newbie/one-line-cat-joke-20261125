"""One-line cat joke entry.

Writes a single joke about cats -- one line, under 200 characters,
nothing else -- to /output/entry.txt.
"""

import os

JOKE = (
    "My cat chased the red dot for three years -- today he caught it, "
    "and it was the recording light on my job interview."
)


def main():
    # Gate: one line, 1-200 characters, nothing else.
    assert 1 <= len(JOKE) <= 200, len(JOKE)
    assert "\n" not in JOKE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
