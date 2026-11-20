from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def evaluar_pronostico(datos, col_fecha, col_valor, corte):
    diaria = datos.groupby(col_fecha)[col_valor].sum().reset_index()  # un valor por día
    diaria["fin_de_semana"] = (diaria[col_fecha].dt.dayofweek >= 5).astype(int)  # sábado o domingo
    train = diaria[diaria[col_fecha] < corte]  # el pasado: con esto aprende
    test = diaria[diaria[col_fecha] >= corte]  # el "futuro": el modelo no lo ve
    modelo = LinearRegression().fit(train[["fin_de_semana"]], train[col_valor])
    base = train[col_valor].mean()  # línea base: el promedio de siempre
    return {"base_test": mean_absolute_error(test[col_valor], [base] * len(test)),
            "modelo_test": mean_absolute_error(test[col_valor], modelo.predict(test[["fin_de_semana"]])),
            "modelo_train": mean_absolute_error(train[col_valor], modelo.predict(train[["fin_de_semana"]]))}

def veredicto(r):
    return "le gana a la línea base" if r["modelo_test"] < r["base_test"] else "NO le gana a la línea base"
