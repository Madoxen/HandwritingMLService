from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
from nnetwork import Network
import numpy as np

class MLService():
   #initialize network with 28*28 input neurons (image size)20 hidden neurons and 10 output neurons
    net = Network(sizes=(784,20,10))

    #prepare incoming image to fit it in 28x28 pixs
    def prepareImage(self,img_data):
        image = Image.frombytes('L', (img_data['width'], img_data['height']), bytes(img_data['array']))
        image = image.resize((28,28), resample=Image.BICUBIC)
        enhancer = ImageEnhance.Contrast(image)
        enhancer.enhance(5.0)
        enhancer.enhance(-5.0)
        image = enhancer.enhance(5.0)
        image = ImageOps.invert(image)
        return list(image.getdata())


    def evaluate(self, img_data):
        image = np.asarray(self.prepareImage(img_data))
        image = image // 255.0
        activations = self.net.feedforward(image)
        result = []
        #make average of activations incoming to the output layer
        for a in activations:
           result.append(np.average(a))
        print(result)
        return result; 


