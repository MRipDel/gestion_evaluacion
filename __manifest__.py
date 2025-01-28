{
    "name": "Gestión de Evaluaciones",
    "version": "1.0",
    "summary": "Módulo para gara gestionar las evaluaciones de desempeño de los empleados",
    "category": "Human Resources",
    "author": "Manuel Ripalda",
    "website": "https://github.com/MRipDel",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "icon": "/evaluacion_desempeno/static/description/icon52.png",
    "data": [
        "views/gestion_tarea_views.xml",
        "security/ir.model.access.csv"
    ],
    "application": True,
    "depends":["base", "mail", "hr"],
    "installable": True,
    "auto_install": False,
    "description": """
    Módulo de Odoo para la las evaluaciones de desempeño de los empleados.
    """,
 'assets': {
        "web.assets_backend": [
            "/evaluacion_desempeno/static/src/css/styles.css"
        ],
    },
}