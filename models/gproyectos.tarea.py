#type:ignore
from odoo import models, fields

class GproyectosTarea(models.Model):
    _name = "gproyectos.tarea"
    _sql_constraints = [
        ('prioridad', 'CHECK(prioridad < 6 AND prioridad > 0)', "La prioridad debe estar entre 1 y 5")
    ]
    name = fields.Char(string="Nombre de tarea" required=True)
    description = fields.Text(string="Descripcion" required=True)
    prioridad = fields.Int(string="Prioridad" required=True)
    end_date = fields.Date(string="Fecha limite" required=True)

    proyect_ids = fields.Many2one("gproyectos.tarea", ondelete="cascade")

# cuando este la realacion, crear un decorador para que la fehca de la tarea no sea mas tarde que el fin del proyecto
