from odoo import fields, models  # type:ignore


class GproyectosProyecto(models.fields):
    _name = "gproyectos.proyecto"
    _description = " aqui va la descripcion"

    name = fields.char(require=True, string="Nombre proyecto")
    description = fields.text(require=True, string="Descripcion")
    start_date = fields.date(require=True, string="Fecha de inicio")
    end_date = fields.date(require=True, string="Fecha de fin ")
    objectives = fields.text(require=True, string="Objetivos")

    employee_ids = fields.Many2one()
    task_ids = fields.One2many()
