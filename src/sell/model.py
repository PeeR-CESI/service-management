from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://admin:admin@mongodb:27017")
db = client.your_service_db
sold_services_collection = db.sold_services

class SoldService:
    @staticmethod
    def create(sold_service_data):
        result = sold_services_collection.insert_one(sold_service_data)
        return str(result.inserted_id)

    @staticmethod
    def update(sold_service_id, sold_service_data):
        result = sold_services_collection.update_one(
            {"_id": ObjectId(sold_service_id)},
            {"$set": sold_service_data}
        )
        return result.modified_count > 0

    @staticmethod
    def delete(sold_service_id):
        result = sold_services_collection.delete_one({"_id": ObjectId(sold_service_id)})
        return result.deleted_count > 0

    @staticmethod
    def find(sold_service_id):
        result = sold_services_collection.find_one({"_id": ObjectId(sold_service_id)})
        if result:
            result['_id'] = str(result['_id'])
            return result
        return None
