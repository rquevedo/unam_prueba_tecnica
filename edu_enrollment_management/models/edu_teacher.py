#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Teacher Record'

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        required=True,
        ondelete='cascade',
    )
    subject_ids = fields.Many2many(
        'edu.subject',
        string='Subjects Taught',
    )
