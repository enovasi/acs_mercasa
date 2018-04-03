# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Invoice(models.Model):
    _inherit = 'account.invoice'

    def _compute_report_url(self):
        for record in self:
            uri = 'http://vps.enovasi.com/detalle.php?idFac=%s' % record.number
            record.custom_url = uri

    custom_url = fields.Char(compute='_compute_report_url', string='Report URL', readonly=True)