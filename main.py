# The joke about the demo - a make.fun entry.
# Writes one text to /output/entry.txt: a one-line joke about working
# beside AI coding agents. Deterministic, no network, no input.

import os

JOKE = (
    "My agent trained in Osaka, where every failure becomes a bit: when the demo "
    "crashed on stage, it bowed for the laugh and advanced to a slide it had "
    "generated during the crash \u2014 'Expected Behavior.'"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
