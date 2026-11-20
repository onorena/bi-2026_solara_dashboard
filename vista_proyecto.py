import solara
from matplotlib.figure import Figure

def diferencia_pct(valor, base):
    return (valor / base - 1) * 100  # cuánto se aleja la selección del total, en %

@solara.component
def Tarjeta(titulo, texto):
    with solara.Card(titulo):
        solara.Markdown(f"## {texto}")

def grafico_proyecto(datos, tope):
    # [Trabajo del estudiante] Paso 1: un gráfico honesto de sus datos con ylim=(0, tope).
    serie = datos.groupby("fecha").viajes.mean()  # promedio por estación
    ax = Figure(figsize=(7, 3)).subplots()
    ax.plot(serie.index, serie.values)
    ax.set(ylim=(0, tope), ylabel="Viajes por día", title="Viajes diarios por estación")
    return ax.figure
