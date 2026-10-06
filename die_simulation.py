import numpy as np
import matplotlib.pyplot as plt

# Fix random seed for reproducible output
np.random.seed(42)

# Simulate rolling a fair six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)

# Print first 10 rolls
print("First 10 rolls:", rolls[:10])

# Count how many times each face appears
faces, counts = np.unique(rolls, return_counts=True)

print("\nFace  Count  Empirical P  Theoretical P")

for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    theoretical_probability = 1 / 6

    print(
        face,
        count,
        round(empirical_probability, 4),
        round(theoretical_probability, 4)
    )

# Plot histogram
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), edgecolor="black")
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("1000 Rolls of a Fair Six-Sided Die")
plt.xticks([1, 2, 3, 4, 5, 6])

# Save plot
plt.savefig("die_rolls.png")

print("\nSaved die_rolls.png")