from flask import Blueprint, request
from .service import create_sold_service, update_sold_service, delete_sold_service, get_sold_service

sell_bp = Blueprint('sell_bp', __name__)

@sell_bp.route('/', methods=['POST'])
def create():
    """
    Crée un nouveau service vendu, incluant les informations du service parent au moment de la vente
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
        description: Service vendu créé avec succès. Les informations du service parent sont incluses.
      404:
        description: Service de base inexistant.
    """
    data = request.json
    service_id = data.get('service_id')
    return create_sold_service(service_id, data)

@sell_bp.route('/<sold_service_id>', methods=['PUT', 'DELETE', 'GET'])
def sell_operations(sold_service_id):
    """
    Opérations sur un service vendu: récupération, mise à jour et suppression.
    ---
    tags:
      - sell
    operations:
      - method: GET
        summary: Récupère les détails d'un service vendu.
        parameters:
          - in: path
            name: sold_service_id
            required: true
            type: string
            description: ID du service vendu.
        responses:
          200:
            description: Détails du service vendu.
          404:
            description: Service vendu non trouvé.

      - method: PUT
        summary: Met à jour un service vendu, y compris le statut du service.
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
                status:
                  type: string
                  description: Statut du service ('validé', 'refusé', 'en attente').
                # Ajoutez ici d'autres champs que vous pouvez mettre à jour.
        responses:
          200:
            description: Service vendu mis à jour avec succès.
          400:
            description: Requête invalide.
          404:
            description: Service vendu non trouvé.

      - method: DELETE
        summary: Supprime un service vendu.
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
    if request.method == 'PUT':
        data = request.json
        return update_sold_service(sold_service_id, data)
    elif request.method == 'DELETE':
        return delete_sold_service(sold_service_id)
    elif request.method == 'GET':
        return get_sold_service(sold_service_id)
      