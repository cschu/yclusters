#!/usr/bin/env python3

import sys

from chunk_reader import get_lines_from_chunks


def read_index(f):
    d = {}
    for line in get_lines_from_chunks(f):
        cluster, start, end = line.split("\t")
        d[cluster] = int(start), int(end)
    return d


def main():
    with open(sys.argv[1], "rt") as speci_sp100:
        index = read_index(f"{sys.argv[1]}.index")

        genomes = set()
        
        for line in get_lines_from_chunks(sys.argv[2]):
            spxxx_cluster, members = line.split("\t")
            spxxx_members = []

            for member in members.split(";"):
                member_xy = index.get(member)
                if member_xy is not None:
                    start, end = member_xy
                    speci_sp100.seek(start)
                    sp100_cluster, sp100_members = speci_sp100.read(end - start).split("\t")
                    if sp100_cluster != member:
                        raise ValueError(f"{member=} != {sp100_cluster=}")
                    spxxx_members += sp100_members.split(";")

            if spxxx_members:
                print(spxxx_cluster, len(spxxx_members), spxxx_members[:10], sep="\t")
                genomes.update("_".join(m.split("_")[:(-2 if m[:2] == "GD" else -1)]) for m in spxxx_members)

        print(f"GENOMES={len(genomes)}")
                    
    



if __name__ == "__main__":
    main()
