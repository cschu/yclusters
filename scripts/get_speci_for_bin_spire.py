import re
import pymongo




client = pymongo.MongoClient(
    "mongodb://schudoma:password_schudoma@koppa:26016",
)
spire_db = client["mags"]

valid_cluster_assignment = re.compile(r"^pg_v3_mapped")

#record = spire_db.bins.find_one()
#print(record["bin_id"], record["spire_v1_cluster"]["name"], record["spire_v1_cluster"]["assignment_method"], sep="\t")


records = list(spire_db.bins.find(
    {"spire_v1_cluster.assignment_method": valid_cluster_assignment}
))


for record in records:
    print(record["bin_id"], record["spire_v1_cluster"]["name"], record["spire_v1_cluster"]["assignment_method"], sep="\t")
