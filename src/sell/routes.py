from flask import Blueprint, request
from .service import create_sold_service, update_sold_service, delete_sold_service, get_sold_service

sell_bp = Blueprint('sell_bp', __name__)

@sell_bp.route('/', methods=['POST'])
def create():
    data = request.json
    service_id = data.get('service_id')
    return create_sold_service(service_id, data)

@sell_bp.route('/<sold_service_id>', methods=['PUT'])
def update(sold_service_id):
    data = request.json
    return update_sold_service(sold_service_id, data)

@sell_bp.route('/<sold_service_id>', methods=['DELETE'])
def delete(sold_service_id):
    return delete_sold_service(sold_service_id)

@sell_bp.route('/<sold_service_id>', methods=['GET'])
def get(sold_service_id):
    return get_sold_service(sold_service_id)
