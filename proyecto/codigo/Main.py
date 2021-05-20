from Entrega1 import ImageCompression 

def main():
    imageCompression = ImageCompression()
    imageCompression.importPhotos(1,0)
    # imageCompression.lossyCompress(2)
    imageCompression.losslessCompress()
    # imageCompression.amplify(2)
    # imageCompression.export()
    
main()