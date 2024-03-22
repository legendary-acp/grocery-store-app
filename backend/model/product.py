from backend import db


class Product(db.models):
    __tablename__="product"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    pricePerUnit=db.Column(db.Double)
    unit=db.Column(db.String)

    def __init__(self,name,price,unit):
        self.name=name
        self.pricePerUnit=price
        self.unit=unit



