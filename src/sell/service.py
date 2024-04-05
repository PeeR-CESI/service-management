from flask import jsonify
from src.services.model import Service as BaseService
from .model import SoldService

def create_sold_service(service_id, sold_service_data):
    # Verify that the base service exists
    if not BaseService.find(service_id):
        return jsonify({"error": "Base service does not exist"}), 404

    sold_service_id = SoldService.create(sold_service_data)
    return jsonify({"message": "Sold service created successfully", "sold_service_id": sold_service_id}), 201

def update_sold_service(sold_service_id, sold_service_data):
    if SoldService.update(sold_service_id, sold_service_data):
        return jsonify({"message": "Sold service updated successfully"}), 200
    else:
        return jsonify({"error": "Sold service not found"}), 404

def delete_sold_service(sold_service_id):
    if SoldService.delete(sold_service_id):
        return jsonify({"message": "Sold service deleted successfully"}), 200
    else:
        return jsonify({"error": "Sold service not found"}), 404

def get_sold_service(sold_service_id):
    sold_service = SoldService.find(sold_service_id)
    if sold_service:
        return jsonify(sold_service), 200
    else:
        return jsonify({"error": "Sold service not found"}), 404
