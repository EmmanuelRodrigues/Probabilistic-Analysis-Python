import matplotlib.pyplot as plt
import numpy as np

# Initialize all_walks
all_walks = []

# Simulate random walk 1000 times
all_walks = []
for i in range(1000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        clumzy = np.random.rand()
        if clumzy <= 0.005:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# Plot histogram of ends, display plot
ends = np_aw_t[-1,:]
plt.hist(ends)
plt.show()

ends = np_aw_t[-1,:]
c = (ends[ends >= 60])
count = len(c)
chance = (len(c)/1000)
print(chance)











