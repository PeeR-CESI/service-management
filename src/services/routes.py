from flask import Blueprint, request
from .service import create_service, update_service, delete_service, get_service

service_bp = Blueprint('service', __name__)

@service_bp.route('/create', methods=['POST'])
def create():
    service_data = request.json
    return create_service(service_data)

@service_bp.route('/update/<service_id>', methods=['PUT'])
def update(service_id):
    service_data = request.json
    return update_service(service_id, service_data)

@service_bp.route('/delete/<service_id>', methods=['DELETE'])
def delete(service_id):
    return delete_service(service_id)

@service_bp.route('/<service_id>', methods=['GET'])
def get(service_id):
    return get_service(service_id)
