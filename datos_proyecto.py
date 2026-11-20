import pandas as pd

ARCHIVO = "alquiler_bicicletas.csv"  # nombre de su CSV dentro de mi_tablero/

def limpiar_proyecto(crudo):
    limpio = crudo.copy()
    limpio["estacion"] = limpio.estacion.str.strip().str.title()  # " Terminal" y "terminal" -> "Terminal"
    limpio = limpio.drop_duplicates()  # filas repetidas
    limpio["minutos"] = pd.to_numeric(limpio.minutos, errors="coerce")  # "sin dato" -> vacío
    limpio = limpio.dropna(subset=["minutos"])  # sin dato de minutos
    limpio = limpio[limpio.viajes >= 0]  # -1 es un centinela
    limpio["fecha"] = pd.to_datetime(limpio.fecha)
    limpio["mes"] = limpio.fecha.dt.strftime("%Y-%m")
    return limpio

def cargar_proyecto(carpeta="."):
    return limpiar_proyecto(pd.read_csv(f"{carpeta}/{ARCHIVO}"))
