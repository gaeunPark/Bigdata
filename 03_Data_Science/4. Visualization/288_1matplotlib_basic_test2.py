import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

simple_data1 = np.arange(1, 11, 1)
box_plot_data = [simple_data1]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

box_labels = ['s1']
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
plt.xlabel('Distribution')
plt.ylabel('Value')

plt.show()