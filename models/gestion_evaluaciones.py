from odoo import models, fields, api


class GestionEvaluaciones(models.Model):
    _name = "gestion.evaluaciones"
    _description = "Evaluación de empleado"
    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Comentarios de evaluador")
    punctuation = fields.Float(string="Puntuación",required=True)
    assigned_to = fields.Many2one("hr.employee", string="Empleado Asignado")
    deadline = fields.Date(string="Fecha de evaluación", required=True)
    state = fields.Selection(
        [
            ("draft", "Pendiente"),
            ("in_progress", "En Progreso"),
            ("done", "Finalizado"),
        ],
        string="Estado",
        default="draft",
    )

    priority = fields.Selection(
        [
            ("0", "Baja"),
            ("1", "Media"),
            ("2", "Alta"),
        ],
        string="Prioridad",
        default="1",
    )
    @api.one
    @api.constrains('punctuation')
    def _check_value(self):
        if self.field_name > 10 or self.field_name < 0:
            raise ValidationError(_('Introduce un valor de 0 a 10'))
