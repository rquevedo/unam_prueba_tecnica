# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Educational enrollment management',
    'version': '17.0.1.0.0',
    'category': 'School Management',
    'description': """
Manage student enrollments within an educational system using this module.
It provides comprehensive tools for managing students, subjects, courses, and teachers,
enabling educational institutions to efficiently organize and oversee these key resources.
    """,
    'author': 'Reinier Quevedo Batista',
    'license': 'OPL-1',
    'maintainer': 'Reinier Quevedo Batista',
    'website': 'https://github.com/rquevedo/unam_prueba_tecnica',
    'depends': [
        'base',
        'contacts',
        'product',
    ],
    "data": [
        # Security
        "security/edu_security.xml",
        "security/ir.model.access.csv",
        # Views
        "views/menus.xml",
        "views/edu_course_views.xml",
        "views/edu_enrollment_views.xml",
        "views/edu_student_views.xml",
        "views/edu_subject_views.xml",
        "views/edu_teacher_views.xml",
        # Reports
        "report/edu_enrollment_report.xml"
    ],
    'installable': True,
    'application': False,
}
