#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    course_ids = fields.One2many(
        'edu.course',
        'product_template_id',
        string='Courses',
    )

    @api.constrains('type')
    def _check_for_product_type(self):
        """
        Check if the product type is consumable
        """
        for product_id in self:
            if product_id.type != 'consumable' and product_id.course_ids:
                raise UserError(_("In products associated with a course, the product type must be set to 'Consumable'."))
