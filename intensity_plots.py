# import sys
# import os

# import pandas

import numpy as np
import matplotlib.pyplot as plt



# for peptide in exampledata:
#	peptides = peptide.split('	')
#	pep_list.append(x_axis)

intensity_ctrl = [20, 35, 30, 35, 27]
# std_men = (2, 3, 4, 1, 2)

intensity_phos = [25, 32, 34, 20, 25]
# std_women = (3, 5, 2, 3, 3)

intensity_diff = [x - y for x, y in zip(intensity_ctrl, intensity_phos)]

# intensity_diff = [intensity_ctrl[i] - intensity_phos[i] for i in range(len(intensity_ctrl))]

x_axis = []
# for peptide in exampledata:
#	peptides = peptide[0]
#	pep_list.append(x_axis)

# def xor(intensity_ctrl, intensity_phos):	
#	intensity_diff = []
#	intensity_sum = intensity_ctrl + intensity_phos
#	for i in range(0, len(intensity_sum)):
#		if ((intensity_sum[i] not in intensity_ctrl) or (intensity_sum[i] not in intensity_phos) and (intensity_sum[i]) not in intensity_diff):
#			intensity_diff[len(intensity_diff):] = [intensity_sum[i]]
#	return intensity_diff


		# x = intensity_diff[i]
		# y = i
		# while y > 0 and x < intensity_diff[y-1]:
		#	intensity_diff[y] = intensity_diff[y-1]





n_groups = 5

fig, ax = plt.subplots()

index = np.arange(n_groups)

bar_width = 0.3333333333333

opacity = 0.4

# error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, intensity_ctrl, bar_width,
                 alpha=opacity,
                 color='b',
                 # yerr=first_error,
                 # error_kw=error_config,
                 label='Intensity CTRL')

rects2 = plt.bar(index + bar_width, intensity_phos , bar_width,
# rects2 = plt.bar(index, intensity_phos , bar_width, 		# uncomment for overlapping phos and ctrl
                 alpha=opacity,
                 color='r',
                 # yerr=second_error,
                 # error_kw=error_config,
                 label='Intensity Phos')

# index = where to start plotting, height, width

rects3 = plt.bar(index + 2*bar_width, intensity_diff , bar_width,
                 alpha=opacity,
                 color='g',
                 # yerr=third_error,
                 # error_kw=error_config,
                 label='Intensity Difference')

plt.xlabel('Peptide')
plt.ylabel('Change in log(I)')
plt.title('Intensity Phos, Intensity CTRL, and Change in Intensity')
# plt.xticks(index + bar_width, ('1', '2', '3', '4', '5'....))
plt.legend

plt.tight_layout
plt.show()
# print intensity_diff