#!/usr/bin/python3
"""Flask with general routes"""
from api.v1.views import app_views
from flask import jsonify
import json
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review

classes = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}


@app_views.route("/status", methods=['GET'])
def status():
    """Returns a JSON status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'])
def stats():
    """
    Retrieves the number of each objects by type
    """
    dict = {}
    for key, value in classes.items():
        dict[key] = storage.count(value)
    return jsonify(dict)
