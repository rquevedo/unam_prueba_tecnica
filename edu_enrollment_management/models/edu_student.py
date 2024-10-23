#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

from dateutil.relativedelta import relativedelta


class EduStudent(models.Model):
    _name = 'edu.student'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _inherits = {"res.partner": "partner_id"}
    _description = 'Student Record'

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        required=True,
        ondelete='cascade'
    )
    birthdate = fields.Date(
        string='Birthdate'
    )
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True
    )

    @api.depends('birthdate')
    def _compute_age(self):
        """
        Compute the age of the student based on the date of birth.
        The age is computed as the difference between the current date and the date of birth.
        """
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                age = relativedelta(today, record.birthdate).years
                record.age = age
            else:
                record.age = 0
