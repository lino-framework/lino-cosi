# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# This file is part of Lino Cosi.
#
# Lino Cosi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Cosi is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Cosi.  If not, see
# <http://www.gnu.org/licenses/>.


"""
Sets `payment_term` of all partners.

"""


from lino.utils import Cycler
from lino.api import rt


def objects():

    PAYMENT_TERMS = Cycler(rt.models.ledger.PaymentTerm.objects.all())

    for obj in rt.models.contacts.Partner.objects.all():
        obj.payment_term = PAYMENT_TERMS.pop()
        yield obj
