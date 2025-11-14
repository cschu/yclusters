#!/usr/bin/env python3

import sys

from chunk_reader import get_lines_from_chunks


def read_index(f):
    d = {}
    for line in get_lines_from_chunks(f):
        cluster, start, end = line.split("\t")
        d[cluster] = int(start), int(end)
    return d

def read_cluster_size(f):
    with open(f, "rt") as _in:
        for line in _in:
            line = line.rstrip().split(" ")
            n_total, n_pg3, n_spire = map(int, line)
            return n_total, n_pg3, n_spire


def main():
    with open(sys.argv[1], "rt") as speci_sp100:
        index = read_index(f"{sys.argv[1]}.index")
        n_total, n_pg3, n_spire = read_cluster_size(f"{sys.argv[1]}.genomes")

        
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
                # print(spxxx_cluster, len(spxxx_members), spxxx_members[:10], sep="\t")
                genomes = {
                    "_".join(m.split("_")[:(-2 if m[:2] == "GD" else -1)])
                    for m in spxxx_members
                }
                n_genomes = len(genomes)
                n_genomes_pg3 = len([m for m in genomes if m[:3] == "GCA"])
                n_genomes_spire = n_genomes - n_genomes_pg3

                print("CLUSTER", spxxx_cluster, n_genomes, n_total, n_genomes_pg3, n_pg3, n_genomes_spire, n_spire, sep="\t")
                print(*sorted(spxxx_members), sep="\n")
                #for member in sorted(spxxx_members):
                #    print(spxxx_cluster, member, n_genomes, n_total, n_genomes_pg3, n_pg3, n_genomes_spire, n_spire, sep="\t")

                    
    



if __name__ == "__main__":
    main()
