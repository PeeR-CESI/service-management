from .model import Service, User, db
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
    # Exemple de récupération du service et du presta_id associé
    service = db.find_service_by_id(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    presta_id = service.presta_id

    # Suppression du service
    db.delete_service(service_id)

    # Mise à jour de la liste des service_ids pour le presta
    presta = db.find_user_by_id(presta_id)
    if presta and 'service_ids' in presta:
        if service_id in presta['service_ids']:
            presta['service_ids'].remove(service_id)
            db.update_user(presta_id, {'service_ids': presta['service_ids']})

    return jsonify({"message": "Service deleted successfully"}), 200

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
