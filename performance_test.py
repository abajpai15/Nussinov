from nussinov import *
import time
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("TkAgg")

filename = "test_sequences.json"

file = open(filename, 'r')
database = json.load(file)

avg_seq_len = 0
start_time = time.time()
print(f"Testing began at {start_time}")

run_times = []
seq_lengths = []

for key in database:
    curr_start = time.time()
    seq = database[key]["sequence"]
    avg_seq_len += len(seq)
    soln = database[key]["dot-bracket"]
    max_base_pairs, structure = nussinov(seq)
    curr_end = time.time()
    print(f"Structure {key}, Length {len(seq)}: {structure}")
    print(f"Sequence Time Taken: {curr_end - curr_start}")

    run_times.append(curr_end - curr_start)
    seq_lengths.append(len(seq))

end_time = time.time()
print(f"Testing ended at {end_time}")

elapsed = end_time-start_time
avg_seq_len = avg_seq_len/len(database)
print(f"Total time elapsed: {elapsed} seconds")
print(f"Processed {len(database)} sequences with an average length of: {avg_seq_len} characters")


seq_lengths_np = np.array(seq_lengths)
n_cubed = seq_lengths_np**3
n_cubed_normalized = n_cubed / np.max(n_cubed) * np.max(run_times)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.scatter(seq_lengths, run_times, color='red', label='Actual Runtime')
plt.scatter(seq_lengths, n_cubed_normalized, color='black', label='$n^3$ graph')
plt.xlabel("Sequence Length")
plt.ylabel("Run Time (seconds)")
plt.title("Nussinov Algorithm Run Time vs. Sequence Length")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()