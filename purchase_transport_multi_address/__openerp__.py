# -*- coding: utf-8 -*-
#
#
#    Author: Alexandre Fayolle
#    Copyright 2015 Camptocamp SA
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
#
#

{'name': 'Purchase - Transport Addresses',
 'summary': 'Manage origin / destination / consignee addresses on purchases',
 'version': '8.0.1.0.0',
 'author': "Camptocamp,Odoo Community Association (OCA)",
 'category': 'Warehouse',
 'license': 'AGPL-3',
 'complexity': 'expert',
 'images': [],
 'website': "http://www.camptocamp.com",
 'depends': ['purchase',
             'stock_transport_multi_address',
             'sale_transport_multi_address',
             ],
 'demo': [],
 'data': ['view/purchase.xml',
          ],
 'test': ['test/setup_user.yml',
          'test/setup_product.yml',
          'test/setup_dropshipping.xml',
          'test/test_propagate_address.yml',
          ],
 'auto_install': False,
 'installable': True,
 }
