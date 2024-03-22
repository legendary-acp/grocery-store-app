from backend import db
from backend.model.product import Product


class OrderItem(db.models):
    __tablename__="order-item"
    id=db.Column(db.Integer,primary_key=True)
    productID=db.Column(db.Integer,db.ForeignKey("product.id"))
    orderID=db.Column(db.Integer,db.ForeignKey("order.id"))
    quantity=db.Column(db.Integer)
    total=db.Column(db.Double)

    def __init__(self,product_id,order_id,quantity):
        self.productID=product_id
        self.orderID=order_id
        self.quantity=quantity
        self.total=self.__getPrice()*quantity

    def __getPrice(self):
        product=Product.query.filter_by(productID=self.productID)
        return product.pricePerUnit



