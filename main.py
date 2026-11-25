"""Write one short family scene to /output/entry.txt.

Stdlib only. The scene is a small domestic moment: warm, funny and
heartfelt, in two lines and well under 280 characters.
"""

import os

SCENE = (
    "Grandma hid the last biscuit in the teapot and winked at me.\n"
    "Grandad searched the whole kitchen like a detective on a very serious case."
)


def main():
    text = SCENE.strip()
    assert 1 <= len(text) <= 280, len(text)
    lines = text.split("\n")
    assert 1 <= len(lines) <= 2
    assert all(line.strip() for line in lines), "no blank lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
