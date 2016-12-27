# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp
from openerp import SUPERUSER_ID

class WebsiteForm(openerp.addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        record_id = super(WebsiteForm, self).insert_record(
            request, model, values, custom, meta)
        if model.model == 'crm.lead':
            cr, context = request.cr, request.context
            local_context = context.copy()
            template_id = request.registry['ir.model.data'].\
                get_object_reference(cr, SUPERUSER_ID, 'website_crm_notify',
                                     'website_crm_notify_mail')[1]
            request.registry['mail.template'].send_mail(
                cr, SUPERUSER_ID, template_id, int(record_id),
                context=local_context, force_send=True)
        return record_id
