from random import choice as rc

from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print("Creating tables if they don't exist...")
        db.create_all()  # Ensures tables are present before seeding

        print("Clearing database...")
        HeroPower.query.delete()
        Hero.query.delete()
        Power.query.delete()

        print("Seeding powers...")
        powers = [
            Power(name="super strength", description="Gives the wielder incredible physical power beyond human limits."),
            Power(name="flight", description="Allows the wielder to fly at supersonic speeds across vast distances."),
            Power(name="super human senses", description="Enhances all five senses to super-human levels for awareness."),
            Power(name="elasticity", description="Allows the body to stretch, bend, and twist at extreme lengths."),
        ]
        db.session.add_all(powers)

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]
        db.session.add_all(heroes)

        print("Assigning powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = [
            HeroPower(hero=rc(heroes), power=rc(powers), strength=rc(strengths))
            for _ in range(15)
        ]
        db.session.add_all(hero_powers)

        db.session.commit()
        print("Done seeding!")
