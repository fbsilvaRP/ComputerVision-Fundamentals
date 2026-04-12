#Primeiros passos com a biblioteca OpenCV
#Feito por Felipe Braga, em 12 de abril de 2026

#contato: felipebsilvarp@usp.br

import cv2

#A imagem precisa estar no mesmo diretório do programa

#Obtém a imagem a partir do endereço da imagem e de sua extensão
img = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

print(img.shape)
print(img[0,0])


cv2.imshow("Cat", img)

cv2.waitKey(0) #Congela o programa
cv2.destroyAllWindows() #Fecha a janela
