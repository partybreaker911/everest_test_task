from flask_admin.contrib.sqla import ModelView


class CountryAdmin(ModelView):
    column_list = ["id", "name"]


class CityAdmin(ModelView):
    column_list = ["id", "name", "country"]


class StreetAdmin(ModelView):
    column_list = ["id", "name", "city"]
