import csv
import matplotlib.pyplot as plt
import os
import math


with open('testing_res/original/brad_muse_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list1 = [math.log(float(row['loss'])) for row in reader]

with open('testing_res/res_improved/brad_muse_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list2 = [math.log(float(row['loss'])) for row in reader]

with open('testing_res/adam_res/brad_muse_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list3 = [math.log(float(row['loss'])) for row in reader]

with open('testing_res/adam_res_improved/brad_muse_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list4 = [math.log(float(row['loss'])) for row in reader]

with open('testing_res/random_init/brad_muse_loss.csv') as f:
    reader = csv.DictReader(f)
    loss_list5 = [math.log(float(row['loss'])) for row in reader]


x1 = range(0, 1000)
y1 = loss_list1
y2 = loss_list2
y3 = loss_list3
y4 = loss_list4
y5 = loss_list5
# y = range(0,int(1e8),int(1e7))
# print(x1, y1)
plt.plot(x1, y1, color='r', linewidth=1, label='original')
plt.plot(x1, y2, color='b', linewidth=1, label='improve')
plt.plot(x1, y3, '-.', color='orangered', linewidth=1, label='original-adam')
plt.plot(x1, y4, '-.', color='g', linewidth=1, label='improve-adam')
plt.plot(x1, y5, '--', color='cyan', linewidth=1, label='random init')
# plt.yticks(y)
plt.xlabel('Iters')
plt.ylabel('ln(Loss)')
plt.legend()
# output_filename, file_extension = os.path.splitext(params.output_image)
plt.savefig('_loss.jpg')