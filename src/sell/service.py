from flask import jsonify
from .model import SoldService, client
from bson.objectid import ObjectId
from ..services.model import Service

def service_exists(service_id):
    db = client.your_service_db
    services_collection = db.services
    return services_collection.find_one({'_id': ObjectId(service_id)}) is not None

def create_sold_service(service_id, sold_service_data):
    if not service_exists(service_id):
        return jsonify({"error": "Base service does not exist"}), 404
    
    parent_service = Service.find(service_id)
    if parent_service:
        sold_service_data['name'] = parent_service.get("nom")
        sold_service_data['description'] = parent_service.get("description")
        sold_service_data['price'] = parent_service.get("price")
        sold_service_data['presta_id'] = parent_service.get("presta_id")
    else:
        return jsonify({"error": "Parent service not found"}), 404

    sold_service_data['status'] = "en attente"
    
    sold_service_id = SoldService.create(sold_service_data)
    return jsonify({"message": "Sold service created successfully", "sold_service_id": sold_service_id}), 201


def update_sold_service(sold_service_id, sold_service_data):
    if 'status' in sold_service_data:
        if sold_service_data['status'] not in ["validé", "refusé", "en attente", "en cours", "terminé"]:
            return jsonify({"error": "Statut invalide"}), 400
    
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

def get_all_sell_services():
    sold_services = SoldService.find_all()
    for sold_service in sold_services:
        # Convertir ObjectId en str
        sold_service['_id'] = str(sold_service['_id'])
    return jsonify(sold_services), 200
