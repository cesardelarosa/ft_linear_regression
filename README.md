# ft\_linear\_regression

*Proyecto del currículum de "Algo & IA & Data" del OuterCore de 42 Madrid.*  
*Autor: César de la Rosa Sobrino (cde-la-r)*

## Descripción del proyecto

El objetivo es predecir la relación entre una variable independiente ($X$, kilometraje) y una variable dependiente ($Y$, precio) a partir de un dataset `data.csv`.

Este típico problema de regresión lineal simple suele resolverse de forma analítica y cerrada mediante las ecuaciones de ajuste por [mínimos cuadrados](https://es.wikipedia.org/wiki/M%C3%ADnimos_cuadrados), pero en este proyecto implementamos desde cero el algoritmo del [descenso del gradiente](https://es.wikipedia.org/wiki/Descenso_del_gradiente). Aunque analíticamente es menos eficiente para una sola variable, su implementación no permite entender la base fundamental de la optimización en aprendizaje automático.

---

## Requisitos

El proyecto requiere un entorno Unix/Linux y las herramientas básicas de Python para construir el entorno virtual gestionado por el `Makefile`:

* **Python 3.10+** (incluyendo el módulo estándar `venv`).
* **GNU Make** (para la gestión automática del entorno y las ejecuciones).
* Paquetes externos (instalados automáticamente en `.venv` desde `requirements.txt`):
  * `matplotlib` (para la visualización gráfica en `plot.py`).

---

## Uso

El proyecto incluye un `Makefile` que gestiona el entorno virtual de Python y sus dependencias de forma aislada:

### 1. Crear el entorno virtual e instalar dependencias
```bash
make
```

### 2. Entrenar el modelo
```bash
make train
```

### 3. Predecir un precio
```bash
make predict
```

### 4. Visualizar datos y recta
```bash
make plot
```

### 5. Evaluar precisión de la recta
```bash
make precision
```

### 6. Limpieza de cachés o entorno
```bash
make clean    # Elimina bytecode y cachés de Python
make fclean   # Elimina params.json y el entorno virtual .venv
```

## Modelo y fórmulas

La función de estimación (hipótesis) es:

$$h_\theta(x) = \theta_0 + \theta_1 x$$

Con parámetros iniciales $\theta_0 = 0$ y $\theta_1 = 0$.

Para ajustar los parámetros, se optimizan iterativamente mediante descenso de gradiente por lotes (*batch gradient descent*), actualizando ambos pesos de forma simultánea en cada iteración:

$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$

$$\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

Donde:
* $\alpha$ es la tasa de aprendizaje (*learning rate*).
* $m$ es el número total de muestras en el dataset.
* $x^{(i)}$ e $y^{(i)}$ representan el kilometraje y precio reales del ejemplo $i$-ésimo.

> **Nota:** Debido a la diferencia de escala entre los valores de kilometraje ($10^4 - 10^5$) y precio ($10^3$), las características se normalizan durante el entrenamiento para garantizar la convergencia del algoritmo, desnormalizando posteriormente los parámetros al guardarlos en `params.json`.

---

## Estructura del repositorio

* `predict.py`: Solicita un kilometraje por terminal y predice el precio utilizando los parámetros guardados en `params.json` (o $0$ si el modelo no ha sido entrenado).
* `train.py`: Lee `data.csv`, ejecuta el descenso de gradiente y persiste los pesos resultantes en `params.json`.
* `plot.py`: Visualiza la dispersión de datos reales y la recta de regresión ajustada.
* `precision.py`: Evalúa el rendimiento del modelo calculando el coeficiente de determinación ($R^2$) y el error absoluto medio (MAE).
* `utils.py`: Funciones compartidas de lectura de datos, parámetros y cálculo de la hipótesis.
