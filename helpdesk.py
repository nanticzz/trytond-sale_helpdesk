# This file is part of the sale_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Helpdesk', 'SaleHelpdesk']


class Helpdesk:
    __metaclass__ = PoolMeta
    __name__ = 'helpdesk'
    sales = fields.Many2Many('sale.sale.helpdesk', 'helpdesk', 'sale',
        'Sales', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['sale', 'generic']),
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('sale', 'Sale')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)


class SaleHelpdesk(ModelSQL):
    'Sale - Helpdesk'
    __name__ = 'sale.sale.helpdesk'
    _table = 'sale_sale_helpdesk_rel'
    sale = fields.Many2One('sale.sale', 'Sale', ondelete='CASCADE',
        select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
