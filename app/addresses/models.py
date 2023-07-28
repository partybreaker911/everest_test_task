from app import db


class Country(db.Model):
    """Model that stores country information."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class City(db.Model):
    """Model that stores city information."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), nullable=False)
    country = db.relationship("Country", backref=db.backref("cities", lazy=True))

    def __init__(self, name, country):
        self.name = name
        self.country = country


class Street(db.Model):
    """Model that stores street information."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)
    city = db.relationship("City", backref=db.backref("streets", lazy=True))

    def __init__(self, name, city):
        self.name = name
        self.city = city
