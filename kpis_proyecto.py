COLUMNAS_KPI = ["viajes", "minutos"]  # columnas que usa su KPI, p. ej. ["viajes", "minutos"]

def kpi_proyecto(datos):
    # [Trabajo del estudiante] Paso 5: su KPI. Sume primero y divida después si es un cociente.
    return datos.minutos.sum() / datos.viajes.sum()  # minutos promedio por viaje
