# !/usr/bin/python3
"""
starting up a Flask web app
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """show the answer status"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def stats():
    """show the number of each type of item"""
    all_classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
                   "Review": "reviews", "State": "states", "User": "users"}
    return jsonify({v: storage.count(k) for k, v in all_classes.items()
                    if storage.count(k)})
