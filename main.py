import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath('cafes.db')}"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    __tablename__ = "cafe"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


@app.route("/")
def home():
    query = db.select(Cafe)
    search_term = request.args.get("q", "").strip()
    if search_term:
        query = query.where(
            Cafe.name.ilike(f"%{search_term}%") | Cafe.location.ilike(f"%{search_term}%")
        )
    if request.args.get("wifi"):
        query = query.where(Cafe.has_wifi == True)
    if request.args.get("sockets"):
        query = query.where(Cafe.has_sockets == True)
    if request.args.get("toilet"):
        query = query.where(Cafe.has_toilet == True)

    all_cafes = db.session.execute(query).scalars().all()
    return render_template("index.html", cafes=all_cafes)

@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    if request.method == "POST":
        cafe.name = request.form.get("name")
        cafe.map_url = request.form.get("map_url")
        cafe.img_url = request.form.get("img_url")
        cafe.location = request.form.get("location")
        cafe.seats = request.form.get("seats")
        cafe.coffee_price = request.form.get("coffee_price")
        cafe.has_wifi = bool(request.form.get("has_wifi"))
        cafe.has_sockets = bool(request.form.get("has_sockets"))
        cafe.has_toilet = bool(request.form.get("has_toilet"))
        cafe.can_take_calls = bool(request.form.get("can_take_calls"))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", cafe=cafe)

@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            can_take_calls=bool(request.form.get("can_take_calls")),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect((url_for("home")))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)