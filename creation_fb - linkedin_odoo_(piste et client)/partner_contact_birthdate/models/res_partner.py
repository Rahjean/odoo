# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


########### client #############
class ResPart(models.Model):
    _inherit = "res.partner"

    facebook = fields.Char()
    linkedin = fields.Char()


###### pistes #############
class CrmLead(models.Model):
    _inherit = "crm.lead"

    facebook = fields.Char()
    linkedin = fields.Char()
 