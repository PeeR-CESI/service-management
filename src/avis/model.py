from pymongo import MongoClient
from bson.objectid import ObjectId

# Connexion à MongoDB
client = MongoClient("mongodb://admin:admin@mongodb:27017")
db = client.your_service_db
services_collection = db.services

class AvisModel:
    @staticmethod
    def service_exists(service_id):
        service = db.services.find_one({'_id': ObjectId(service_id)})
        return service is not None
    @staticmethod
    def add_avis(service_id, commentaire, note):
        avis_document = {
            "service_id": ObjectId(service_id),
            "commentaire": commentaire,
            "note": note
        }
        return db.avis.insert_one(avis_document).inserted_id

    @staticmethod
    def get_avis_by_service(service_id):
        # Recherche des avis pour un service donné
        avis_cursor = db.avis.find({"service_id": ObjectId(service_id)})

        # Création de la liste des avis, conversion des ObjectId en strings
        avis_list = []
        for avis in avis_cursor:
            avis['_id'] = str(avis['_id'])  # Convertir ObjectId en string
            avis['service_id'] = str(avis['service_id'])  # Convertir ObjectId en string
            avis_list.append(avis)  # Ajouter l'avis modifié à la liste

        return avis_list

    @staticmethod
    def calculate_average_rating(service_id):
        pipeline = [
            {"$match": {"service_id": ObjectId(service_id)}},
            {"$group": {"_id": None, "average": {"$avg": "$note"}}}
        ]
        result = list(db.avis.aggregate(pipeline))
        return result[0]['average'] if result else None