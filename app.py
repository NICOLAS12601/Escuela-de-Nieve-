
import pyodbc as odbc
import dash
from dash import dcc, html, Dash, Input, Output, State, ALL
import pandas as pd
from database_connection import (
    agregar_instructor,
    agregar_turno,
    eliminar_instructor,
    eliminar_turno,
    obtener_instructores,
    obtener_turnos,
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
    html.Div(id="tabs-content")  # Contenedor para el contenido de las pestañas
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
            
            # Sección de reporte de ingresos
            html.H2("Actividades con Mayor Ingreso"),
            html.Button("Generar Reporte de Ingresos", id="generate-income-report", n_clicks=0),
            dcc.Loading(
                id="loading-income-report",
                type="default",
                children=html.Div(id="income-report-output")
            ),

            # Espaciado entre secciones
            html.Br(), html.Hr(), html.Br(),

            # Sección de reporte de alumnos
            html.H2("Actividades con Más Alumnos"),
            html.Button("Generar Reporte de Alumnos", id="generate-students-report", n_clicks=0),
            dcc.Loading(
                id="loading-students-report",
                type="default",
                children=html.Div(id="students-report-output")
            ),

            # Espaciado entre secciones
            html.Br(), html.Hr(), html.Br(),

            # Sección de reporte de turnos
            html.H2("Turnos con Más Clases Dictadas"),
            html.Button("Generar Reporte de Turnos", id="generate-turns-report", n_clicks=0),
            dcc.Loading(
                id="loading-turns-report",
                type="default",
                children=html.Div(id="turns-report-output")
            )
        ])

    elif tab == "abm_instructores":
        return html.Div([
            html.H1("ABM de Instructores"),
            html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '10px'}, children=[
                html.Label("CI:"),
                dcc.Input(id="input-ci", type="text", placeholder="Cédula de Identidad"),
                html.Label("Nombre:"),
                dcc.Input(id="input-nombre", type="text", placeholder="Nombre del Instructor"),
                html.Label("Apellido:"),
                dcc.Input(id="input-apellido", type="text", placeholder="Apellido del Instructor"),
                html.Button("Agregar Instructor", id="save-instructor-btn", n_clicks=0)
            ]),
            dcc.Loading(
                id="loading-instructors",
                type="default",
                children=[
                    html.Div(id="add-instructor-message"),
                    html.Div(id="instructors-table")
                ]
            )
        ])

    elif tab == "abm_turnos":
      return html.Div([
        html.H1("ABM de Turnos"),
        html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '10px'}, children=[
            html.Label("Horario inicio:"),
            dcc.Input(id="input-inicio", type="text"),
            html.Label("Horario final:"),
            dcc.Input(id="input-final", type="text"),
            html.Button("Agregar turno", id="save-turno-btn", n_clicks=0),
        ]),
        dcc.Loading(
            id="loading-turnos",
            type="default",
            children=[
                html.Div(id="turnos-table"),
                html.Div(id="add-turnos-message")  # Asegúrate de que este ID esté presente
            ]
        )
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

    # Si la pestaña no coincide, no actualizamos nada
    return dash.no_update

from dash import callback_context

# Callback unificado para los reportes
@app.callback(
    [Output("income-report-output", "children"),
     Output("students-report-output", "children"),
     Output("turns-report-output", "children")],
    [Input("generate-income-report", "n_clicks"),
     Input("generate-students-report", "n_clicks"),
     Input("generate-turns-report", "n_clicks")]
)
def update_reports(income_clicks, students_clicks, turns_clicks):
    ctx = callback_context

    # Identificar qué botón fue presionado
    if not ctx.triggered:
        return dash.no_update, dash.no_update, dash.no_update

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Generar reporte de ingresos
    if button_id == "generate-income-report":
        data = reporte_actividades_mayor_ingreso()
        data = [(actividad, float(ingreso) if isinstance(ingreso, Decimal) else ingreso) for actividad, ingreso in data]
        if data:
            df = pd.DataFrame(data, columns=["Actividad", "Ingresos Totales"])
            table = html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
                    for i in range(len(df))
                ])
            ])
            return table, dash.no_update, dash.no_update
        else:
            return "No se encontraron datos para el reporte de ingresos.", dash.no_update, dash.no_update

    # Generar reporte de alumnos
    elif button_id == "generate-students-report":
        data = reporte_actividades_mas_alumnos()
        if data:
            df = pd.DataFrame(data, columns=["Actividad", "Cantidad de Alumnos"])
            table = html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
                    for i in range(len(df))
                ])
            ])
            return dash.no_update, table, dash.no_update
        else:
            return dash.no_update, "No se encontraron datos para el reporte de alumnos.", dash.no_update

    # Generar reporte de turnos
    elif button_id == "generate-turns-report":
        data = reporte_turnos_mas_clases()
        if data:
            df = pd.DataFrame(data, columns=["Turno", "Clases Dictadas"])
            table = html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
                    for i in range(len(df))
                ])
            ])
            return dash.no_update, dash.no_update, table
        else:
            return dash.no_update, dash.no_update, "No se encontraron datos para el reporte de turnos."

    return dash.no_update, dash.no_update, dash.no_update


# Callback para cargar la lista de turnos al seleccionar la pestaña
@app.callback(
    Output("turnos-table", "children"),
    Input("tabs", "value")
)
def cargar_turnos(tab):
    if tab == "abm_turnos":
        turnos = obtener_turnos()

        # Convertimos la lista de tuplas en una lista de listas
        data = [list(turno) for turno in turnos] if turnos and all(len(t) == 3 for t in turnos) else []

        if data:
            # Crear un DataFrame con los datos obtenidos
            df = pd.DataFrame(data, columns=["ID", "Hora Inicio", "Hora Fin"])

            # Generar la tabla en HTML
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ] + [
                        # Asegurándonos de que el ID esté correctamente asignado al botón de eliminación
                        html.Td(html.Button("X", id={"type": "delete-btn", "index": str(df.iloc[i]["ID"])}))
                    ])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "No hay turnos disponibles."

    return dash.no_update

@app.callback(
    [Output("turnos-table", "children", allow_duplicate=True),
     Output("add-turnos-message", "children", allow_duplicate=True)],
    [Input("save-turno-btn", "n_clicks"),
     Input({"type": "delete-btn", "index": ALL}, "n_clicks")],
    [State("input-inicio", "value"),  # id correcto para la hora inicio
     State("input-final", "value"),   # id correcto para la hora final
     State("tabs", "value")],
    prevent_initial_call=True
)
def manejar_turnos(save_n_clicks, delete_n_clicks, hora_inicio, hora_fin, tab):
    ctx = dash.callback_context
    
    # Solo ejecutar si estamos en la pestaña correcta
    if tab != "abm_turnos":
        return dash.no_update, ""

    if ctx.triggered:
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # Si se activó el botón "Guardar Turno"
        if triggered_id == "save-turno-btn" and save_n_clicks > 0:
            if hora_inicio and hora_fin:
                resultado = agregar_turno(hora_inicio, hora_fin)
                if resultado == "agregado":
                    return cargar_turnos("abm_turnos"), "Turno agregado exitosamente"
                return dash.no_update, "Error al agregar el turno"
            return dash.no_update, "Error: Todos los campos son obligatorios"

        # Si se activó un botón "Eliminar Turno"
        elif "delete-btn" in triggered_id:
            index = eval(triggered_id)["index"]
            
            # Eliminar el turno sin verificar si existe en la base de datos (ya está en la tabla)
            resultado = eliminar_turno(index)
            if resultado == "eliminado":
                return cargar_turnos("abm_turnos"), "Turno eliminado exitosamente"
            return dash.no_update, "Error al eliminar el turno"
    
    return dash.no_update, ""

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