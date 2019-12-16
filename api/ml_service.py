from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
from nnetwork import Network
import numpy as np

class MLService():
   #initialize network with 28*28 input neurons (image size)20 hidden neurons and 10 output neurons
    net = Network(path="network.json")

    #prepare incoming image to fit it in 28x28 pixs
    def prepareImage(self,img_data):
        image = Image.frombytes('L', (img_data['width'], img_data['height']), bytes(img_data['array']))
        image = image.resize((28,28), resample=Image.BICUBIC)
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(5.0)
        image = enhancer.enhance(-5.0)
        image = enhancer.enhance(5.0)
        return list(image.getdata())


    def evaluate(self, img_data):
        raw_data = self.prepareImage(img_data)
        raw_data = np.array(raw_data)
        image = np.zeros((784,1))
        image = raw_data.flatten('F') 
        image = np.reshape(image,(784,1))
        image = image / 255.0
        print(image.shape)
        activations = self.net.feedforward(image)
        return [int(np.argmax(activations)), float(activations[np.argmax(activations)])]


