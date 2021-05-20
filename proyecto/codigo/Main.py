from Entrega1 import ImageCompression 

def main():
    imageCompression = ImageCompression()
    imageCompression.importPhotos(5,5)
    imageCompression.compress(2)
    # imageCompression.amplify(2)
    imageCompression.export()

main()