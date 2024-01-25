import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Crear los datos de entrenamiento y prueba
x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [2]])
x_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_test = np.array([[0], [1], [1], [2]])

# Crear el modelo de la red neuronal
modelo = Sequential()
modelo.add(Dense(units=4, input_dim=2, activation='relu'))
modelo.add(Dense(units=1, activation='linear'))

# Compilar el modelo
modelo.compile(loss='mse', optimizer='adam', metrics=['mse'])

# Entrenar el modelo
modelo.fit(x_train, y_train, epochs=10000, batch_size=4,
           validation_data=(x_test, y_test))

# Evaluar el modelo
scores = modelo.evaluate(x_test, y_test)
print("\n%s: %.2f" % (modelo.metrics_names[1], scores[1]))

# Hacer predicciones con el modelo
predicciones = modelo.predict(x_test)
print(predicciones)
