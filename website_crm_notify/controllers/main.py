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

class WebsiteForm(addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        res = super(WebsiteForm, self).insert_record(request, model, values, custom, meta)

        dest_model = request.env[model.model]
        message = "Contact Form Submitted"
        partner_ids = [fid.id for fid in dest_model.message_follower_ids]

        dest_model.message_post(body=message, partner_ids=partner_ids)

        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
