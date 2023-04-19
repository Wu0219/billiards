from PIL import Image
import numpy as np
import data
from matplotlib import pyplot as plt


def draw_picture():
    img = Image.fromarray(np.uint8(data.table))
    img.show(img)
    # plt.imshow(data.table, interpolation='nearest')
    # plt.show()



