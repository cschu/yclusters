#!/usr/bin/env python3

import sys

from chunk_reader import get_lines_from_chunks


def main():
    p = 0

    with open(f"{sys.argv[1]}.index", "wt") as index_out:
        for line in get_lines_from_chunks(sys.argv[1]):
            cluster, members = line.split("\t")
            pend = p + len(line) 
            print(cluster, p, pend, sep="\t", file=index_out)
            p = pend + 1
            
    


if __name__ == "__main__":
    main()
