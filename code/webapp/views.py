from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .mymodels import Product, Category, Order, OrderDetails
from .forms import OrderForm, SearchForm
from . import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

main_bp = Blueprint("main", __name__)


# category
@main_bp.route("/")
def index():
    Categorys = Category.query.order_by(Category.name).all()
    return render_template("index.html", Categorys=Categorys)


# products
@main_bp.route("/products/<int:categoryid>")
def categoryproducts(categoryid):
    Products = Product.query.filter(Product.category_id == categoryid).all()
    return render_template("categoryproducts.html", Products=Products)


# item details pages
@main_bp.route("/itemdetails/<int:product_id>")
def itemdetailspage(product_id):
    product = Product.query.get(product_id)
    if product:
        return render_template(
            "itemdetailspage.html", Product=product, product_id=product_id
        )
    else:
        return render_template(
            "error.html", message="Product was not found in our warehouse!"
        )


# search
@main_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    categories = Category.query.filter(Category.name.ilike(f"%{query}%")).all()
    products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    return render_template(
        "search.html", categories=categories, products=products, query=query
    )


# basket = order
@main_bp.route("/order", methods=["POST", "GET"])
def order():
    quantity = 1
    product_id = None

    if request.method == "POST":
        product_id = request.form.get("product_id")
        quantity = int(request.form.get("quantity", 1))

    print(f"quantity: {quantity}")
    print(f"product_id: {product_id}")

    # retrieve or create order
    if "order_id" in session.keys():
        order = db.session.scalar(
            db.select(Order).where(Order.id == session["order_id"])
        )
    else:
        order = None

    if order is None:
        order = Order(
            status=False,
            first_name="",
            surname="",
            email="",
            shipping_address="",
            total_price=0,
        )
        try:
            db.session.add(order)
            db.session.commit()
            session["order_id"] = order.id
        except SQLAlchemyError as e:  # catch database exception
            print(f"Failed at creating a new order: {str(e)}")
            order = None

    # adding item or items to order
    if product_id is not None and order is not None:
        product = db.session.scalar(db.select(Product).where(Product.id == product_id))

        # check if the product is already in the order.products
        existing_product = next((p for p in order.products if p.id == product.id), None)

        if existing_product:
            existing_product.quantity += quantity  # update existing product quantity
        else:
            product.quantity = quantity  # set quantity for the new product
            order.products.append(product)  # add the new product to the order

        try:
            db.session.commit()
        except SQLAlchemyError as e:  # catch database exception
            flash(
                "There was an issue adding the item to your basket", category="danger"
            )
            print(f"Failed at adding item to order: {str(e)}")
            return redirect(url_for("main.order"))

    # calculate total price after
    total_price = sum(product.price * product.quantity for product in order.products)

    return render_template("order.html", order=order, total_price=total_price)


# Delete specific basket item
@main_bp.route("/deleteorderitem", methods=["POST"])
def deleteorderitem():
    product_id = request.form["id"]
    if "order_id" in session:
        order = Order.query.get_or_404(session["order_id"])
        product_to_delete = Product.query.get(product_id)

        try:
            product_price = product_to_delete.price
            order.products.remove(product_to_delete)
            order.total_price -= product_price
            db.session.commit()
            return redirect(url_for("main.order"))
        except Exception as e:
            print(e)
            return render_template("error.html", message="Something's gone wrong.")
    return redirect(url_for("main.order"))


# Scrap gym bag
@main_bp.route("/deleteorder")
def deleteorder():
    if "order_id" in session:
        del session["order_id"]
        flash(
            "All items have now been deleted, return to the products page to start shopping again!"
        )
    return redirect(url_for("main.index"))


# form post
@main_bp.route("/checkout", methods=["POST", "GET"])
def checkout():
    form = OrderForm()
    if "order_id" in session:
        order = Order.query.get_or_404(session["order_id"])

        if form.validate_on_submit():
            # details from form
            order.status = True
            order.first_name = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.shipping_address = form.shipping_address.data
            order.date = datetime.now()

            try:
                db.session.commit()
                del session["order_id"]
                flash(
                    "Thank you! Your order has been sent to our warehouse for packing!"
                )
                return redirect(url_for("main.index"))
            except:
                return "There was an issue completing your order, Please try again or delete your basket and repeat!"

    return render_template("checkout.html", form=form)
