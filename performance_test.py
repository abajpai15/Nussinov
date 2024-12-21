from nussinov import *
import time
import json


filename = "test_sequences.json"

file = open(filename, 'r')
database = json.load(file)

avg_seq_len = 0
start_time = time.time()
print(f"Testing began at {start_time}")

for key in database:
    seq = database[key]["sequence"]
    avg_seq_len += len(seq)
    soln = database[key]["dot-bracket"]
    max_base_pairs, structure = nussinov(seq)
    print(f"Structure {key}: {structure}")

end_time = time.time()
print(f"Testing ended at {end_time}")

elapsed = end_time-start_time
avg_seq_len = avg_seq_len/len(database)
print(f"Total time elapsed: {elapsed} seconds")
print(f"Processed {len(database)} sequences with an average length of: {avg_seq_len} characters")