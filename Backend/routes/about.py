from flask import Blueprint, jsonify

about_bp = Blueprint("about", __name__, url_prefix="/api")


@about_bp.get("/about")
def get_about():
    return jsonify({
        "message": "About route is working"
    })
  
