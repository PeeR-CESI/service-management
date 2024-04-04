from flask import Blueprint, request, jsonify
from .service import AvisService

avis_bp = Blueprint('avis_bp', __name__)
avis_service = AvisService()

@avis_bp.route('/add', methods=['POST'])
def add_avis():
    data = request.json
    response, status = AvisService.add_avis(data)
    return jsonify(response), status

@avis_bp.route('/<service_id>', methods=['GET'])
def get_avis(service_id):
    response, status = AvisService.get_avis_by_service(service_id)
    return jsonify(response), status

@avis_bp.route('/average/<service_id>', methods=['GET'])
def get_average_rating(service_id):
    response, status = avis_service.calculate_average_rating(service_id)
    return jsonify(response), status
