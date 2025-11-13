import re
import pymongo




client = pymongo.MongoClient(
    "mongodb://schudoma:password_schudoma@koppa:26017",
)
pg3_db = client["progenomes"]


#record = pg3_db.samples.find_one({"fr13_cluster": {"$exists": True}})
#print(record["sample_id"], record["fr13_cluster"], sep="\t")

records = list(pg3_db.samples.find({"fr13_cluster": {"$exists": True}}))

for record in records:
    print(record["sample_id"], record["fr13_cluster"], sep="\t")
