from flask import Blueprint, request
from .service import get_all_sell_services, create_sold_service, update_sold_service, delete_sold_service, get_sold_service

sell_bp = Blueprint('sell_bp', __name__)

@sell_bp.route('/', methods=['POST'])
def create():
    """
    Crée un nouveau service vendu
    ---
    tags:
      - sell
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - service_id
            - advancement
          properties:
            service_id:
              type: string
              description: ID du service de base.
            advancement:
              type: integer
              description: État d'avancement du service (chiffre de 0 à 5).
    responses:
      201:
        description: Service vendu créé avec succès.
      404:
        description: Service de base inexistant.
    """
    data = request.json
    service_id = data.get('service_id')
    return create_sold_service(service_id, data)

@sell_bp.route('/<sold_service_id>', methods=['PUT'])
def update(sold_service_id):
    """
    summary: Met à jour un service vendu, y compris le statut du service.
    ---
    tags:
      - sell
    consumes:
      - application/json
    parameters:
      - in: path
        name: sold_service_id
        required: true
        type: string
        description: ID du service vendu.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            advancement:
              type: integer
              description: Nouvel état d'avancement du service (chiffre de 0 à 5).
            status:
              type: string
              description: Statut du service ('validé', 'refusé', 'en attente').
    responses:
      200:
        description: Service vendu mis à jour avec succès.
      400:
        description: Requête invalide.
      404:
        description: Service vendu non trouvé.
    """
    data = request.json
    return update_sold_service(sold_service_id, data)

@sell_bp.route('/<sold_service_id>', methods=['DELETE'])
def delete(sold_service_id):
    """
    Supprime un service vendu
    ---
    tags:
      - sell
    parameters:
      - in: path
        name: sold_service_id
        required: true
        type: string
        description: ID du service vendu à supprimer.
    responses:
      200:
        description: Service vendu supprimé avec succès.
      404:
        description: Service vendu non trouvé.
    """
    return delete_sold_service(sold_service_id)

@sell_bp.route('/<sold_service_id>', methods=['GET'])
def get(sold_service_id):
    """
    Récupère les détails d'un service vendu
    ---
    tags:
      - sell
    parameters:
      - in: path
        name: sold_service_id
        required: true
        type: string
        description: ID du service vendu à récupérer.
    responses:
      200:
        description: Détails du service vendu.
      404:
        description: Service vendu non trouvé.
    """
    return get_sold_service(sold_service_id)

@sell_bp.route('/all', methods=['GET'])
def get_sell_services():
    """Récupère tous les services vendu
    ---
    tags:
      - sell
    responses:
      200:
        description: Liste de tous les services vendu
      404:
        description: Aucun service vendu trouvé
    """
    return get_all_sell_services()