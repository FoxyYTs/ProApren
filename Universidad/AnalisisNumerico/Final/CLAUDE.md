# CLAUDE.md — Registro de proceso: Parcial Métodos Numéricos

**Examen:** Parcial I — Métodos Numéricos (S1 2026)  
**Institución:** Politécnico Colombiano Jaime Isaza Cadavid  
**Profesor:** Víctor Hugo Borda Yepes  
**Estudiante:** FoxyYTs  

---

## Contexto del problema

Circuito RLC serie en régimen transitorio. La tasa de cambio de carga es:

$$\frac{dq}{dt} = -\frac{1}{R(q) \cdot C} \cdot \sqrt{\frac{2 \cdot E(q)}{C}}$$

Parámetros:
- `C = 2.5e-4 F`
- `E(q) = q² / (2C)` (relación lineal simplificada)
- `q(0) = 6e-3 C` (condición inicial)
- `q_final = 0 C`

Datos experimentales R(q):
| q [C]   | 6e-3 | 5e-3 | 4e-3 | 3e-3 | 2e-3 | 1e-3 | 0    |
|---------|------|------|------|------|------|------|------|
| R(q)[Ω] | 1.17 | 0.97 | 0.67 | 0.45 | 0.32 | 0.18 | 0.05 |

---

## Derivación analítica de f(q)

Sustituyendo E(q) = q²/(2C) en dq/dt:

```
dq/dt = -1/(R(q)*C) * sqrt(2*(q²/2C)/C)
      = -1/(R(q)*C) * sqrt(q²/C²)
      = -1/(R(q)*C) * (q/C)       [q > 0]
      = -q / (R(q) * C²)
```

Separando variables para obtener T:

```
dt = -R(q)*C² / q * dq
T  = ∫₀^{6e-3}  R(q)*C² / q  dq    [límites invertidos por el signo]
   = ∫₀^{6e-3}  f(q) dq
```

Donde:  **f(q) = R(q) · C² / q**

---

## Archivos del proyecto

| Archivo        | Descripción                                              | Estado     |
|----------------|----------------------------------------------------------|------------|
| ENUNCIADO.md   | Enunciado original del parcial                           | ✅ listo   |
| CLAUDE.md      | Este archivo — registro y contexto del proceso           | ✅ listo   |
| problema1.py   | Regla del Trapecio Compuesta para calcular T             | ✅ listo   |
| problema2.py   | Método de Euler hacia adelante para simular q(t)         | ✅ listo   |
| informe.tex    | Documento LaTeX con procedimientos completos             | ✅ listo   |

---

## Problema 1 — Integración Numérica

**Método:** Regla del Trapecio Compuesta  
**Δq = 1e-3 C**, 6 subintervalos  
**Fórmula:**

```
T ≈ (Δq/2) * [f(q₀) + 2·f(q₁) + 2·f(q₂) + ... + 2·f(q_{n-1}) + f(qₙ)]
```

**f(q) = R(q) · C² / q**

Nodo especial: q=0 → f(0) es indefinido (división por 0).  
Se usa límite: cuando q→0, R(q)→0.05, f(q)→0 (se justifica en el informe).

---

## Problema 2 — EDO con Euler hacia adelante

**Método:** Forward Euler con Δt = 5e-4 s  
**Recurrencia:** `q_{i+1} = q_i + φ(t_i, q_i) · Δt`  
**φ(t,q) = dq/dt = -q / (R(q) · C²)`

**Interpolación:** Para R(q) en valores intermedios se usa interpolación lineal entre los puntos tabulados más cercanos.

**Iteraciones manuales:**
- t=0: q₀ = 6e-3 C, R(6e-3) = 1.17 Ω (punto exacto, no se interpola)
- t=0.5ms: q₁ calculado en el script
- t=1.0ms: q₂ calculado en el script

---

## Estado de avance

- [x] Derivación analítica de f(q)
- [x] problema1.py creado y verificado
- [x] problema2.py creado y verificado
- [x] informe.tex creado
- [ ] Compilar PDF del informe (requiere LaTeX instalado: `pdflatex informe.tex`)

---

## Cómo retomar si se cortan los tokens

1. Leer este CLAUDE.md para contexto completo
2. Leer ENUNCIADO.md para los enunciados originales
3. Los archivos .py son autónomos y ejecutables con `python problema1.py` / `python problema2.py`
4. El informe.tex se compila con `pdflatex informe.tex`
