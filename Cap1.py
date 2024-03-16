import cv2 # biblioteca Opencv em Python

imagem = cv2.imread('gato.jpg') #lê a imagem

print('Largura em pixels: ', end='') # O termo end= '' faz com que a resposta fique ao lado do print
print(imagem.shape[1])  # largura da imagem
print('Altura em pixels: ', end='') # O termo end= '' faz com que a resposta fique ao lado do print
print(imagem.shape[0])  # altura da imagem
print('Quantidade de canais: ', end='') # O termo end= '' faz com que a resposta fique ao lado do print
print(imagem.shape[2]) #número de canais (vermelho, verde, azul)

cv2.imshow("Nome da janela", imagem) # apresenta a imagem
cv2.waitKey(0)  # espera pressionar qualquer tecla

cv2.imwrite("gato.jpg", imagem) #salva a imagem
