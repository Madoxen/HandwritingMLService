import sys
import data_loader
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
import numpy as np
sys.path.append("../")
from api.nnetwork import Network


n = Network(sizes=[28*28, 30, 10])
#n = Network(path="network.json")
print("School: Loading data...")
data = data_loader.load_data("ml_data/train-images", "ml_data/train-labels")
test_data = data_loader.load_data("ml_data/test-images", "ml_data/test-labels")
print("Data loaded")
print(data[0][0]*255)


image_data = (data[0][0]*255).reshape((28,28))
i = Image.fromarray(image_data, mode='L')
i.show()

n.SGD(data, 30, 10, 0.5)
n.dump()

