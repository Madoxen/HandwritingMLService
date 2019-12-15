import sys
import os
import struct
import numpy as np

#loads data sets (MINST) in form of tuples that consist of input vector and desired output vector
def load_data(data_path, label_path):
    if not (os.path.isfile(data_path) and os.path.isfile(label_path)):
        print("Could not open one of provided files")
        return
    
    result = []

    #check if both files have the same length (ie. length field not byte-wise length)
    with open(data_path, 'rb') as data_file:
        with open(label_path, 'rb') as label_file:
            sizeI = int.from_bytes(data_file.read(8)[4:], byteorder="big")
            sizeL = int.from_bytes(label_file.read(8)[4:], byteorder="big")
            #read first 5 bytes (1st is magic number, 4 next are int in bigendian)
            if sizeI != sizeL: 
                print("data and label files are not matching in length")
                return #if both lengths are not equals stop
            #read data dimensions             
            rows = int.from_bytes(data_file.read(4), byteorder="big")
            cols = int.from_bytes(data_file.read(4), byteorder="big")

            label_bytes = label_file.read(sizeL)
            image_bytes = data_file.read(rows * cols * sizeI)
            for k in range(0, len(label_bytes)):
                img_data = []
                #compose input data vector
                for i in range(0, rows*cols):
                        img_data.append(image_bytes[i*(k+1)] // 255.0)
                output_vector = np.zeros((10,1))
                output_vector[label_bytes[k]] = 1.0
                result.append((img_data, output_vector))
    return result 
