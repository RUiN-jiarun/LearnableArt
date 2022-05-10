import csv
import matplotlib.pyplot as plt
import os
import math


with open('testing_res/res/bird_rain_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list1 = [math.log(float(row['loss'])) for row in reader]

with open('testing_res/res_improved/bird_rain_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list2 = [math.log(float(row['loss'])) for row in reader]

# print(loss_list)


x1 = range(0, 1000)
y1 = loss_list1
y2 = loss_list2
# y = range(0,int(1e8),int(1e7))
# print(x1, y1)
plt.plot(x1, y1, '-.', color='r', linewidth=1)
plt.plot(x1, y2, color='b', linewidth=1)
# plt.yticks(y)
plt.xlabel('Iters')
plt.ylabel('ln(Loss)')
# output_filename, file_extension = os.path.splitext(params.output_image)
plt.savefig('_loss.jpg')