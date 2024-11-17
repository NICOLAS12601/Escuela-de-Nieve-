import numpy as np
import pyodbc as odbc
import dash
from dash import dcc, html, Dash, Input, Output, State, ALL
from dash import callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import ast
from database_connection import (
    agregar_actividad,
    agregar_clase,
    agregar_inscripcion,
    agregar_instructor,
    agregar_turno,
    agregar_alumno,
    eliminar_actividad,
    eliminar_clase,
    eliminar_inscripcion,
    eliminar_instructor,
    eliminar_turno,
    eliminar_alumno,
    obtener_actividades,
    obtener_clases,
    obtener_inscripciones,
    obtener_instructores,
    obtener_turnos,
    obtener_alumnos,
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
        dcc.Tab(label="ABM Actividades", value="abm_actividades"),
        dcc.Tab(label="ABM Alumnos", value="abm_alumnos"),
        dcc.Tab(label="ABM Clases", value="abm_clases"),
        dcc.Tab(label="ABM Inscripciones", value="abm_inscripciones")
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

    elif tab == "abm_actividades":
        return html.Div([
            html.H1("ABM Actividades"),
            dcc.Loading(
                id="loading-activities",
                type="default",
                children=[
                    html.Table(id="activities-table", style={"width": "100%", "margin": "0 auto", "textAlign": "center"}),
                    html.Div(id="activity-message", style={"textAlign": "center", "marginTop": "10px"}),
                ]
            ),
            html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '10px'}, children=[
                dcc.Input(id="input-id", type="hidden"),  # Para almacenar el ID si es una edición
                html.Label("Descripción:"),
                dcc.Input(id="input-descripcion", type="text"),
                html.Label("Costo:"),
                dcc.Input(id="input-costo", type="number"),
                html.Button("Guardar", id="save-activity-btn", n_clicks=0),
            ])
        ])

    elif tab == "abm_alumnos":
        return html.Div([
            html.H1("ABM de Alumnos"),
            html.Div(
                style={
                    'display': 'flex',
                    'flexDirection': 'row',
                    'flexWrap': 'wrap',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'gap': '20px',
                    'maxWidth': '1200px',
                    'margin': '0 auto'
                },
                children=[
                    html.Div([
                        html.Label("CI:"),
                        dcc.Input(id="input-alumno-ci", type="text", placeholder="Cédula de Identidad"),
                    ], style={'flex': '1', 'minWidth': '200px'}),

                    html.Div([
                        html.Label("Nombre:"),
                        dcc.Input(id="input-alumno-nombre", type="text", placeholder="Nombre del Alumno"),
                    ], style={'flex': '1', 'minWidth': '200px'}),

                    html.Div([
                        html.Label("Apellido:"),
                        dcc.Input(id="input-alumno-apellido", type="text", placeholder="Apellido del Alumno"),
                    ], style={'flex': '1', 'minWidth': '200px'}),

                    html.Div([
                        html.Label("Teléfono:"),
                        dcc.Input(id="input-alumno-telefono", type="text", placeholder="Teléfono de contacto"),
                    ], style={'flex': '1', 'minWidth': '200px'}),

                    html.Div([
                        html.Label("Correo Electrónico:"),
                        dcc.Input(id="input-alumno-correo", type="email", placeholder="Correo electrónico"),
                    ], style={'flex': '1', 'minWidth': '200px'}),

                    html.Div([
                        html.Button("Agregar Alumno", id="save-alumno-btn", n_clicks=0)
                    ], style={'flex': '1', 'minWidth': '200px', 'textAlign': 'center'}),
                ]
            ),
            dcc.Loading(
                id="loading-alumnos",
                type="default",
                children=[
                    html.Div(id="add-alumno-message"),
                    html.Div(id="alumnos-table")
                ]
            )
        ]),

    elif tab == "abm_clases":
        # Obtener los datos para los menús desplegables
        instructores = obtener_instructores()
        actividades = obtener_actividades()
        turnos = obtener_turnos()

        # Formatear los turnos
        turnos_formateados = [
            (turno[0], pd.to_datetime(turno[1]).strftime("%H:%M"), pd.to_datetime(turno[2]).strftime("%H:%M"))
            for turno in turnos
]
        
        # Crear opciones para los menús desplegables
        opciones_instructores = [
            {'label': f"{inst[1]} {inst[2]} (CI: {inst[0]})", 'value': inst[0]}
            for inst in instructores
        ]

        opciones_actividades = [
            {'label': f"{act[1]} (ID: {act[0]})", 'value': act[0]}
            for act in actividades
        ]

        opciones_turnos = [
            {'label': f"{turno[1]} - {turno[2]} (ID: {turno[0]})", 'value': turno[0]}
            for turno in turnos_formateados
        ]

        return html.Div([
            html.H1("ABM Clases"),
            html.Div([
                html.Label("Instructor:"),
                dcc.Dropdown(
                    id="dropdown-instructor",
                    options=opciones_instructores,
                    placeholder="Seleccione un instructor"
                ),
                html.Br(),
                html.Label("Actividad:"),
                dcc.Dropdown(
                    id="dropdown-actividad",
                    options=opciones_actividades,
                    placeholder="Seleccione una actividad"
                ),
                html.Br(),
                html.Label("Turno:"),
                dcc.Dropdown(
                    id="dropdown-turno",
                    options=opciones_turnos,
                    placeholder="Seleccione un turno"
                ),
                html.Br(),
                html.Button("Agregar Clase", id="btn-agregar-clase", n_clicks=0),
                html.Div(id="mensaje-clase", style={"marginTop": "20px"}),
                html.Br(),
            ], style={'width': '50%', 'margin': '0 auto'}),
            html.H2("Listado de Clases"),
            dcc.Loading(
                id="loading-clases",
                type="default",
                children=[
                    html.Div(id="clases-table"),
                    html.Div(id="mensaje-eliminar-clase", style={"marginTop": "20px"})
                ]
            )
        ])

    elif tab == "abm_inscripciones":
        # Obtener datos para los menús desplegables
        clases = obtener_clases()
        alumnos = obtener_alumnos()
        # Convertir clases y alumnos en opciones para los dropdowns
        # Opciones para clases
        clases_options = []
        for clase in clases:
            clase_id = clase['id']
            actividad = clase['actividad_descripcion']
            instructor = f"{clase['instructor_nombre']} {clase['instructor_apellido']}"
            hora_inicio = pd.to_datetime(clase['hora_inicio']).strftime("%H:%M")
            hora_fin = pd.to_datetime(clase['hora_fin']).strftime("%H:%M")
            label = f"ID: {clase_id} - {actividad} con {instructor} de {hora_inicio} a {hora_fin}"
            clases_options.append({'label': label, 'value': clase_id})
        
        # Opciones para alumnos
        alumnos_options = [{'label': f"{alumno[1]} {alumno[2]} (CI: {alumno[0]})", 'value': alumno[0]} for alumno in alumnos]
        
        # Opciones para equipamiento
        equipamiento_options = [
            {'label': 'Sí', 'value': 1},
            {'label': 'No', 'value': 0}
        ]
        
        return html.Div([
            html.H1("ABM Inscripciones"),
            html.Div([
                html.Label("Clase:"),
                dcc.Dropdown(
                    id="dropdown-clase",
                    options=clases_options,
                    placeholder="Seleccione una clase"
                ),
                html.Br(),
                html.Label("Alumno:"),
                dcc.Dropdown(
                    id="dropdown-alumno",
                    options=alumnos_options,
                    placeholder="Seleccione un alumno"
                ),
                html.Br(),
                html.Label("¿Alquila equipamiento?"),
                dcc.Dropdown(
                    id="dropdown-equipamiento",
                    options=equipamiento_options,
                    placeholder="Seleccione una opción"
                ),
                html.Br(),
                html.Button("Agregar Inscripción", id="btn-agregar-inscripcion", n_clicks=0),
                html.Div(id="mensaje-inscripcion", style={"marginTop": "20px"}),
                html.Br(),
            ], style={'width': '50%', 'margin': '0 auto'}),
            html.H2("Listado de Inscripciones"),
            dcc.Loading(
                id="loading-inscripciones",
                type="default",
                children=[
                    html.Div(id="inscripciones-table"),
                    html.Div(id="mensaje-eliminar-inscripcion", style={"marginTop": "20px"})
                ]
            )
        ])
                
        # Si la pestaña no coincide, no actualizamos nada
        return dash.no_update

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
    ctx = dash.callback_context

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
        print("Data returned from reporte_actividades_mas_alumnos:", data)
        if data:
            # Convertir cada fila en una tupla
            data_list = [tuple(row) for row in data]
            print("Data list:", data_list)
            df = pd.DataFrame(data_list, columns=["Actividad", "Cantidad de Alumnos"])
            print("DataFrame df:", df)
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
        print("Data returned from reporte_turnos_mas_clases:", data)
        if data:
            data_list = [tuple(row) for row in data]
            print("Data list:", data_list)
            df = pd.DataFrame(data_list, columns=["Turno", "Clases Dictadas"])
            print("DataFrame df:", df)
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
        
# Función para cargar la lista de instructores
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
                    ] + [html.Td(html.Button("X", id={"type": "delete-instructor-btn", "index": df.iloc[i]["CI"]}))])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "No hay instructores disponibles."
    return dash.no_update

# Callback para manejar agregar y eliminar instructores
@app.callback(
    [Output("instructors-table", "children"),
     Output("add-instructor-message", "children")],
    [Input("tabs", "value"),
     Input("save-instructor-btn", "n_clicks"),
     Input({"type": "delete-instructor-btn", "index": ALL}, "n_clicks")],
    [State("input-ci", "value"),
     State("input-nombre", "value"),
     State("input-apellido", "value")],
)
def manejar_instructores(tab, save_n_clicks, delete_n_clicks, ci, nombre, apellido):
    ctx = dash.callback_context

    if tab != "abm_instructores":
        return dash.no_update, ""

    # Si no hay interacción (al cargar la pestaña), cargamos la tabla
    if not ctx.triggered or ctx.triggered[0]['prop_id'] == 'tabs.value':
        return cargar_instructores(tab), ""

    triggered_prop_id = ctx.triggered[0]["prop_id"]
    triggered_id = triggered_prop_id.split(".")[0]

    # Si se presionó el botón de guardar instructor
    if triggered_id == "save-instructor-btn":
        if ci and nombre and apellido:
            resultado = agregar_instructor(ci, nombre, apellido)
            if resultado == "existe":
                return dash.no_update, "Error: El CI ya existe"
            return cargar_instructores("abm_instructores"), "Instructor agregado exitosamente"
        return dash.no_update, "Error: Todos los campos son obligatorios"

    # Si se presionó un botón de eliminar instructor
    elif 'delete-instructor-btn' in triggered_id:
        dict_id = ast.literal_eval(triggered_id)
        ci_to_delete = dict_id['index']
        resultado = eliminar_instructor(ci_to_delete)
        if resultado == "eliminado":
            return cargar_instructores("abm_instructores"), "Instructor eliminado exitosamente"
        else:
            return dash.no_update, "Error al eliminar el instructor."

    return dash.no_update, ""

# Función para cargar la lista de turnos al seleccionar la pestaña
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
            df["Hora Inicio"] = pd.to_datetime(df["Hora Inicio"]).dt.strftime("%H:%M")
            df["Hora Fin"] = pd.to_datetime(df["Hora Fin"]).dt.strftime("%H:%M")

            # Generar la tabla en HTML
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ] + [
                        html.Td(html.Button("X", id={"type": "delete-turno-btn", "index": str(df.iloc[i]["ID"])}))
                    ])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "No hay turnos disponibles."
    return dash.no_update

# Callback para agregar turnos
@app.callback(
    [Output("turnos-table", "children", allow_duplicate=True),
     Output("add-turnos-message", "children", allow_duplicate=True)],
    Input("save-turno-btn", "n_clicks"),
    State("input-inicio", "value"),
    State("input-final", "value"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def agregar_turno_callback(save_n_clicks, hora_inicio, hora_fin, tab):
    if tab != "abm_turnos":
        return dash.no_update, ""
    
    if save_n_clicks and save_n_clicks > 0:
        if hora_inicio and hora_fin:
            resultado = agregar_turno(hora_inicio, hora_fin)
            if resultado == "agregado":
                return cargar_turnos("abm_turnos"), "Turno agregado exitosamente"
            return dash.no_update, "Error al agregar el turno"
        return dash.no_update, "Error: Todos los campos son obligatorios"
    return dash.no_update, ""

# Callback para eliminar turnos
@app.callback(
    [Output("turnos-table", "children", allow_duplicate=True),
     Output("add-turnos-message", "children", allow_duplicate=True)],
    Input({"type": "delete-turno-btn", "index": ALL}, "n_clicks_timestamp"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def eliminar_turno_callback(n_clicks_timestamps, tab):
    if tab != "abm_turnos":
        return dash.no_update, ""
    
    if not n_clicks_timestamps or all(ts is None or ts == 0 for ts in n_clicks_timestamps):
        return dash.no_update, ""
    
    ctx = dash.callback_context
    max_ts = max([ts if ts is not None else 0 for ts in n_clicks_timestamps])
    if max_ts > 0:
        idx = n_clicks_timestamps.index(max_ts)
        delete_ids = [input['id'] for input in ctx.inputs_list[0]]
        turno_id_to_delete = delete_ids[idx]['index']
        resultado = eliminar_turno(turno_id_to_delete)
        if resultado == "eliminado":
            return cargar_turnos("abm_turnos"), "Turno eliminado exitosamente"
        else:
            return dash.no_update, "Error al eliminar el turno."
    return dash.no_update, ""

# Función para cargar la lista de actividades
@app.callback(
    Output("activities-table", "children"),
    Input("tabs", "value")
)
def cargar_actividades(tab):
    if tab == "abm_actividades":
        actividades = obtener_actividades()
        print("Datos de actividades:", actividades)  # Depuración

        # Asegúrate de que los datos tengan la estructura correcta
        if actividades and all(len(act) == 3 for act in actividades):
            # Convierte los datos en una lista procesada (con Decimal convertido a float)
            actividades_procesadas = [
                (int(id), descripcion, float(costo)) for id, descripcion, costo in actividades
            ]

            # Crea el DataFrame con las columnas esperadas
            df = pd.DataFrame(actividades_procesadas, columns=["ID", "Descripción", "Costo"])

            # Renderiza la tabla en HTML con botones de eliminar
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
                html.Tbody([
                    html.Tr([html.Td(df.iloc[i][col]) for col in df.columns] +
                            [html.Td(html.Button("X", id={"type": "delete-activity-btn", "index": int(df.iloc[i]["ID"])}))])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "Error: Datos de actividades en formato inesperado."
    return dash.no_update

# Callback para agregar actividades
@app.callback(
    [Output("activities-table", "children", allow_duplicate=True),
     Output("activity-message", "children", allow_duplicate=True)],
    Input("save-activity-btn", "n_clicks"),
    State("input-descripcion", "value"),
    State("input-costo", "value"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def agregar_actividad_callback(save_n_clicks, descripcion, costo, tab):
    if tab != "abm_actividades":
        return dash.no_update, ""
    
    if save_n_clicks and save_n_clicks > 0:
        if descripcion and costo:
            resultado = agregar_actividad(descripcion, costo)
            return cargar_actividades("abm_actividades"), "Actividad agregada exitosamente." if resultado == "ok" else "Error al agregar actividad."
        return dash.no_update, "Error: Todos los campos son obligatorios"
    return dash.no_update, ""

# Callback para eliminar actividades
@app.callback(
    [Output("activities-table", "children", allow_duplicate=True),
     Output("activity-message", "children", allow_duplicate=True)],
    Input({"type": "delete-activity-btn", "index": ALL}, "n_clicks_timestamp"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def eliminar_actividad_callback(n_clicks_timestamps, tab):
    if tab != "abm_actividades":
        return dash.no_update, ""
    
    if not n_clicks_timestamps or all(ts is None or ts == 0 for ts in n_clicks_timestamps):
        return dash.no_update, ""
    
    ctx = dash.callback_context
    max_ts = max([ts if ts is not None else 0 for ts in n_clicks_timestamps])
    if max_ts > 0:
        idx = n_clicks_timestamps.index(max_ts)
        delete_ids = [input['id'] for input in ctx.inputs_list[0]]
        activity_id = delete_ids[idx]['index']
        resultado = eliminar_actividad(activity_id)
        if resultado == "ok":
            return cargar_actividades("abm_actividades"), "Actividad eliminada exitosamente."
        elif resultado == "referenciado":
            return dash.no_update, "Error: La actividad está referenciada en otras tablas."
        return dash.no_update, "Error al eliminar la actividad."
    return dash.no_update, ""

# Función para cargar la lista de alumnos
@app.callback(
    Output("alumnos-table", "children"),
    Input("tabs", "value")
)
def cargar_alumnos(tab):
    if tab == "abm_alumnos":
        alumnos = obtener_alumnos()
        data = [list(alumno) for alumno in alumnos] if alumnos and all(len(a) == 5 for a in alumnos) else []
        
        if data:
            df = pd.DataFrame(data, columns=["CI", "Nombre", "Apellido", "Teléfono", "Correo Electrónico"])
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ] + [html.Td(html.Button("X", id={"type": "delete-alumno-btn", "index": df.iloc[i]["CI"]}))])
                    for i in range(len(df))
                ])
            ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
        else:
            return "No hay alumnos disponibles."
    return dash.no_update

# Callback para agregar alumnos
@app.callback(
    [Output("alumnos-table", "children", allow_duplicate=True),
     Output("add-alumno-message", "children", allow_duplicate=True)],
    Input("save-alumno-btn", "n_clicks"),
    State("input-alumno-ci", "value"),
    State("input-alumno-nombre", "value"),
    State("input-alumno-apellido", "value"),
    State("input-alumno-telefono", "value"),
    State("input-alumno-correo", "value"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def agregar_alumno_callback(save_n_clicks, ci, nombre, apellido, telefono, correo, tab):
    if tab != "abm_alumnos":
        return dash.no_update, ""
    
    if save_n_clicks and save_n_clicks > 0:
        if ci and nombre and apellido and correo:
            resultado = agregar_alumno(ci, nombre, apellido, telefono, correo)
            if resultado == "existe":
                return dash.no_update, "Error: El CI ya existe"
            elif resultado == "ok":
                # Opcionalmente, limpiar los campos de entrada después de agregar
                return cargar_alumnos("abm_alumnos"), "Alumno agregado exitosamente"
            else:
                return dash.no_update, "Error al agregar el alumno"
        else:
            return dash.no_update, "Error: Los campos CI, Nombre, Apellido y Correo son obligatorios"
    return dash.no_update, ""

# Callback para eliminar alumnos
@app.callback(
    [Output("alumnos-table", "children", allow_duplicate=True),
     Output("add-alumno-message", "children", allow_duplicate=True)],
    Input({"type": "delete-alumno-btn", "index": ALL}, "n_clicks_timestamp"),
    State("tabs", "value"),
    prevent_initial_call=True
)
def eliminar_alumno_callback(n_clicks_timestamps, tab):
    if tab != "abm_alumnos":
        return dash.no_update, ""
    
    if not n_clicks_timestamps or all(ts is None or ts == 0 for ts in n_clicks_timestamps):
        return dash.no_update, ""
    
    ctx = dash.callback_context
    max_ts = max([ts if ts is not None else 0 for ts in n_clicks_timestamps])
    if max_ts > 0:
        idx = n_clicks_timestamps.index(max_ts)
        delete_ids = [input['id'] for input in ctx.inputs_list[0]]
        ci_to_delete = delete_ids[idx]['index']
        resultado = eliminar_alumno(ci_to_delete)
        if resultado == "ok":
            return cargar_alumnos("abm_alumnos"), "Alumno eliminado exitosamente"
        elif resultado == "referenciado":
            return dash.no_update, "Error: No se puede eliminar el alumno porque tiene clases asociadas."
        else:
            return dash.no_update, "Error al eliminar el alumno"
    return dash.no_update, ""

def cargar_clases():
    clases = obtener_clases()
    if clases:
        df = pd.DataFrame(clases)
        # Reorganizar las columnas
        df = df[["id", "instructor_nombre", "instructor_apellido", "actividad_descripcion", "hora_inicio", "hora_fin"]]
        df["hora_inicio"] = pd.to_datetime(df["hora_inicio"]).dt.strftime("%H:%M")
        df["hora_fin"] = pd.to_datetime(df["hora_fin"]).dt.strftime("%H:%M")
        df.columns = ["ID", "Nombre", "Apellido", "Actividad", "Hora Inicio", "Hora Fin"]
        
        return html.Table([
            html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ] + [
                    html.Td(
                        html.Button(
                            "X",
                            id={
                                "type": "delete-clase-btn",
                                "index": int(df.iloc[i]["ID"])
                            }
                        )
                    )
                ])
                for i in range(len(df))
            ])
        ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
    else:
        return "No hay clases disponibles."

# Callback para manejar agregar y eliminar clases
@app.callback(
    [Output("clases-table", "children"),
     Output("mensaje-clase", "children")],
    [Input("tabs", "value"),
     Input("btn-agregar-clase", "n_clicks"),
     Input({"type": "delete-clase-btn", "index": ALL}, "n_clicks")],
    [State("dropdown-instructor", "value"),
     State("dropdown-actividad", "value"),
     State("dropdown-turno", "value")],
)
def manejar_clases(tab, n_clicks_agregar, delete_n_clicks, ci_instructor, id_actividad, id_turno):
    ctx = dash.callback_context

    if tab != "abm_clases":
        return dash.no_update, ""

    # Si no hay interacción (al cargar la pestaña), cargamos la tabla
    if not ctx.triggered or ctx.triggered[0]['prop_id'] == 'tabs.value':
        return cargar_clases(), ""

    triggered_prop_id = ctx.triggered[0]["prop_id"]
    triggered_id = triggered_prop_id.split(".")[0]

    # Si se presionó el botón de agregar clase
    if triggered_id == "btn-agregar-clase":
        if ci_instructor and id_actividad and id_turno:
            resultado = agregar_clase(ci_instructor, id_actividad, id_turno)
            if resultado == "ok":
                return cargar_clases(), dbc.Alert("Clase agregada exitosamente.", color="success")
            else:
                return dash.no_update, dbc.Alert("Error al agregar la clase.", color="danger")
        else:
            return dash.no_update, dbc.Alert("Por favor, complete todos los campos.", color="warning")

    # Si se presionó un botón de eliminar clase
    elif 'delete-clase-btn' in triggered_id:
        dict_id = ast.literal_eval(triggered_id)
        clase_id = int(dict_id['index'])
        resultado = eliminar_clase(clase_id)
        if resultado == "ok":
            return cargar_clases(), dbc.Alert("Clase eliminada exitosamente.", color="success")
        else:
            return dash.no_update, dbc.Alert("Error al eliminar la clase.", color="danger")

    return dash.no_update, ""

def cargar_inscripciones():
    inscripciones = obtener_inscripciones()
    if inscripciones:
        df = pd.DataFrame(inscripciones)
        # Reorganizar las columnas
        df = df[["id_clase", "ci_alumno", "alumno_nombre", "alumno_apellido", "actividad_descripcion", "instructor_nombre", "instructor_apellido", "hora_inicio", "hora_fin", "alquiler"]]
        df["hora_inicio"] = pd.to_datetime(df["hora_inicio"]).dt.strftime("%H:%M")
        df["hora_fin"] = pd.to_datetime(df["hora_fin"]).dt.strftime("%H:%M")
        df.columns = ["ID Clase", "CI Alumno", "Nombre Alumno", "Apellido Alumno", "Actividad", "Nombre Instructor", "Apellido Instructor", "Hora Inicio", "Hora Fin", "Alquiler"]

        # Mapear alquiler a Sí/No
        df["Alquiler"] = df["Alquiler"].apply(lambda x: "Sí" if x else "No")
        
        return html.Table([
            html.Thead(html.Tr([html.Th(col) for col in df.columns] + [html.Th("Eliminar")])),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ] + [
                    html.Td(
                        html.Button(
                            "X",
                            id={
                                "type": "delete-inscripcion-btn",
                                "index": f"{int(df.iloc[i]['ID Clase'])}_{df.iloc[i]['CI Alumno']}"
                            }
                        )
                    )
                ])
                for i in range(len(df))
            ])
        ], style={"width": "100%", "margin": "0 auto", "textAlign": "center"})
    else:
        return "No hay inscripciones disponibles."

@app.callback(
    [Output("inscripciones-table", "children"),
     Output("mensaje-inscripcion", "children")],
    [Input("tabs", "value"),
     Input("btn-agregar-inscripcion", "n_clicks"),
     Input({"type": "delete-inscripcion-btn", "index": ALL}, "n_clicks")],
    [State("dropdown-clase", "value"),
     State("dropdown-alumno", "value"),
     State("dropdown-equipamiento", "value")],
)
def manejar_inscripciones(tab, n_clicks_agregar, delete_n_clicks, clase_id, ci_alumno, alquiler):
    ctx = dash.callback_context

    if tab != "abm_inscripciones":
        return dash.no_update, ""

    # Si no hay interacción (al cargar la pestaña), cargamos la tabla
    if not ctx.triggered or ctx.triggered[0]['prop_id'] == 'tabs.value':
        return cargar_inscripciones(), ""

    triggered_prop_id = ctx.triggered[0]["prop_id"]
    triggered_id = triggered_prop_id.split(".")[0]

    # Si se presionó el botón de agregar inscripción
    if triggered_id == "btn-agregar-inscripcion":
        if clase_id and ci_alumno and alquiler is not None:
            resultado = agregar_inscripcion(clase_id, ci_alumno, alquiler)
            if resultado == "ok":
                return cargar_inscripciones(), dbc.Alert("Inscripción agregada exitosamente.", color="success")
            else:
                return dash.no_update, dbc.Alert("Error al agregar la inscripción.", color="danger")
        else:
            return dash.no_update, dbc.Alert("Por favor, complete todos los campos.", color="warning")

    # Si se presionó un botón de eliminar inscripción
    elif 'delete-inscripcion-btn' in triggered_id:
        dict_id = ast.literal_eval(triggered_id)
        index_str = dict_id['index']
        clase_id_str, ci_alumno = index_str.split('_')
        clase_id = int(clase_id_str)
        resultado = eliminar_inscripcion(clase_id, ci_alumno)
        if resultado == "ok":
            return cargar_inscripciones(), dbc.Alert("Inscripción eliminada exitosamente.", color="success")
        else:
            return dash.no_update, dbc.Alert("Error al eliminar la inscripción.", color="danger")

    return dash.no_update, ""

# Correr la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)