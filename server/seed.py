#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    print("Clearing database...")
    Plant.query.delete()

    print("Creating plants...")
    plant1 = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
        is_in_stock=True
    )
    plant2 = Plant(
        name="Fiddle Leaf Fig",
        image="./images/fiddle-leaf-fig.jpg",
        price=35.00,
        is_in_stock=True
    )
    plant3 = Plant(
        name="Snake Plant",
        image="./images/snake-plant.jpg",
        price=15.00,
        is_in_stock=True
    )
    plant4 = Plant(
        name="Monstera",
        image="./images/monstera.jpg",
        price=25.00,
        is_in_stock=True
    )
    plant5 = Plant(
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=18.50,
        is_in_stock=True
    )
    plant6 = Plant(
        name="Pothos",
        image="./images/pothos.jpg",
        price=10.00,
        is_in_stock=True
    )
    plant7 = Plant(
        name="Bird of Paradise",
        image="./images/bird-of-paradise.jpg",
        price=45.00,
        is_in_stock=True
    )
    plant8 = Plant(
        name="Rubber Plant",
        image="./images/rubber-plant.jpg",
        price=22.00,
        is_in_stock=True
    )

    db.session.add_all([
        plant1,
        plant2,
        plant3,
        plant4,
        plant5,
        plant6,
        plant7,
        plant8
    ])
    db.session.commit()

    print("Done!")