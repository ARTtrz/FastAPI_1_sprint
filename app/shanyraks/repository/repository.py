
from pymongo.database import Database

from bson.objectid import ObjectId


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database
    
    def create_shanyrak(self, shanyrak: dict):
        payload = {
            "type": shanyrak["type"],
            "price": shanyrak["price"],
            "address": shanyrak["address"],
           "area": shanyrak["area"],
            "rooms_count": shanyrak["rooms_count"],
            "description": shanyrak["description"]
        }

        

        self.database["shanyraks"].insert_one(payload)
    
        

    def findById(self, id:str):
        shanyrak = self.database["shanyraks"].find_one({"_id": ObjectId(id) })
        return shanyrak


    def update_shanyrak(self, id: str, data: dict):
        
        shanyrak = self.database["shanyraks"].update_one({"_id": ObjectId(id)}, {"$set": data})

        
        if shanyrak.modified_count > 0:
            return {"message": "Shanyrak updated successfully"}
        else:
            return {"message": "No changes were made to the shanyrak"}

    def delete_shanyrak(self, id: str):
        shanyrak = self.database["shanyraks"].delete_one({"_id": ObjectId(id)})
        return {"message": "successfully deleted"}    
