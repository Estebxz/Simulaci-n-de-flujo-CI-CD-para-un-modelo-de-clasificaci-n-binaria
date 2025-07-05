from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Cargar datos
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Cargar modelo
model = joblib.load('model/model.pkl')

# Predecir
preds = model.predict(X_test)

# Calcular precisión
acc = accuracy_score(y_test, preds)
print(f"Precisión del modelo: {acc:.2f}")

# Asegurar que alcanza cierto umbral
assert acc >= 0.80, f"Precisión insuficiente: {acc:.2f}"