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
    service = Service.find(service_id)
    if service:
        presta_id = service.presta_id
        success = Service.delete(service_id)
        if success:
            presta = User.query.get(presta_id)
            if presta and presta.service_ids:
                service_ids_list = presta.service_ids.split(',')
                if str(service_id) in service_ids_list:
                    service_ids_list.remove(str(service_id))
                    presta.service_ids = ','.join(service_ids_list)
                    db.session.commit()
            return jsonify({"message": "Service deleted successfully"}), 200
        else:
            return jsonify({"error": "Service not found"}), 404
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
