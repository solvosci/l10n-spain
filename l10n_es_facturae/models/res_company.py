# © 2015 Tecon
# © 2015 Omar Castiñeira (Comunitea)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    facturae_cert = fields.Binary(
        string='Certificado firma electrónica', filters='*.pfx')
    facturae_cert_password = fields.Char(string='Contraseña certificado')
