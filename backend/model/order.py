from backend import db


class Order(db.models):
    __tablename__="order"

    id=db.Column(db.Integer,primary_key=True)
    customerName=db.Column(db.String)
    total=db.Column(db.Double)

    def __init__(self,customerName,total):
        self.customerName=customerName
        self.total=total


