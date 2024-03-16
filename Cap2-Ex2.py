import cv2 # biblioteca Opencv em Python

imagem = cv2.imread('gato.jpg') #lê a imagem
for y in range(0, imagem.shape[0]): # percorre as linhas
    for x in range(0, imagem.shape[1]): # percorre as colunas

        imagem[y, x] = (255, 0, 0) #as coordenadas x e y serão transformada para o espectro apenas azul puro

cv2.imshow("Imagem modificada", imagem) # apresenta a imagem

cv2.waitKey(0) # espera pressionar qualquer tecla
