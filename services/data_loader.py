import sys
import os
import struct

#loads data sets (MINST) in form of tuples that consist of input vector and desired output vector
def load_data(data_path, label_path):
    if not os.path.isfile(data_path) or not os.path.isfile(label_path):
        print("Could not open one of provided files")
        return
    
    result = []

    #check if both files have the same length (ie. length field not byte-wise length)
    with open("data_path", 'b') as data_file:
        with open("label_path", 'b') as label_file:
            #read first 5 bytes (1st is magic number, 4 next are int in bigendian)
            if data_file.read(5)[1:] != label_file.read(5)[1:]:
                print("data and label files are not matching in length")
                return #if both lengths are not equals stop
            #read data dimensions             
            if sys.byteorder == "big":
                rows = int(data_file.read(4))
                cols = int(data_file.read(4))
            else:
                rows = int(data_file.read(4)[::-1])
                cols = int(data_file.read(4)[::-1])
            #since all other values are stored in one byte
            #we dont have to care about endianness
            label = int(label_file.read(1))
            while label:
                input_data = []
                #compose input data vector
                for i in range(0, rows):
                    for j in range(0, cols):
                        input_data.append(int(data_file.read(1)))
                result.append((input_data, label))
                label = int(label_file.read(1))
        return result 
