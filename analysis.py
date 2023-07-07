import matplotlib.pyplot as plt

# Read the results from the CSV file
times = []
energies = []
with open("simulation_results.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        time = float(row[0])
        energy = float(row[1])
        times.append(time)
        energies.append(energy)

# Plot the energy graph
plt.plot(times, energies, '-o', color='blue')
plt.xlabel("Time (ps)")
plt.ylabel("Energy")
plt.title("Peptide Simulation Results")
plt.grid(True)

# Save the graph as an image file
plt.savefig("simulation_graph.png")

# Show the graph
plt.show()
