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
    # Trouver le service à supprimer pour obtenir l'ID du prestataire
    service = Service.find(service_id)
    if service:
        presta_id = service.presta_id  # Assurez-vous que cette propriété existe dans vos modèles de service
        
        # Supprimer le service
        success = Service.delete(service_id)
        if success:
            # Trouver le prestataire pour mettre à jour sa liste de services
            presta = User.query.get(presta_id)
            if presta:
                if presta.service_ids:
                    # Convertir la chaîne en liste, retirer l'ID du service, puis reconstruire la chaîne
                    service_ids_list = presta.service_ids.split(',')
                    if str(service_id) in service_ids_list:  # Assurez-vous que les types correspondent
                        service_ids_list.remove(str(service_id))  # Convertir service_id en str si nécessaire
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
