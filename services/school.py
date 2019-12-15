import sys
import data_loader
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
import numpy as np
sys.path.append("../")
from api.nnetwork import Network

n = Network(sizes=(28*28, 20, 10))
n.dump()
#n = Network(path="network.json")
print("School: Loading data...")
data = data_loader.load_data("ml_data/train-images", "ml_data/train-labels")
test_data = data_loader.load_data("ml_data/test-images", "ml_data/test-labels")
print("Data loaded")
n.learn(data, 3.0, 10, 10, test_data)
n.dump()

