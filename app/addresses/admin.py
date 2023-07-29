from flask_admin.contrib.sqla import ModelView

from app import db, admin
from app.addresses.models import Country, City, Street


class CountryAdmin(ModelView):
    column_list = ["id", "name"]


admin.add_view(CountryAdmin(Country, db.session))


class CityAdmin(ModelView):
    column_list = ["id", "name", "country"]


admin.add_view(CityAdmin(City, db.session))


class StreetAdmin(ModelView):
    column_list = ["id", "name", "city"]


admin.add_view(StreetAdmin(Street, db.session))
