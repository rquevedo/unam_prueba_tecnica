#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class EduEnrollment(models.Model):
    _name = 'edu.enrollment'
    _description = 'Student Enrollment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _sql_constraints = [("student_course_uniq", "unique (student_id, course_id)", "The student and course must be unique !")]

    name = fields.Char(
        string='Name',
        compute='_compute_name',
    )
    student_id = fields.Many2one(
        'edu.student',
        string='Student',
        required=True,
        readonly=True,
    )
    course_id = fields.Many2one(
        'edu.course',
        string='Course',
        required=True,
        readonly=True,
    )
    enrollment_date = fields.Date(
        string='Enrollment Date',
        default=fields.Date.today,
        required=True,
        readonly=True,
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')],
        string='State',
        default='draft',
        required=True,
        tracking=True,
    )

    @api.depends('student_id', 'course_id')
    def _compute_name(self):
        """
        Compute the name of the enrollment record based on
        the student and course names.
        """
        for record in self:
            record.name = f'{record.student_id.name} - {record.course_id.name}'

    def action_request(self):
        """
        Method to request enrollment.
        """
        for record in self:
            record.state = 'pending'

    def action_confirm(self):
        """
        Method to confirm enrollment.
        """
        for record in self:
            record.state = 'confirmed'

    def action_cancel(self):
        """
        Method to cancel enrollment.
        """
        for record in self:
            record.state = 'canceled'

    def action_draft(self):
        """
        Method to set enrollment to draft again.
        """
        for record in self:
            record.state = 'draft'

    def unlink(self):
        """
        Override the unlink method to prevent deletion of confirmed enrollments.
        """
        for record in self:
            if record.state == 'confirmed':
                raise Exception('You cannot delete a confirmed enrollment.')
        return super(EduEnrollment, self).unlink()

    @api.constrains('course_id', 'course_id.max_students', 'state')
    def _check_for_course_max_students(self):
        """
        Check if the course has reached the maximum number of students.
        """
        for record in self:
            if record.course_id.max_students <= len(
                record.course_id.enrollment_ids.filtered(lambda e: e.state == 'confirmed')
            ):
                raise UserError(_('The course has reached the maximum number of students.'))
