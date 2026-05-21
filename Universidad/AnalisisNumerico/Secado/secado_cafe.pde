{ ==============================================================================
  Secado Solar de Café en Marquesina — Modelo Difusivo PDE 1D
  FlexPDE 6.x / 7.x

  Facultad de Ingeniería — Rionegro, Antioquia, Colombia

  CORRECCIONES APLICADAS:
  1. Variable de temperatura renombrada a 'Temp' — 'T' es variable reservada
     en FlexPDE (representa el tiempo). Causa: "Duplicate use of time variable T".
  2. Estructura BOUNDARIES corregida: NATURAL declarado antes del segmento.
  3. Frontera en x = 0 (fondo) con flujo cero explícito.
  4. MONITORS usa HISTORY (sintaxis válida en FlexPDE).
  5. POINT(0.04) redundante removido.
  ============================================================================== }

TITLE 'Secado Solar de Cafe en Marquesina — Modelo Difusivo PDE 1D'

COORDINATES
  cartesian1    { Sistema cartesiano unidimensional (eje X = profundidad z) }

SELECT
  errlim = 1.0e-5    { Tolerancia de error relativo }
  ngrid  = 80        { Nodos iniciales en la malla }

VARIABLES
  W      { Contenido de humedad base seca [kg_agua/kg_seco] }
  Temp   { Temperatura del lecho de café [K] — NO usar 'T' (reservada = tiempo) }

DEFINITIONS
  { --- Propiedades termofísicas del lecho de café --- }
  rho_b    = 350.0     { Densidad aparente seca [kg/m³] }
  Cp_b     = 1800.0    { Calor específico [J/(kg·K)] }
  k_b      = 0.15      { Conductividad térmica [W/(m·K)] }
  D_eff    = 5.0e-10   { Difusividad efectiva de humedad [m²/s] }
  lambda_e = 2.26e6    { Calor latente de evaporación [J/kg] }

  { --- Coeficientes de transferencia en la superficie --- }
  h_conv   = 15.0      { Coeficiente convectivo de calor [W/(m²·K)] }
  h_mass   = 5.0e-5    { Coeficiente de transferencia de masa [m/s] }
  W_eq     = 0.12      { Humedad de equilibrio [kg/kg] }

  { --- Temperatura ambiente senoidal (ciclo diario) --- }
  T_min    = 288.15    { 15 °C [K] }
  T_max    = 301.15    { 28 °C [K] }
  T_med    = (T_min + T_max) / 2.0
  amp_T    = (T_max - T_min) / 2.0
  omega    = 2.0 * pi / 86400.0    { Frecuencia angular diaria [rad/s] }
  T_amb    = T_med + amp_T * sin(omega * t - pi / 2.0)

  { --- Condiciones iniciales --- }
  W_ini    = 0.55      { Humedad inicial base seca [kg/kg] }
  T_ini    = 288.15    { Temperatura inicial [K] = 15 °C }

INITIAL VALUES
  W    = W_ini
  Temp = T_ini

EQUATIONS
  { Difusión de humedad (variable W) }
  W: dt(W) = dx(D_eff * dx(W))

  { Conducción de calor (variable Temp) }
  Temp: rho_b * Cp_b * dt(Temp) = dx(k_b * dx(Temp))

BOUNDARIES
  REGION 1
    { ------------------------------------------------------------------ }
    { Punto x = 0: Fondo de la cama — Impermeable y Adiabático           }
    { FlexPDE asume NATURAL = 0 por defecto si no se especifica nada.     }
    { Se declara explícitamente para claridad y compatibilidad.           }
    { ------------------------------------------------------------------ }
    START(0.0)
      NATURAL(W) = 0
      NATURAL(Temp) = 0

    { ------------------------------------------------------------------ }
    { Segmento: desde x = 0 hasta x = 0.04 m (interior del lecho)        }
    { ------------------------------------------------------------------ }
    LINE TO (0.04)

    { ------------------------------------------------------------------ }
    { Punto x = 0.04: Superficie expuesta al ambiente                    }
    {                                                                      }
    { NATURAL(W)  → Flujo de humedad saliente por evaporación             }
    { NATURAL(T)  → Pérdida de calor por convección + evaporación         }
    {                                                                      }
    { Convenio FlexPDE: NATURAL = flujo hacia AFUERA del dominio          }
    {   Flujo_W   = h_mass * (W - W_eq)           [kg/(m²·s)]            }
    {   Flujo_T   = h_conv*(T - T_amb)            [W/m²]  convección      }
    {             + lambda_e * rho_b * h_mass*(W - W_eq)  [W/m²] evap.    }
    { ------------------------------------------------------------------ }
      NATURAL(W) = h_mass * (W - W_eq)
      NATURAL(Temp) = h_conv * (Temp - T_amb) + lambda_e * rho_b * h_mass * (W - W_eq)

TIME 0 TO 28800    { Simulación: 0 a 8 horas (28800 segundos) }

MONITORS
  { Historiales en tiempo real durante la simulución }
  HISTORY(W) AT (0.040) AT (0.020) AT (0.000)
  HISTORY(Temp - 273.15) AT (0.040) AT (0.000)

PLOTS
  { --- Perfiles finales de profundidad al terminar t = 8 h --- }
  ELEVATION(W) FROM (0) TO (0.04)
    TITLE 'Perfil de humedad W(z) al finalizar t = 8 h'
    XLABEL 'Profundidad z [m]'
    YLABEL 'W [kg/kg bs]'

  ELEVATION(Temp - 273.15) FROM (0) TO (0.04)
    TITLE 'Perfil de temperatura T(z) al finalizar t = 8 h'
    XLABEL 'Profundidad z [m]'
    YLABEL 'T [°C]'

  { --- Mapas espacio-temporales --- }
  SURFACE(W)
    TITLE 'Evolucion espacio-temporal de la humedad W(z,t)'

  SURFACE(Temp - 273.15)
    TITLE 'Evolucion espacio-temporal de la temperatura T(z,t) [C]'

  { --- Historiales temporales en diferentes profundidades --- }
  HISTORY(W) AT (0.040) AT (0.030) AT (0.020) AT (0.010) AT (0.000)
    TITLE 'Evolucion de la humedad W en diferentes profundidades'
    XLABEL 'Tiempo [s]'
    YLABEL 'W [kg/kg bs]'

  HISTORY(Temp - 273.15) AT (0.040) AT (0.000)
    TITLE 'Evolucion de la temperatura del cafe [C]'
    XLABEL 'Tiempo [s]'
    YLABEL 'T [C]'

  HISTORY(T_amb - 273.15)
    TITLE 'Evolucion de la temperatura ambiente [C]'
    XLABEL 'Tiempo [s]'
    YLABEL 'T_amb [C]'

END
