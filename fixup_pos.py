#!/usr/bin/env python3
from os import listdir
from os import rename

def main():
    for filename in listdir("CAM"):
        if filename.endswith("pos.csv"):
            filename = f"CAM/{filename}"
            old_filename = f"{filename}.old"
            new_filename = f"{filename}.new"

            print(f"Processing {filename}")
            with open(filename, "r") as ifd:
                with open(new_filename, "w") as ofd:
                    for i, line in enumerate(ifd):
                        if i == 0:
                            ofd.write("Designator,Val,Package,MidX,MidY,Rotation,Side\n")
                        else:
                            ofd.write(line)
                
            rename(filename, old_filename)
            rename(new_filename, filename)

if __name__ == "__main__":
    main()

