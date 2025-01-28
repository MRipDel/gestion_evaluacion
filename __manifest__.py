{
    "name": "Gestión de Evaluaciones",
    "version": "1.0",
    "summary": "Módulo para gara gestionar las evaluaciones de desempeño de los empleados",
    "category": "Productivity",
    "author": "Manuel Ripalda",
    "website": "https://github.com/MRipDel",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "icon": "/gestion_tareas/static/description/icon52.png",
    "data": [
        "views/gestion_tarea_views.xml",
        "security/ir.model.access.csv"
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "description": """
    Módulo de Odoo para la las evaluaciones de desempeño de los empleados.
    """,
 'assets': {
        "web.assets_backend": [
            "/gestion_tareas/static/src/css/styles.css"
        ],
    },
}