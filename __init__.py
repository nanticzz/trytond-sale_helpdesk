# This file is part of the sale_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .helpdesk import *


def register():
    Pool.register(
        HelpdeskConfiguration,
        Helpdesk,
        SaleHelpdesk,
        module='sale_helpdesk', type_='model')
