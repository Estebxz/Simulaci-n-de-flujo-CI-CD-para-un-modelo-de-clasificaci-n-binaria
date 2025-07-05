# Simulación de flujo CI/CD para un modelo de clasificación binaria

Es una demostracion sencilla de un flujo aplicado a un modelo de clasificación usando `RandomForestClassifier` con el dataset Iris de `scikit-learn`, tiene una estructura tal que asi...:

`data/dataset.csv  
model/train.py  
tests/test_metrics.py  
buildspec.yml  
requirements.txt  
README.md`

## Etapas del proyecto

1. **Entrenamiento del Modelo (`train_model.py`)**  
   Entrena un modelo de clasificación con datos del Iris Dataset y lo guarda en un archivo `.pkl` usando `joblib`.

2. **Evaluación del Modelo (`test_metrics.py`)**  
   Carga el modelo guardado y evalúa su rendimiento sobre un conjunto de prueba utilizando `accuracy_score`. Se incluye una aserción para asegurar que la precisión sea al menos del 80%.

3. **Simulacion de integracion continua(CI)**   
   se simula manualmente ejecutando `test_metrics.py` después de cada cambio.

4. **Simulacion de despliegue(CD)**    
   Se simula en consola donde la precision del modelo es: 1.00 

## Conclusion

- Al desarrollar este proyecto, comprendí de forma más práctica cómo funciona el flujo CI/CD y su importancia para mantener la calidad y consistencia en los proyectos. Además, profundicé en el ciclo de vida de los modelos de machine learning, desde el entrenamiento y evaluación hasta su validación automatizada. Esta experiencia me ayudó a conectar conceptos teóricos con su aplicación real en procesos de integración y entrega continua.
<br />

> [!NOTE]
> Este contenido ha sido desarrollado con fines educativos como parte de una actividad estudiantil.
