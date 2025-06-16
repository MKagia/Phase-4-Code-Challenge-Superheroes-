from flask import Blueprint, request, jsonify
from .models import Hero, Power, HeroPower
from . import db

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@api.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    hero_data = hero.to_dict()
    hero_data["hero_powers"] = [hp.to_dict() for hp in hero.hero_powers]
    return jsonify(hero_data), 200

@api.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

@api.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@api.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    try:
        data = request.get_json()
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

@api.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
