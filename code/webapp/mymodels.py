from . import db

OrderDetails = db.Table(
    "OrderDetails",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("quantity", db.Integer, nullable=False, default=1),
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), nullable=False),
    db.Column("product_id", db.Integer, db.ForeignKey("Product.id"), nullable=False),
    db.UniqueConstraint("order_id", "product_id"),
)


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))
    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}"


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    image = db.Column(db.String(60), nullable=False, default="defaultcity.jpg")
    quantity = db.Column(db.Integer, nullable=False, default=1)
    itemdetails = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("Category.id"), nullable=False)
    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: ${self.price}\nImage: {self.image}\nQuantity: {self.quantity}"


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(60))
    shipping_address = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float)

    products = db.relationship("Product", secondary="OrderDetails", backref="orders")

    def __repr__(self):
        return f"ID: {self.id}\nStatus: {self.status}\nFirst Name: {self.first_name}\nSurname: {self.surname}\nProducts: {self.products}\nTotal Cost: ${self.total_cost}"
