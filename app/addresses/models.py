from app import db, admin
from app.addresses.admin import (
    CountryAdmin,
    CityAdmin,
    StreetAdmin,
)


class Country(db.Model):
    """Country model"""

    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    city = db.relationship("City", back_populates="country")

    def __repr__(self):
        return self.name


class City(db.Model):
    """City model"""

    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    country_id = db.Column(db.Integer(), db.ForeignKey("countries.id"))

    country = db.relationship("Country", back_populates="city")
    streets = db.relationship("Street", back_populates="city")

    def __repr__(self):
        return self.name


class Street(db.Model):
    """Street model"""

    __tablename__ = "streets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    city_id = db.Column(db.Integer(), db.ForeignKey("cities.id"))

    city = db.relationship("City", back_populates="streets")

    def __repr__(self):
        return self.name


admin.add_view(CountryAdmin(Country, db.session))
admin.add_view(CityAdmin(City, db.session))
admin.add_view(StreetAdmin(Street, db.session))
