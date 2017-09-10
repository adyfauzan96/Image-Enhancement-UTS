from color_histogram.io_util.image import loadRGB
from color_histogram.core.hist_1d import Hist1D
import matplotlib.pyplot as plt

from color_histogram.datasets.datasets import dataFile

image_file = dataFile("messi", 0)


image = loadRGB(C:/Users/penak/Music/messi.jpg')

hist1D = Hist1D(image, num_bins=16, color_space='Lab', channel=0)

fig = plt.figure()
ax = fig.add_subplot(111)
hist1D.plot(ax)
plt.show()