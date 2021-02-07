#! /usr/bin/env python3
# coding: utf-8
""" """

from django.core.management.base import BaseCommand

from product.offapi.api_requests import ApiRequests
from product.offapi.insertdb import deletedata, insertdb
from product.offapi.charmax import Charmax


class Command(BaseCommand):
    def databasefill(self):
        """ """
        # Retrieves the maximum number of characters for the fields.
        Fields_charmax = Charmax.characters_max()
        # Retrives datas from Api and reject unsuitable datas.
        Api_data = ApiRequests().api_get_data(Fields_charmax)
        # Clear products data (not users and favorites)
        deletedata()
        # Insertion in database.
        Insert = insertdb(Api_data)
        print("Database installed.")

    def handle(self, *args, **options):
        self.databasefill()
