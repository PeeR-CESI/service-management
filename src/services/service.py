from .model import Service
from flask import jsonify

def create_service(service_data):
    service_id = Service.create(service_data)
    return jsonify({"message": "Service created successfully", "service_id": service_id}), 201

def update_service(service_id, service_data):
    if Service.update(service_id, service_data):
        return jsonify({"message": "Service updated successfully"}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

def delete_service(service_id):
    if Service.delete(service_id):
        return jsonify({"message": "Service deleted successfully"}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

def get_service(service_id):
    service = Service.find(service_id)
    if service:
        return jsonify(service), 200
    else:
        return jsonify({"error": "Service not found"}), 404


def get_all_services():
    services = Service.find_all()
    for service in services:
        # Convertir ObjectId en str
        service['_id'] = str(service['_id'])
    return jsonify(services), 200