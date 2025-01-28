from odoo import models, fields, api

class GestionEvaluaciones(models.Model):
    _name = "gestion.evaluaciones"
    _description = "Evaluación de empleado"
    _inherit = ['mail.thread']
    
    title = fields.Char(string="Título", required=True, tracking=True)
    evaluation_date = fields.Date(string="Fecha de evaluación", required=True, tracking=True)
    comments = fields.Text(string="Comentarios de evaluador", tracking=True)
    punctuation = fields.Integer(
        string="Puntuación",
        required=True,
        tracking=True,
        help="Puntuación del empleado (0-10)"
    )
    state = fields.Selection(
        [
            ("draft", "Pendiente"),
            ("in_progress", "En Progreso"),
            ("done", "Finalizado"),
        ],
        string="Estado",
        default="draft",
        tracking=True,
    )
    assigned_to = fields.Many2one(
        "hr.employee", 
        string="Empleado Asignado",
        required=True,
        tracking=True,
        ondelete='restrict'
    )
    
    @api.constrains('punctuation')
    def _check_punctuation(self):
        for record in self:
            if record.punctuation > 10 or record.punctuation < 0:
                raise ValidationError(_('La puntuación debe estar entre 0 y 10'))