#!/bin/bash
module load Miniforge3

INPUT=$(ls sp100_speci/*.txt | sed -n ${SLURM_ARRAY_TASK_ID}p)

if [[ ! -f sp095/$(basename ${INPUT}).done ]]; then
	python scripts/compute_speci_cluster.py ${INPUT} SP095_members_no_count_minid.tsv > sp095/$(basename ${INPUT}) && touch sp095/$(basename ${INPUT}).done
fi

if [[ ! -f sp090/$(basename ${INPUT}).done ]]; then
	python scripts/compute_speci_cluster.py ${INPUT} SP090_members_no_count_minid.tsv > sp090/$(basename ${INPUT}) && touch sp090/$(basename ${INPUT}).done
fi

if [[ ! -f sp080/$(basename ${INPUT}).done ]]; then
	python scripts/compute_speci_cluster.py ${INPUT} SP080_members_no_count_minid.tsv > sp080/$(basename ${INPUT}) && touch sp080/$(basename ${INPUT}).done
fi
