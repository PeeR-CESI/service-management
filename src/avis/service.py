from .model import AvisModel
from flask import jsonify

class AvisService:
    @staticmethod
    def add_avis(data):
        service_id = data.get("service_id")
        commentaire = data.get("commentaire")
        note = data.get("note")

        if not AvisModel.service_exists(service_id):
            return {"error": "Service not found"}, 404

        avis_id = AvisModel.add_avis(service_id, commentaire, note)
        return {"message": "Avis ajouté avec succès", "avis_id": str(avis_id)}, 201

    @staticmethod
    def get_avis_by_service(service_id):
        avis_list = AvisModel.get_avis_by_service(service_id)
        if avis_list:
            return avis_list, 200  # Renvoie une liste d'avis et un statut HTTP 200
        else:
            return {"error": "Aucun avis trouvé"}, 404  # Renvoie une erreur et un statut HTTP 404

    @staticmethod
    def calculate_average_rating(service_id):
        average = AvisModel.calculate_average_rating(service_id)
        return jsonify({"moyenne": average}), 200 if average is not None else jsonify({"error": "Aucun avis trouvé pour ce service"}), 404
