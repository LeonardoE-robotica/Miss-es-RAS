import cv2 # biblioteca Opencv em Python
imagem = cv2.imread('gato.jpg') #lê a imagem

for y in range(0, imagem.shape[0], 1):  # percorre as linhas de 1 em 1 pixel
    for x in range(0, imagem.shape[1], 1):  # percorre as colunas de 1 em 1 pixel
        imagem[y, x] = (0, (x*y) % 256, 0) # só haverá canal de cor verde e será o resto da multiplicação entre x e y divido por 256 

cv2.imshow("Imagem modificada", imagem) # apresenta a imagem
cv2.waitKey(0) # espera pressionar qualquer tecla

