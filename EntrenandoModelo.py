from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3
)

model = KNeighborsClassifier()

model.fit(X_train, y_train)

print("Precisión:", model.score(X_test, y_test))

flor = X_test[0]               # una flor del examen
pred = model.predict([flor])   # el modelo adivina

print("Flor (medidas):", flor)
print("Predicción del modelo:", iris.target_names[pred[0]])
print("Respuesta real:", iris.target_names[y_test[0]])

