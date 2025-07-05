
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Cargar datos
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

# Entrenar modelo
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Guardar modelo
joblib.dump(clf, 'model/model.pkl')