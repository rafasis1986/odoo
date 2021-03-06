# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from openerp import models, fields, api

class sale_order_line(models.Model):
    _inherit = "sale.order.line"
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False, fiscal_position=False,
            lang=False, date_order=False, packaging=False, update_tax=True, flag=False, context=None):
        res = super(sale_order_line,self).product_id_change(cr, uid, ids, pricelist, product, qty=qty,
            uom=False, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)
        #if product:
        #    p = self.pool.get('product.product').browse(cr, uid, product)
        #    res['value']['size_x'] = p.size_x
        #    res['value']['size_y'] = p.size_y
        #    res['value']['size_z'] = p.size_z
        return res
    def size_change(self, cr, uid, ids, size_x, size_y, product_id, qty, context={}):
        if (not product_id) or not (size_x and size_y ):
            return {}
        res= {}
        p = self.pool.get('product.product').browse(cr, uid, product_id)
        if size_x and size_y:
            res['product_uom_qty'] = size_x*size_y
        else:
            res['product_uom_qty'] = size_x*size_y
        return {'value': res}


    #prodlot_id = fields.Many2one('stock.production.lot', 'Production lot', help="Production lot is used to put a serial number on the production")
    #prodlot_ids = fields.One2many('stock.production.lot.all', 'lot_id', 'Lots Assignation', help="Production lot is used to put a serial number on the production")
    size_x = fields.Float(digits=(16,2), string='Width')
    size_y = fields.Float(digits=(16,2), string='Height')
    #size_z = fields.Float(digits=(16,2), string='Thickness')


class prod_lot_lines(models.Model):
    _name='stock.production.lot.all'
    name = fields.Float('Quantity')
    lot_id = fields.Many2one('stock.production.lot', 'Lot')


#class sale_order(models.Model):
#    _inherit = "sale.order"
#    def action_wait(self, cr, uid, ids, *args):
#        print 'Confirm'
#        res = super(sale_order,self).action_wait(cr, uid, ids, *args)
#        for sale in self.browse(cr, uid, ids):
#            for line in sale.order_line:
#                if line.prodlot_id.id:
#                    self.pool.get('stock.production.lot.reservation').create(cr, uid, {
#                        'name': sale.name,
#                        'size_x': line.size_x,
#                        'size_y': line.size_y,
#                        'size_z': line.size_z,
#                        'lot_id': line.prodlot_id.id
#                    })
#                for move in line.move_ids:
#                    self.pool.get('stock.move').write(cr, uid, {
#                        'prodlot_id': line.prodlot_id.id or False,
#                        'name': '%.2f x %.2f x %.2f' % (line.size_x or 1.0, line.size_y or 1.0, line.size_z or 1.0)
#                    })
#        return res
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

