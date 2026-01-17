import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [18,2],
    [20,4],
    [22,6],
    [25,8],
    [30,9],
    [35,10]
])

y = np.array(['Reprobado', 'Reprobado','Aprobado','Aprobado','Aprobado','Aprobado'])

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

nuevo = np.array([[23,5]])
prediccion = modelo.predict(nuevo)

print("Resultado para el nuevo estudiante:", prediccion[0])


for etiqueta in np.unique(y):
    plt.scatter(
        X[y == etiqueta][:, 0],
        X[y == etiqueta][:, 1],
        label=etiqueta
    )

    plt.scatter(nuevo[:,0], nuevo[:,1], color='black', marker='x', s=100, label='Nuevo')
    plt.xlabel('Edad')
    plt.ylabel('Horas de estudio')
    plt.title('Clasificación KNN')
    plt.legend()
    plt.show()