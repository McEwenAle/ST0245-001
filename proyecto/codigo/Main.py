from Entrega1 import ImageCompression 
from Entrega2_3 import Image

def main():
    img = Image("/Users/alejandromcewen/Documents/Estudios/Semestre2/EstructurasDeDatosYAlgoritmosI/ST0245-001/proyecto/codigo/archivosCSV/ganadoEnfermoCSVs/cow.csv")
    print(img.losslessCompress())
    # imageCompression = ImageCompression()
    # imageCompression.importPhotos()
    # imageCompression.lossyCompress(2)
    # imageCompression.losslessCompress()
    # imageCompression.amplify(2)
    # imageCompression.export()
    
main()