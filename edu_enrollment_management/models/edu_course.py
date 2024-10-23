#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class EduCourse(models.Model):
    _name = 'edu.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {"product.template": "product_template_id"}
    _description = 'Course Record'

    product_template_id = fields.Many2one(
        'product.template',
        string='Product Template',
        required=True,
        ondelete='cascade',
    )
    teacher_ids = fields.Many2many(
        'edu.teacher',
        string='Assigned Teachers',
    )
    subject_ids = fields.Many2many(
        'edu.subject',
        string='Subjects',
    )
    duration = fields.Integer(
        string='Duration (hours)',
        required=True,
        tracking=True,
    )
    start_date = fields.Date(
        string='Start Date',
        required=True,
        tracking=True,
    )
    max_students = fields.Integer(
        string='Max Students',
        required=True,
        tracking=True,
    )
    enrollment_ids = fields.One2many(
        'edu.enrollment',
        'course_id',
        string='Enrollments',
    )
