from Entrega1 import ImageCompression 
from Entrega2_3 import Image

def main():
    # img = Image("./archivosCSV/images.csv")
    # img.losslessCompress()
    # img.export("./archivosCSV/compressedmages.csv")
    imageCompression = ImageCompression()
    imageCompression.importPhotos(1,0)
    # imageCompression.lossyCompress(2)
    imageCompression.losslessCompress()
    # imageCompression.amplify(2)
    imageCompression.export()
    
main()