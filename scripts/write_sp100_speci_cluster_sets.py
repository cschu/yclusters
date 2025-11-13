#!/usr/bin/env

import pathlib
import sys

from chunk_reader import get_lines_from_chunks


def main():

    outdir = pathlib.Path("sp100_speci")
    outdir.mkdir(exist_ok=True, parents=True,)


    speci_files = {}

    for line in get_lines_from_chunks(sys.argv[1]):
        cluster_id, speci, members = line.rstrip().split("\t")
        fo = speci_files.get(speci)
        if fo is None:
            fo = speci_files[speci] = open(outdir / f"{speci}.txt", "wt")
        print(cluster_id, members, sep="\t", file=fo)


    for speci, fh in speci_files.items():
        try:
            fh.close()
        except Exception as ex:
            print("Problem closing file handle for {speci=}:\n{ex}")
            continue


if __name__ == "__main__":
    main()
