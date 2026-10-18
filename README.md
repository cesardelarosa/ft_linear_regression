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

## Descenso del gradiente

El modelo aproxima la relación entre variables mediante la hipótesis lineal:

$$h_\theta(x) = \theta_0 + \theta_1 x$$

Para evaluar el error global se utiliza la función de coste del Error Cuadrático Medio (MSE) sobre las $m$ muestras del dataset:

$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=0}^{m-1} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2$$

El algoritmo minimiza $J(\theta_0, \theta_1)$ actualizando los parámetros en la dirección opuesta al gradiente:
 $$\boldsymbol{\theta} := \boldsymbol{\theta} - \alpha \nabla J$$
Aplicando la regla de la cadena obtenemos las derivadas parciales:

$$\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=0}^{m-1} \left( h_\theta(x^{(i)}) - y^{(i)} \right)$$

$$\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=0}^{m-1} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x^{(i)}$$

En cada época se realiza una actualización simultánea de ambos pesos:

$$\theta_0 := \theta_0 - \alpha \frac{\partial J}{\partial \theta_0}, \qquad \theta_1 := \theta_1 - \alpha \frac{\partial J}{\partial \theta_1}$$

El bucle se detiene cuando se alcanza el límite de iteraciones (`epochs`) o cuando la norma del gradiente converge por debajo de una tolerancia predefinida:

$$|\nabla J(\theta_0, \theta_1)| = \sqrt{(\frac{\partial J}{\partial \theta_0})^2 + (\frac{\partial J}{\partial \theta_1})^2} < \varepsilon$$

---

## Normalización y desnormalización

Dado que el kilometraje ($x \sim 10^5$) y el precio ($y \sim 10^3$) operan en órdenes de magnitud distintos, la superficie de coste se deforma en elipsoides alargados que provocan oscilaciones numéricas, frenando la convergencia. Se aplica escalado Min-Max bidimensional para confinar ambas variables al intervalo $[0, 1]$.

Definiendo $\Delta x = x_{\max} - x_{\min}$ y $\Delta y = y_{\max} - y_{\min}$:

$$x_{\text{norm}} = \frac{x - x_{\min}}{\Delta x}, \qquad y_{\text{norm}} = \frac{y - y_{\min}}{\Delta y}$$

Tras entrenar sobre los datos normalizados, el modelo produce parámetros óptimos $(\theta_0^{\text{norm}}, \theta_1^{\text{norm}})$ para predecir $\hat{y}_{\text{norm}}$:

$$\hat{y}_{\text{norm}} = \theta_0^{\text{norm}} + \theta_1^{\text{norm}} x_{\text{norm}}$$

Para que `predict.py` opere directamente sobre la escala real sin transformaciones adicionales ($\hat{y} = \theta_0 + \theta_1 x$), se sustituyen las definiciones Min-Max y se despeja $\hat{y}$:

$$\frac{\hat{y} - y_{\min}}{\Delta y} = \theta_0^{\text{norm}} + \theta_1^{\text{norm}} \left( \frac{x - x_{\min}}{\Delta x} \right)$$

$$\hat{y} = y_{\min} + \Delta y \cdot \theta_0^{\text{norm}} + \left( \theta_1^{\text{norm}} \frac{\Delta y}{\Delta x} \right) (x - x_{\min})$$

Reordenando los términos respecto a la variable $x$:

$$\hat{y} = \underbrace{\left( y_{\min} + \Delta y \cdot \theta_0^{\text{norm}} - \theta_1^{\text{norm}} \frac{\Delta y}{\Delta x} x_{\min} \right)}_{\theta_0} + \underbrace{\left( \theta_1^{\text{norm}} \frac{\Delta y}{\Delta x} \right)}_{\theta_1} x$$

De aquí resultan las fórmulas de desnormalización implementadas antes de persistir los pesos en `params.json`:

$$\theta_1 = \theta_1^{\text{norm}} \cdot \frac{\Delta y}{\Delta x}$$

$$\theta_0 = y_{\min} + \Delta y \cdot \theta_0^{\text{norm}} - \theta_1 x_{\min}$$

---

## Estructura del repositorio

* `predict.py`: Solicita un kilometraje por terminal y predice el precio utilizando los parámetros guardados en `params.json` (o $0$ si el modelo no ha sido entrenado).
* `train.py`: Lee `data.csv`, ejecuta el descenso de gradiente y persiste los pesos resultantes en `params.json`.
* `plot.py`: Visualiza la dispersión de datos reales y la recta de regresión ajustada.
* `precision.py`: Evalúa el rendimiento del modelo calculando el coeficiente de determinación ($R^2$) y el error absoluto medio (MAE).
* `utils.py`: Funciones compartidas de lectura de datos, parámetros y cálculo de la hipótesis.
