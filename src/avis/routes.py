from flask import Blueprint, request, jsonify
from .service import AvisService

avis_bp = Blueprint('avis_bp', __name__)
avis_service = AvisService()

@avis_bp.route('/add', methods=['POST'])
def add_avis():
    """Ajoute un avis pour un service
    ---
    tags:
      - avis
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          id: AvisData
          required:
            - service_id
            - commentaire
            - note
          properties:
            service_id:
              type: string
              description: L'ID du service.
            commentaire:
              type: string
              description: Le commentaire de l'avis.
            note:
              type: integer
              description: La note donnée au service.
    responses:
      201:
        description: Avis ajouté avec succès.
    """
    data = request.json
    response, status = AvisService.add_avis(data)
    return jsonify(response), status

@avis_bp.route('/<service_id>', methods=['GET'])
def get_avis(service_id):
    """Obtient les avis pour un service spécifique
    ---
    tags:
      - avis
    parameters:
      - name: service_id
        in: path
        type: string
        required: true
        description: L'ID du service pour lequel obtenir les avis.
    responses:
      200:
        description: Une liste des avis pour le service spécifié.
        schema:
          type: array
          items:
            $ref: '#/definitions/Avis'
      404:
        description: Aucun avis trouvé pour ce service.
    definitions:
      Avis:
        type: object
        properties:
          service_id:
            type: string
            description: L'ID du service évalué.
          commentaire:
            type: string
            description: Le commentaire laissé par l'utilisateur.
          note:
            type: integer
            description: La note donnée au service.
    """
    response, status = AvisService.get_avis_by_service(service_id)
    return jsonify(response), status

@avis_bp.route('/average/<service_id>', methods=['GET'])
def get_average_rating(service_id):
    """Calcule la note moyenne des avis pour un service spécifique
    ---
    tags:
      - avis
    parameters:
      - name: service_id
        in: path
        type: string
        required: true
        description: L'ID du service pour lequel calculer la note moyenne.
    responses:
      200:
        description: La note moyenne des avis pour le service spécifié.
        schema:
          type: object
          properties:
            moyenne:
              type: number
              description: La note moyenne calculée des avis.
      404:
        description: Aucun avis trouvé pour calculer une moyenne pour ce service.
    """
    response, status = avis_service.calculate_average_rating(service_id)
    return jsonify(response), status
