TITLE 'Secado Solar de Cafe en Marquesina - Modelo Difusivo PDE 1D'

{
  Dominio 1D: x en [0, 0.04 m]  (profundidad de la cama de cafe)
    x = 0.00 m  ->  fondo (impermeable, adiabatico)
    x = 0.04 m  ->  superficie expuesta al aire

  Variables:
    W  [kg_agua / kg_seco] : humedad base seca
    T  [K]                 : temperatura del lecho

  Ecuaciones:
    dW/dt = D_eff * d2W/dx2
    rho * Cp * dT/dt = k * d2T/dx2

  Condiciones de borde superficie (x = 0.04 m):
    D_eff * dW/dx = -h_m * (W - W_eq)       evaporacion
    k * dT/dx     =  h_c * (T - T_amb) + lambda * rho * h_m * (W - W_eq)

  Condiciones de borde fondo (x = 0):
    dW/dx = 0   impermeable
    dT/dx = 0   adiabatico

  Politecnico Colombiano Jaime Isaza Cadavid
  Facultad de Ingenieria - Rionegro, Antioquia, Colombia
}

COORDINATES
  Xcart1

SELECT
  errlim = 1.0e-5
  ngrid  = 60

VARIABLES
  W    { humedad base seca [kg/kg] }
  T    { temperatura [K] }

DEFINITIONS

  { --- Propiedades termofisicas del lecho de cafe --- }
  rho_b    = 350.0       { densidad aparente seca [kg/m3] }
  Cp_b     = 1800.0      { calor especifico [J/(kg K)] }
  k_b      = 0.15        { conductividad termica [W/(m K)] }
  D_eff    = 5.0e-10     { difusividad efectiva de humedad [m2/s] }
  lambda_e = 2.26e6      { calor latente de evaporacion [J/kg] }

  { --- Coeficientes de transferencia en la superficie --- }
  h_conv   = 15.0        { coeficiente convectivo [W/(m2 K)] }
  h_mass   = 1.0e-7      { coeficiente de transferencia de masa [m/s] }
  W_eq     = 0.12        { humedad de equilibrio [kg/kg] }

  { --- Temperatura ambiente senoidal (clima andino cafetero) --- }
  T_min  = 288.15        { 15 grados C en K }
  T_max  = 301.15        { 28 grados C en K }
  T_med  = (T_min + T_max) / 2
  amp_T  = (T_max - T_min) / 2
  T_amb  = T_med + amp_T * sin(2 * pi * t / 86400 - pi / 2)

EQUATIONS

  { Difusion de humedad }
  dt(W) = dx(D_eff * dx(W))

  { Conduccion de calor }
  rho_b * Cp_b * dt(T) = dx(k_b * dx(T))

BOUNDARIES

  REGION 1
    START(0)
    NATURAL(W) = 0
    NATURAL(T) = 0
    LINE TO (0.04)
    NATURAL(W) = -h_mass * (W - W_eq)
    NATURAL(T) =  h_conv * (T - T_amb) + lambda_e * rho_b * h_mass * (W - W_eq)

INITIAL VALUES
  W = 0.55
  T = 288.15

TIME 0 TO 28800

MONITORS
  ELEVATION(W)            AS 'Humedad W(x)'
  ELEVATION(T - 273.15)   AS 'Temperatura T(x) grados C'

PLOTS
  ELEVATION(W, x=0, x=0.04)
    AS 'Perfil de humedad W(x) t=8h'

  ELEVATION(T - 273.15, x=0, x=0.04)
    AS 'Perfil de temperatura T(x) grados C t=8h'

  HISTORY(W(0.040))  AS 'W superficie x=4cm'
  HISTORY(W(0.020))  AS 'W centro x=2cm'
  HISTORY(W(0.000))  AS 'W fondo x=0cm'

  HISTORY(T(0.040) - 273.15)  AS 'T superficie grados C'

END
