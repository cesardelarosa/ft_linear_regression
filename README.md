# ft\_linear\_regression

*Proyecto del currículum de "Algo & IA & Data" del OuterCore del Campus 42 Madrid. Realizado por el estudiante César de la Rosa Sobrino (cde-la-r).*

## Descripción del proyecto

Debemos predecir la relación entre una variable independiente (X) y una variable dependiente (Y) a partir de un dataset dado. Este típico problema de regresión lineal que solemos resolver de forma analítica y cerrada por las ecuaciones de ajuste de [mínimos cuadrados](https://es.wikipedia.org/wiki/M%C3%ADnimos_cuadrados) va a ser resuelta en este caso por el algoritmo del [descenso del grediente](https://es.wikipedia.org/wiki/Descenso_del_gradiente). Este algoritmo es, en este caso, mucho menos eficiente, pero aprender a implementarlo en un caso tan sencillo nos ayuda a comprender la base fundamental del [Aprendizaje automático](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico).

En nuestro caso específico debemos obtener de los datos de `data.csv` el kilometraje de un coche y su precio, obteniendo su correlación. Debemos crear por tanto dos programas:

1. Programa para obtener la estimación del precio en función del kilometraje, aplicando la fórmula:

$$ f(X) = \theta_0 + (\theta_1 * X) $$

con parámetros iniciales $\theta_0$ y $\theta_1$ nulos.

2. Entrenamiento del modelo, optimizar el valor de los parámetros con las fórmulas:

$$ \theta_0 = $\eta * \frac{1}{n} \sum^(m-1)_i(i=0) f(X[i]) - Y[i]$

$$ \theta_1 = $\eta * \frac{1}{n} \sum^(m-1)_i(i=0) f(X[i] - Y[i]) * X[i]$

Y vamos actualizando los valores de los parámetros.

Como parte bonus debemos representar en un gráfico los datos, la linea ajustada y el cálculo de precisión (R^2).
