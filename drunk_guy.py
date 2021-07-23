import numpy as np
import time
import pandas
import matplotlib.pyplot as plt

df = open("DRUNKDATA.txt", "w")

finish_point = 0
steps = 0
t = 0

start_time = time.time()

while finish_point <= 150:
    s = np.random.randint(3)
    finish_point += 1
    if s == 1:
        steps += 1
        data = finish_point, steps
        df.write(repr(data) + "\n")
        print(steps)
        if steps == 5 or steps == -5:
            finish_point = 0
            t = t + 1
            steps = 0
            df.truncate(0)

    elif s == 0:
        steps = steps + 0
        data = finish_point, steps
        df.write(repr(data) + "\n")
        print(steps)
        if steps == 5 or steps == -5:
            finish_point = 0
            t = t + 1
            steps = 0
            df.truncate()
    else:
        steps = steps - 1
        print(steps)
        data = finish_point, steps
        df.write(repr(data) + "\n")
        if steps == 5 or steps == -5:
            finish_point = 0
            t = t + 1
            steps = 0
            df.truncate(0)

df.close()
with open("DRUNKDATA.txt")  as f :
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

plt.plot(x, y)
plt.show()

print(t)
print("--- %s seconds ---" % (time.time() - start_time))