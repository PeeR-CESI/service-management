from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://admin:admin@mongodb:27017")
db = client.your_service_db
services_collection = db.services

class Service:
    @staticmethod
    def create(service_data):
        result = services_collection.insert_one(service_data)
        return str(result.inserted_id)

    @staticmethod
    def update(service_id, service_data):
        result = services_collection.update_one({"_id": ObjectId(service_id)}, {"$set": service_data})
        return result.modified_count > 0

    @staticmethod
    def delete(service_id):
        result = services_collection.delete_one({"_id": ObjectId(service_id)})
        return result.deleted_count > 0

    @staticmethod
    def find(service_id):
        result = services_collection.find_one({"_id": ObjectId(service_id)})
        if result:
            result['_id'] = str(result['_id'])
        return result
