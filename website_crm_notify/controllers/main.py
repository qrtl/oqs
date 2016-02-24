# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Rooms For (Hong Kong) Limited T/A OSCG
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import openerp
#from openerp import SUPERUSER_ID
#from openerp import http

#from openerp.addons.website_form.controllers.main import WebsiteForm

#class WebsiteForm(http.Controller):
class WebsiteForm(openerp.addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        record_id = super(WebsiteForm, self).insert_record(request, model, values, custom, meta)

#        context = {}
#        context.get('default_team_id', None)
#        team_obj = request.env['crm.team']
#        team_id = team_obj._get_default_team_id(SUPERUSER_ID, context=context, user_id=SUPERUSER_ID)

        follower_ids = [uid.id for uid in request.env['res.users'].browse() if uid.receive_contact ]
        vals = {
            'body': "Website Form Submitted",
            'model': model.model,
            'message_type': 'notification',
            'res_id': record_id,
            'partner_ids': follower_ids,
        }
        request.env['mail.message'].sudo().create(vals)

        return record_id
#        return super(WebsiteForm, self).insert_record(request, model, values, custom, meta)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
