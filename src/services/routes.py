from flask import Blueprint, request
from .service import create_service, update_service, delete_service, get_service

service_bp = Blueprint('service', __name__)

@service_bp.route('/create', methods=['POST'])
def create():
    """Crée un nouveau service
    ---
    tags:
      - service
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          id: ServiceData
          required:
            - nom
            - description
          properties:
            nom:
              type: string
              description: Nom du service.
            description:
              type: string
              description: Description du service.
            price:
              type: string
              description: Description du service.
    responses:
      201:
        description: Service créé avec succès.
    """
    service_data = request.json
    return create_service(service_data)

@service_bp.route('/update/<service_id>', methods=['PUT'])
def update(service_id):
    """Mise à jour d'un service existant
    ---
    tags:
      - service
    consumes:
      - application/json
    parameters:
      - in: path
        name: service_id
        type: string
        required: true
        description: L'ID du service à mettre à jour.
      - in: body
        name: body
        schema:
          id: ServiceUpdate
          required:
            - nom
            - description
          properties:
            nom:
              type: string
              description: Nouveau nom du service.
            description:
              type: string
              description: Nouvelle description du service.
    responses:
      200:
        description: Service mis à jour avec succès.
      404:
        description: Service non trouvé.
    """
    service_data = request.json
    return update_service(service_id, service_data)

@service_bp.route('/delete/<service_id>', methods=['DELETE'])
def delete(service_id):
    """Suppression d'un service
    ---
    tags:
      - service
    parameters:
      - in: path
        name: service_id
        type: string
        required: true
        description: L'ID du service à supprimer.
    responses:
      200:
        description: Service supprimé avec succès.
      404:
        description: Service non trouvé.
    """
    return delete_service(service_id)

@service_bp.route('/<service_id>', methods=['GET'])
def get(service_id):
    """Récupération d'un service par son ID
    ---
    tags:
      - service
    parameters:
      - in: path
        name: service_id
        type: string
        required: true
        description: L'ID du service à récupérer.
    responses:
      200:
        description: Service récupéré avec succès.
      404:
        description: Service non trouvé.
    """
    return get_service(service_id)