from odoo import models, fields

class Department(models.Model):
    _name = 'department.management'
    _description = 'Department Management'

    name = fields.Char(string='Department Name', required=True)  # Field 'name'
    manager_id = fields.Many2one('res.users', string='Manager')  # Field 'manager_id'
    description = fields.Text(string='Description')  # Thêm field mô tả (nếu cần)
