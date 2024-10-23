#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EduSubject(models.Model):
    _name = 'edu.subject'
    _description = 'Subject Record'

    name = fields.Char(
        string='Subject Name',
        required=True,
        translate=True,
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
    course_ids = fields.Many2many(
        'edu.course',
        string='Courses',
    )
    credits = fields.Integer(
        string='Credits',
    )
