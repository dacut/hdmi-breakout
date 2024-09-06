#!/usr/bin/env python3
from os import listdir
from os import rename

REPLACEMENTS = {
    "C346216": "C5189822",
    "C2130243": "C43473",
    "C2131941": "C427206",
    "C4096848": "C25901",
}


def main():
    for file in listdir("."):
        if file.endswith(".kicad_sch"):
            print(f"Processing {file}")
            with open(file, "r") as fd:
                data = fd.read()

            for original, replacement in REPLACEMENTS.items():
                if data.find(original) == -1:
                    continue

                data = data.replace(f'"{original}"', f'"{replacement}"')
                assert data.find(original) == -1
                assert data.find(replacement) != -1, f"Failed to find replacement {replacement} in {file}"
            
            with open(f"{file}.new", "w") as fd:
                fd.write(data)
            
            rename(file, f"{file}.old")
            rename(f"{file}.new", file)

if __name__ == "__main__":
    main()
