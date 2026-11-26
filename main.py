#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes one line (<=200 chars) to /output/entry.txt: the elevator pitch
a city pigeon gives investors for its startup.
"""
import os

ENTRY = (
    "Coo-ber: the last-mile delivery network that already owns every "
    "rooftop, ledge and statue in the city - and our drivers work for "
    "breadcrumbs. Seed us before the squirrels IPO."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
