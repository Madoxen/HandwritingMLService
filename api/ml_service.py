from PIL import Image
from PIL import ImageEnhance

class MLService():
    
    #prepare incoming image to fit it in 28x28 pixs
    def prepareImage(self,img_data):
        image = Image.frombytes('L', (img_data['width'], img_data['height']), bytes(img_data['array']))
        image = image.resize((28,28), resample=Image.BICUBIC)
        enhancer = ImageEnhance.Contrast(image)
        enhancer.enhance(5.0).show()
        enhancer.enhance(-0.2).show()
        enhancer.enhance(0.2).show()
         

