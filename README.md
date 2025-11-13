Y-cluster
=========

1. Obtain all available specI annotations for PG3 genomes and SPIRE bins:
- get_speci_for_bin_spire.py and get_speci_for_bin_pg3.py
- sort outputs by 1st column (genome/bin id)
- extract bin_id/y-id map 
 -> tail -n +2 /g/scb2/bork/ckim/HGT_MGE_project_v3/data/SPIRE_genome_annotations.tsv | cut -f 1,2 | sort -k2,2 > spire_genome_yid_map.txt
- generate spire y-id/speci map (also filter out speci assignments that did not result from marker gene mapping)
 -> join -1 2 -2 1 spire_genome_yid_map.txt spire_genome_speci_map.txt | tr " " "\t" | awk '$4=="pg_v3_mapped_marker_gene"' | cut -f 2,3 | sort -k1,1 > spire_yid_speci_map.txt
- concat both maps and get rid of GCA version tail (.[0-9]+) as the y-cluster annotation does not have that
 -> cat pg3_genome_speci_map.txt spire_yid_speci_map.txt | sed "s/\.[0-9]\+//" > pg3_spire_speci_map.txt
- remove singleton specI clusters
 -> join -1 1 -2 2 -o 2.1,2.2 <(cut -f 2 pg3_spire_speci_map.txt | sort -k1,1 | uniq -c | sed "s/^ \+//" | awk '$1>1 {print $2}') <(sort -k2,2 pg3_spire_speci_map.txt) | tr " " "\t" > pg3_spire_speci_map.txt.sorted.no_singleton_specis

2. Preprocess SP100 clusters
- remove count column and remove SP100_0* padding to save some space / downstream processing time -- NOTE: SP0XX clustering references SP100 clusters and SP100 are non-contiguous (supposedly), i.e. we cannot completely replace the id by the row index  
- from previous attempts: this should be about it with respect to data reduction at this time, otherwise the lookups will be too complex later on
 -> cut -f 1,3 /g/scb2/bork/ckim/HGT_MGE_project_v3/1.combine_SPIRE/SP100/SP100_members.tsv | sed 's/^SP100_0*\([0-9]\)/\1/' > SP100_members_no_count_minid.tsv (about 42 minutes)

- Do the same with derived cluster sets (SP095,SP090,SP080)!
 -> use scripts/clean_cluster_data.sh

3. Split SP100 clusters by specI
- initial split, keep all singletons etc., only drop genes without speci and resulting empty clusters
 -> python scripts/split_into_yspeci_clusters.py pg3_spire_speci_map.txt SP100_members_no_count_minid.tsv > SP100_members_by_speci.tsv (about 1 hour 5 minutes)
- + ignoring singleton specis
 -> python scripts/split_into_yspeci_clusters.py pg3_spire_speci_map.txt.sorted.no_singleton_specis SP100_members_no_count_minid.tsv > SP100_members_by_speci.tsv.no_singleton_specis (about 1 hour 1 minute)
