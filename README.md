# Simulación de flujo CI/CD para un modelo de clasificación binaria

- Es una demostracion sencilla de un flujo aplicado a un modelo de clasificación usando `RandomForestClassifier` con el dataset Iris de `scikit-learn`, tiene una estructura tal que asi...:

ml-ci-cd-simulado/
├── data/
│   └── dataset.csv
├── model/
│   └── train.py
├── tests/
│   └── test_metrics.py
├── buildspec.yml
├── requirements.txt
└── README.md

## etapas del proyecto

1. **Entrenamiento del Modelo (`train_model.py`)**  
   Entrena un modelo de clasificación con datos del Iris Dataset y lo guarda en un archivo `.pkl` usando `joblib`.

2. **Evaluación del Modelo (`test_metrics.py`)**  
   Carga el modelo guardado y evalúa su rendimiento sobre un conjunto de prueba utilizando `accuracy_score`. Se incluye una aserción para asegurar que la precisión sea al menos del 80%.

3. **Simulacion de integracion continua(CI)**   
   se simula manualmente ejecutando `test_metrics.py` después de cada cambio.

4. **Simulacion de despliegue(CD)**    
   Se simula en consola donde la precision del modelo es: 1.00 

## Conclusion

- Al realizar el proyecto entendi mejor el tema principal (CI/CD), tambien profundize en el ciclo de vida de ML 

