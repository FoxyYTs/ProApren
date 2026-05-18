TITLE 'Secado Solar de Cafe en Marquesina - Modelo Difusivo PDE 1D'

{
  Dominio 1D: x en [0, 0.04 m]  (profundidad de la cama de cafe)
    x = 0.00 m  ->  fondo (impermeable, adiabatico)
    x = 0.04 m  ->  superficie expuesta al aire

  Variable:
    W  [kg_agua / kg_seco] : humedad base seca

  Ecuacion:
    dW/dt = D_eff * d2W/dx2

  Condicion de borde superficie (x = 0.04 m):
    D_eff * dW/dx = -h_m * (W - W_eq)

  Condicion de borde fondo (x = 0):
    dW/dx = 0   (impermeable)

  Temperatura calculada analiticamente (cuasi-estacionaria):
    T_surf = T_amb - lambda_e * rho_b * h_mass * (W - W_eq) / h_conv

  Politecnico Colombiano Jaime Isaza Cadavid
  Facultad de Ingenieria - Rionegro, Antioquia, Colombia
}

COORDINATES
  Xcart1

SELECT
  errlim = 1.0e-5
  ngrid  = 60

VARIABLES
  W

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

  { --- Temperatura de superficie (cuasi-estacionaria) --- }
  J_ev   = lambda_e * rho_b * h_mass * (W - W_eq)
  T_surf = T_amb - J_ev / h_conv

EQUATIONS

  dt(W) = dx(D_eff * dx(W))

BOUNDARIES

  REGION 1
    START(0)
    NATURAL(W) = 0
    LINE TO (0.04)
    NATURAL(W) = -h_mass * (W - W_eq)

INITIAL VALUES
  W = 0.55

TIME 0 TO 28800

MONITORS
  ELEVATION(W)             AS 'Perfil de humedad W(x)'
  ELEVATION(T_surf - 273.15)  AS 'Temperatura superficie grados C'

PLOTS

  ELEVATION(W)
    AS 'Perfil de humedad W(x) al final t=8h'

  ELEVATION(T_surf - 273.15)
    AS 'Temperatura de superficie T(x) grados C al final t=8h'

  SURFACE(W)
    AS 'Evolucion espacio-temporal W(x,t)'

  HISTORY(W(0.040))  AS 'W superficie x=4cm'
  HISTORY(W(0.030))  AS 'W a 3cm'
  HISTORY(W(0.020))  AS 'W centro x=2cm'
  HISTORY(W(0.010))  AS 'W a 1cm'
  HISTORY(W(0.000))  AS 'W fondo x=0cm'

  HISTORY(T_surf - 273.15)  AS 'T superficie grados C'
  HISTORY(T_amb - 273.15)   AS 'T ambiente grados C'

END
