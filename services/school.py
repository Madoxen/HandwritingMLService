import sys
import data_loader
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
sys.path.append("../")

from api.nnetwork import Network

n = Network(sizes=(28*28, 20, 10))
n.dump()
n = Network(path="network.json")
data = data_loader.load_data("ml_data/train-images", "ml_data/train-labels")
print(len(data))
print(data[0][0])
image = Image.frombytes('L', (28, 28), bytes(data[0][0]))


