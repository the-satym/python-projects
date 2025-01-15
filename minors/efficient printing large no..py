#date: 14 jan 2025


import time

# Start time
start_time = time.time()

# Write numbers to a file instead of printing to console
with open("output1.txt", "w") as f:
    f.write("\n".join(map(str, range(1, 10000001))))

# End time
end_time = time.time()

# Calculate and print elapsed time
print(f"Time taken: {end_time - start_time} seconds")
