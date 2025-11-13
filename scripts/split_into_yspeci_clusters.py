#!/usr/bin/env python3

import sys

from chunk_reader import get_lines_from_chunks


def read_speci_map(f):
    with open(f) as _in:
        return dict(
            line.split("\t")
            for line in _in.read().rstrip().split("\n")
        )
        


def main():

    speci_map = read_speci_map(sys.argv[1])

    for line in get_lines_from_chunks(sys.argv[2]):
        cluster_id, members = line.split("\t")
        
        member_speci = {}
        for member in members.split(";"):
            member_genome = member[:member.rfind("_")]
            if member[:3] != "GCA":
                member_genome = member_genome[:member_genome.rfind("_")]
            member_speci.setdefault(speci_map.get(member_genome, "NO_SPECI"), []).append(member) 

        for speci, members in sorted(member_speci.items()):
            if speci != "NO_SPECI":
                print(cluster_id, speci, ";".join(sorted(members)), sep="\t") 
    


if __name__ == "__main__":
    main()
