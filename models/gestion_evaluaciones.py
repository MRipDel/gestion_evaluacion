from odoo import models, fields, api

class GestionEvaluaciones(models.Model):
    _name = "gestion.evaluaciones"
    _description = "Evaluación de empleado"
    title = fields.Char(string="Título", required=True)
    evaluation_date = fields.Date(string="Fecha de evaluación", required=True)
    comments = fields.Text(string="Comentarios de evaluador")
    punctuation = fields.Float(string="Puntuación",required=True)
    state = fields.Selection(
        [
            ("draft", "Pendiente"),
            ("in_progress", "En Progreso"),
            ("done", "Finalizado"),
        ],
        string="Estado",
        default="draft",
    )
    assigned_to = fields.Many2one("hr.employee", string="Empleado Asignado")
    @api.one
    @api.constrains('punctuation')
    def _check_punctuation(self):
        if self.field_name > 10 or self.field_name < 0:
            raise ValidationError(_('Introduce un valor de 0 a 10'))
