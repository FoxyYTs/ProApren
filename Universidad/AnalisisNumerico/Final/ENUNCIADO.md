# Examen Parcial I - Métodos Numéricos (S1 2026)
**Institución:** Politécnico Colombiano Jaime Isaza Cadavid  
**Facultad:** Ingeniería  
**Programa:** Ingeniería en Informática  
**Profesor:** Víctor Hugo Borda Yepes  
**Código Formato:** FD-GC195 (Versión 03)  

> **Nota importante:** El parcial debe ser sustentado en la siguiente clase. La asistencia a la sustentación es obligatoria.

---

## 1. Problema [2.50 Puntos] - Enfoque de Integración Numérica y Análisis de Errores

### Contexto
Como parte de un proyecto de consultoría en optimización de sistemas de filtrado de armónicos y calidad de la energía para una planta industrial, se requiere analizar la disipación de la energía y el tiempo de descarga en un circuito RLC serie en régimen transitorio (descarga de un capacitor a través de una resistencia y una inductancia).

Bajo las leyes de Kirchhoff, la corriente transitoria $i(t)$ durante la descarga responde a una ecuación diferencial no lineal o de parámetros dependientes si los componentes se saturan. Para este análisis dinámico, se ha determinado que el tiempo total $T$ requerido para que la carga del capacitor disminuya desde un valor inicial hasta un nivel seguro se puede modelar mediante la tasa de cambio de la carga $q$ respecto al tiempo:

$$\frac{dq}{dt} = -\left[ \frac{1}{R(q) \cdot C} \right] \cdot \sqrt{\frac{2 \cdot E(q)}{C}}$$

**Donde:**
* $q$: Carga instantánea en el capacitor $[C]$.
* $C$: Capacitancia fija del sistema ($C = 2.5 \times 10^{-4} \text{ F}$).
* $E(q)$: Energía remanente en el campo eléctrico $[J]$.
* $R(q)$: Resistencia dinámica del circuito $[\Omega]$, la cual varía de forma no lineal debido al calentamiento térmico por efecto Joule según el nivel de carga remanente.

El departamento de instrumentación y metrología ha medido experimentalmente el comportamiento de la resistencia no lineal $R(q)$ para diferentes niveles de carga discretos mediante sensores térmicos y de corriente, obteniendo el siguiente cuadro de datos:

#### Cuadro 1: Resistencia dinámica en función de la carga
| Carga $q$ $[C]$ | $6 \times 10^{-3}$ | $5 \times 10^{-3}$ | $4 \times 10^{-3}$ | $3 \times 10^{-3}$ | $2 \times 10^{-3}$ | $1 \times 10^{-3}$ | $0$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$R(q)$ $[\Omega]$** | 1.17 | 0.97 | 0.67 | 0.45 | 0.32 | 0.18 | 0.05 |

* **Condición inicial:** En el instante $t = 0 \text{ s}$, el capacitor cuenta con una carga inicial máxima de $q(0) = 6 \times 10^{-3} \text{ C}$.

### Se solicita:

1.  **Desarrollo Analítico:** Realice la separación de variables de la ecuación diferencial para expresar el tiempo total de descarga ($T$) necesario para ir desde $q = 6 \times 10^{-3} \text{ C}$ hasta $q = 0 \text{ C}$ en forma de una integral definida: 
    
    $$T = \int_{0}^{6 \times 10^{-3}} f(q) \, dq$$
    
    Deduzca analíticamente la función $f(q)$ y tabule sus valores numéricos para cada punto del Cuadro 1 (asuma una relación lineal simplificada para la energía $E(q) = \frac{q^2}{2C}$ si requiere sustitución).

2.  **Aproximación Numérica:** A partir de los datos tabulados, determine el tiempo total que tarda el circuito en descargarse empleando el método de la **Regla del Trapecio Compuesta** ($\Delta q = 1 \times 10^{-3} \text{ C}$). Exprese el resultado final en milisegundos ($\text{ms}$).

3.  **Análisis de Errores:** En su solución escrita, conceptualice y discuta cómo afectan a este cálculo los siguientes conceptos matemáticos aprendidos en clase: *Error de corte, Error por truncamiento, Error por redondeo, Error absoluto y Error relativo*. Presente un cuadro analítico donde evalúe el impacto cualitativo o cuantitativo de estos errores sobre el resultado de la descarga del circuito.

---

## 2. Problema [2.50 Puntos] - Enfoque de Ecuaciones Diferenciales Ordinarias (EDO)

### Contexto
En lugar de transformar el fenómeno en un problema de acumulación (integración), un enfoque alternativo consiste en resolver la ecuación diferencial directamente hacia adelante en el tiempo para monitorear la tasa de decremento de la carga en el circuito paso a paso.

Para este propósito, se desea aproximar el descenso de la carga eléctrica utilizando el **Método de Euler hacia adelante (Forward Euler)**, definido matemáticamente por la relación de recurrencia:

$$q_{i+1} = q_i + \phi(t_i, q_i) \cdot \Delta t$$

Donde $\phi(t, q) = \frac{dq}{dt}$ corresponde a la función de la derivada dada en el Problema 1. Establezca un tamaño de paso de tiempo fijo de $\Delta t = 0.5 \text{ ms}$ ($5 \times 10^{-4} \text{ s}$).

### Se solicita:

1.  **Estrategia Algorítmica y Acoplamiento:** Dado que el término de la resistencia dinámica $R(q)$ solo se conoce para valores discretos y equiespaciados de la carga ($q = 0, 1\times10^{-3}, 2\times10^{-3}, \dots, 6\times10^{-3} \text{ C}$), explique detalladamente qué método numérico complementario (por ejemplo, *Interpolación Lineal* o *Polinomios de Lagrange*) debería integrar en su código si, en un paso de tiempo cualquiera, el algoritmo de Euler requiere evaluar la función en una carga intermedia no tabulada (ej. $q = 5.42 \times 10^{-3} \text{ C}$).

2.  **Simulación Manual:** Realice de forma manual y organizada las primeras dos (2) iteraciones del método de Euler hacia adelante. Calcule con precisión:
    * La carga $q_1$ en el tiempo $t = 0.5 \text{ ms}$.
    * La carga $q_2$ en el tiempo $t = 1.0 \text{ ms}$.
    
    *Nota: Para estas dos primeras iteraciones, justifique rigurosamente si requiere o no aplicar interpolación sobre el Cuadro 1.*

3.  **Análisis Compartivo Crítico:** Si tuviera que extender el método numérico hasta que el capacitor se descargue por completo ($q = 0$), compare ambos enfoques (*Regla del Trapecio Compuesta del Problema 1* frente al *Método de Euler del Problema 2*). ¿Cuál de los dos métodos considera que acumulará un mayor error de truncamiento global debido a la naturaleza discreta de los datos experimentales del circuito? Justifique su respuesta desde la teoría matemática de convergencia y estabilidad de métodos numéricos.