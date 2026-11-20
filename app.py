import solara
from datos_proyecto import cargar_proyecto
from kpis_proyecto import kpi_proyecto
from vista_proyecto import diferencia_pct, Tarjeta, grafico_proyecto
from prediccion import evaluar_pronostico, veredicto

todos = cargar_proyecto()
COLUMNA_FILTRO = "estacion"  # cambie por la columna de su filtro
TOPE = todos.viajes.max()  # una sola escala para todas las opciones
opcion = solara.reactive("Todas")

@solara.component
def Page():
    datos = todos if opcion.value == "Todas" else todos[todos[COLUMNA_FILTRO] == opcion.value]
    dif = diferencia_pct(kpi_proyecto(datos), kpi_proyecto(todos))
    solara.Select(label="Estación", value=opcion, values=["Todas"] + sorted(todos[COLUMNA_FILTRO].unique()))
    with solara.Columns([1, 1]):
        Tarjeta("Minutos por viaje", f"{kpi_proyecto(datos):.1f} min")
        Tarjeta("Frente a todo el sistema", f"{dif:+.1f} %")
    solara.FigureMatplotlib(grafico_proyecto(datos, TOPE))
    solara.Markdown(f"**Lectura:** en {opcion.value} cada viaje dura {dif:+.1f} % frente al sistema.")
    r = evaluar_pronostico(datos, "fecha", "viajes", "2026-10-01")  # paso 5
    solara.Markdown(f"**Pronóstico de viajes por día:** error de {r['modelo_test']:.1f} en octubre; {veredicto(r)} ({r['base_test']:.1f}).")
