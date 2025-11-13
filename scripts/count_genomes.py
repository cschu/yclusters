#!/usr/bin/env python3

import sys

from chunk_reader import get_lines_from_chunks


def main():

    genomes = set()
    for line in get_lines_from_chunks(sys.argv[1]):
        members = line[line.find("\t") + 1:].split(";")
        genomes.update("_".join(m.split("_")[:(-2 if m[:2] == "GD" else -1)]) for m in members)

    with open(f"{sys.argv[1]}.genomes", "wt") as genomes_out:
        n_total = len(genomes)
        n_pg3 = len([m for m in genomes if m[:3] == "GCA"])
        n_spire = n_total - n_pg3
        print(n_total, n_pg3, n_spire, file=genomes_out)
        print(*sorted(genomes), sep="\n", file=genomes_out)
        


if __name__ == "__main__":
    main()
