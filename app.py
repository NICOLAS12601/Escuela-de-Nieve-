import pyodbc as odbc
import dash
from dash import dcc, html, Dash, Input, Output, State, ALL
import pandas as pd
from database_connection import (
    agregar_instructor,
    eliminar_instructor,
    obtener_instructores,
    reporte_actividades_mas_alumnos,
    reporte_actividades_mayor_ingreso,
    reporte_turnos_mas_clases
)
from decimal import Decimal

# Inicializar la aplicación Dash con suppress_callback_exceptions=True
app = Dash(__name__, suppress_callback_exceptions=True)

# Layout de la aplicación con pestañas
app.layout = html.Div([
    dcc.Tabs(id="tabs", value="reportes", children=[
        dcc.Tab(label="Reportes", value="reportes"),
        dcc.Tab(label="ABM Instructores", value="abm_instructores"),
        dcc.Tab(label="ABM Turnos", value="abm_turnos"),
        dcc.Tab(label="Modificación de Actividades", value="mod_actividades"),
        dcc.Tab(label="ABM Alumnos", value="abm_alumnos")
    ]),
    html.Div(id="tabs-content")
])

# Callback para actualizar el contenido según la pestaña seleccionada
@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value")]
)
def render_content(tab):
    if tab == "reportes":
        return html.Div([
            html.H1("Escuela de Deportes de Nieve - Reportes"),
            html.H2("Actividades con Mayor Ingreso"),
            html.Button("Generar Reporte de Ingresos", id="generate-income-report", n_clicks=0),
            dcc.Loading(id="loading-income-report", type="default", children=html.Div(id="income-report-output")),

            html.H2("Actividades con Más Alumnos"),
            html.Button("Generar Reporte de Alumnos", id="generate-students-report", n_clicks=0),
            dcc.Loading(id="loading-students-report", type="default", children=html.Div(id="students-report-output")),

            html.H2("Turnos con Más Clases Dictadas"),
            html.Button("Generar Reporte de Turnos", id="generate-turns-report", n_clicks=0),
            dcc.Loading(id="loading-turns-report", type="default", children=html.Div(id="turns-report-output"))
    ])
    elif tab == "abm_instructores":
        return html.Div([
            html.H1("ABM de Instructores"),
            html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '10px'}, children=[
                html.Label("CI:"),
                dcc.Input(id="input-ci", type="text"),
                html.Label("Nombre:"),
                dcc.Input(id="input-nombre", type="text"),
                html.Label("Apellido:"),
                dcc.Input(id="input-apellido", type="text"),
                html.Button("Agregar Instructor", id="save-instructor-btn", n_clicks=0),
            ]),
            dcc.Loading(
                id="loading-instructors",
                type="default",
                children=[
                    html.Div(id="instructors-table"),
                    html.Div(id="add-instructor-message")
                ]
            )
        ])
    elif tab == "abm_turnos":
        return html.Div([
            html.H1("ABM de Turnos"),
            html.P("Aquí podrás realizar el alta, baja y modificación de turnos.")
        ])
    elif tab == "mod_actividades":
        return html.Div([
            html.H1("Modificación de Actividades"),
            html.P("Aquí podrás modificar las actividades existentes.")
        ])
    elif tab == "abm_alumnos":
        return html.Div([
            html.H1("ABM de Alumnos"),
            html.P("Aquí podrás realizar el alta, baja y modificación de alumnos.")
        ])



# Callbacks para los reportes
@app.callback(
    Output("income-report-output", "children"),
    [Input("generate-income-report", "n_clicks")]
)
def update_income_report(n_clicks):
    if n_clicks > 0:
        data = reporte_actividades_mayor_ingreso()
        data = [(actividad, float(ingreso) if isinstance(ingreso, Decimal) else ingreso) for actividad, ingreso in data]
        if data:
            df = pd.DataFrame(data, columns=["Actividad", "Ingresos Totales"])
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ]) for i in range(len(df))
                ])
            ])
        else:
            return "No se encontraron datos para el reporte de ingresos."
    return dash.no_update

@app.callback(
    Output("students-report-output", "children"),
    [Input("generate-students-report", "n_clicks")]
)
def update_students_report(n_clicks):
    if n_clicks > 0:
        data = reporte_actividades_mas_alumnos()
        data = [(actividad, int(cantidad)) for actividad, cantidad in data]
        if data:
            df = pd.DataFrame(data, columns=["Actividad", "Cantidad de Alumnos"])
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ]) for i in range(len(df))
                ])
            ])
        else:
            return "No se encontraron datos para el reporte de alumnos."
    return dash.no_update

@app.callback(
    Output("turns-report-output", "children"),
    [Input("generate-turns-report", "n_clicks")]
)
def update_turns_report(n_clicks):
    if n_clicks > 0:
        data = reporte_turnos_mas_clases()
        formatted_data = [
            (hora_inicio[:5] if hora_inicio else "N/A", 
             hora_fin[:5] if hora_fin else "N/A", 
             int(cantidad))
            for hora_inicio, hora_fin, cantidad in data
        ]
        if formatted_data:
            df = pd.DataFrame(formatted_data, columns=["Hora de Inicio", "Hora de Fin", "Cantidad de Clases"])
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ]) for i in range(len(df))
                ])
            ])
        else:
            return "No se encontraron datos para el reporte de turnos."
    return dash.no_update

# Callback para cargar la lista de instructores al entrar en la pestaña
@app.callback(
    Output("instructors-table", "children"),
    Input("tabs", "value")
)
def cargar_instructores(tab):
    if tab == "abm_instructores":
        instructores = obtener_instructores()
        data = [list(inst) for inst in instructores] if instructores and all(len(i) == 3 for i in instructores) else []
        
        if data:
            df = pd.DataFrame(data, columns=["CI", "Nombre", "Apellido"])
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ] + [html.Td(html.Button("X", id={"type": "delete-btn", "index": df.iloc[i]["CI"]}))])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "No hay instructores disponibles."
    return dash.no_update

# Callback para mostrar/ocultar el formulario de agregar instructor
@app.callback(
    Output("add-instructor-form", "style"),
    [Input("add-instructor-btn", "n_clicks")],
    prevent_initial_call=True
)
def mostrar_formulario_agregar(n_clicks):
    if n_clicks > 0:
        return {"display": "block", "textAlign": "center"}
    return {"display": "none"}

# Callback para manejar agregar y eliminar instructores
@app.callback(
    Output("instructors-table", "children", allow_duplicate=True),
    Output("add-instructor-message", "children", allow_duplicate=True),
    Input("save-instructor-btn", "n_clicks"),
    Input({"type": "delete-btn", "index": ALL}, "n_clicks"),
    State("input-ci", "value"),
    State("input-nombre", "value"),
    State("input-apellido", "value"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def manejar_instructores(save_n_clicks, delete_n_clicks, ci, nombre, apellido, tab):
    ctx = dash.callback_context

    if tab != "abm_instructores":
        return dash.no_update, ""

    if ctx.triggered:
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # Si se activó el botón de "Guardar Instructor"
        if triggered_id == "save-instructor-btn" and save_n_clicks > 0:
            if ci and nombre and apellido:
                resultado = agregar_instructor(ci, nombre, apellido)
                if resultado == "existe":
                    return dash.no_update, "Error: El CI ya existe"
                return cargar_instructores("abm_instructores"), "Instructor agregado exitosamente"
            return dash.no_update, "Error: Todos los campos son obligatorios"

        # Si se activó un botón de "Eliminar Instructor"
        elif "delete-btn" in triggered_id:
            index = eval(triggered_id)["index"]
            try:
                resultado = eliminar_instructor(index)
                return cargar_instructores("abm_instructores"), ""
            except odbc.IntegrityError:
                return dash.no_update, "Error: No se puede eliminar el instructor porque tiene clases asociadas."

    return dash.no_update, ""




# Correr la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)