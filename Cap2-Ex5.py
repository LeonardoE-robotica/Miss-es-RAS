import cv2 # biblioteca Opencv em Python
imagem = cv2.imread('gato.jpg') #lê a imagem
for y in range(0, imagem.shape[0], 10):  # percorre as linhas de 10 em 10 pixels
    for x in range(0, imagem.shape[1], 10):  # percorre colunas 10 em 10 pixels
        imagem[y:y+5, x:x+5] = (0, 255, 255) #forma blocos de 5 pixels na coluna y e outro bloco de 5 pixels na linha x
                                            #permite apenas a cor vermelha pura e verde pura
cv2.imshow("Imagem modificada", imagem) # apresenta a imagem
cv2.waitKey(0) # espera pressionar qualquer tecla

