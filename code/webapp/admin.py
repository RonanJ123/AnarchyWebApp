from flask import Blueprint
from . import db
from .mymodels import Product, Order, Category, OrderDetails


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# function to put some seed data in the database
@admin_bp.route("/dbseed")
def dbseed():
    category1 = Category(
        name="Base Steroids",
        description="This category of steroids facilitates a solid foundation to build your perfect cycle off. By utilising one or more of these you will be almost guarenteed to have successful cycle!!",
    )

    category2 = Category(
        name="Sports Performance",
        description="This category of steroids is catered to athletic perfomance making it perfect for any and all athletes of any genre. Whether you are seeking performance gains or help recovering this is the section for you",
    )

    category3 = Category(
        name="Post Cycle Therapy + Health",
        description="This category of steroids is for individuals coming off cycle and seeking extra support for their body to recover. These supplements will support your body through the process of recovery aswell as in some cases sexual health recovery.",
    )

    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return "There was in issue, try again!"

    product1 = Product(
        name="Testosterone",
        price=89.99,
        description="Testosterone is a naturally occuring hormone in both males and females, Testosterone should be a base steroid implemented in all successfull and effective stacks.",
        image="Testosterone.jpg",
        quantity=1,
        itemdetails="Ingredients: 100% Testosterone Enanthate Solution- Pharmacy Grade. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category1.id,
    )

    product2 = Product(
        name="Trenbolone-Acetate",
        price=94.99,
        description="100ml size. Tren is the ultimate muscle growth and fat stripping steroid. Trenbolone can be paired with a base of testosterone or fueled with an oral to kickstart the effects.",
        image="Trenbolone-Acetate.jpg",
        quantity=1,
        itemdetails="95% Trenbolone Acetate Solution - Pharmacy Grade. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category1.id,
    )
    product3 = Product(
        name="Masteron-Propionate",
        price=60,
        description="Drostanolone Propionate or Masteron is a major muscle builder.Masteron alsoreduces metabolism resulting in lower appetite which allows for easy weight loss leading to a shredded body.",
        image="Masteron-Propionate.jpg",
        quantity=1,
        itemdetails="50ml Bottle Pharmacy Grade - Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category1.id,
    )
    product4 = Product(
        name="Human-Growth-Hormone",
        price=77.50,
        description="HGH helps your body increase lean muscle mass and can also burn fat at the same time ideal for endurance athletes.",
        image="Human-Growth-Hormone.jpg",
        quantity=1,
        itemdetails="80ml Bottle HGH 100% Pure. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk ",
        category_id=category2.id,
    )

    product5 = Product(
        name="Creatine-Monohydrate",
        price=40,
        description="Creatine improves muscle strength and power by allowing more water to flow into your muscles. It is perfect for sprinters or athletes with short events.",
        image="Creatine-Monohydrate.webp",
        quantity=1,
        itemdetails="200g Tub of Pure Creatine Monohydrate. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category2.id,
    )

    product6 = Product(
        name="Albuterol",
        price=30,
        description="Albuterol works within the lungs relaxing the broncial tubes. This allows more air to flow in resulting in higher oxygen levels within the body leading to increased athletic performance.",
        image="Albuterol.webp",
        quantity=1,
        itemdetails="30 tablets, Albuterol 100%. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category2.id,
    )

    product7 = Product(
        name="Milk-Thistle",
        price=55,
        description="Milk thistle has many benefits that help your liver both on and off cycle.It protects your liver from all toxins and helps you recover.",
        image="Milk-Thistle.jpg",
        quantity=1,
        itemdetails="60 Gummies , Mix of Milk Thistle + Vitamins. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category3.id,
    )

    product8 = Product(
        name="Nolvadex",
        price=25.99,
        description="Nolvadex is originally used as an aromatase inhibitor but also regulates post cycle estrogen levels in your body keeping you healthy.",
        image="Nolvadex.jpg",
        quantity=1,
        itemdetails="30 Tablets of 95% Nolvadex 5% Arimidex. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category3.id,
    )

    product9 = Product(
        name="Clomid",
        price=15,
        description="Clomid is used for men post cycle to increase and bring back their fertility.It leads to an increase in natural tesosterone and sperm count.",
        image="Clomid.jpg",
        quantity=1,
        itemdetails="10 tablets, of 100% Clomid Mix. Health Warning- Rad Ronans Roids pty ltd does not accept any fault for health issues as a result ofconsuming any of our products. We are not subject to any liability. Take at your own risk",
        category_id=category3.id,
    )

    try:
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)
        db.session.add(product5)
        db.session.add(product6)
        db.session.add(product7)
        db.session.add(product8)
        db.session.add(product9)
        db.session.commit()
    except:
        return "There was an issue adding a product in dbseed function"

    return "DATA LOADED, Database initilised.... hacking the mainframe..."
