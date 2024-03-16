import cv2 # biblioteca Opencv em Python
imagem = cv2.imread('gato.jpg') #lê a imagem
(b, g, r) = imagem[0, 0]  # veja que a ordem BGR e não RGB

print('O pixel (0, 0) tem as seguintes cores: ')
print('Vermelho: ', r, 'Verde: ', g, 'Azul: ', b) # apresentará os valores dos canais no ponto x = 0 e y = 0
