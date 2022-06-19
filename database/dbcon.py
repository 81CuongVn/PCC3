from http import server
from typing import MutableSequence
import pymongo
from decouple import config

tserv = "5"
tuser = "1234"
troles = ["1234", "12345", "123456"]

pakkucli  = pymongo.MongoClient("mongodb+srv://" + config('MONGODB_USER') + ":" + config('MONGODB_PWD') + "@" + config('MONGODB_HOST') + "/?retryWrites=true&w=majority")

pakkumdb = pakkucli["main"]
pakkucol = pakkumdb["servers"]

collist = pakkumdb.list_collection_names()


#
#        SERVER MANAGEMENT
#

class Server:
    def __init__(self, server_id):
        self.server_id = server_id
        self.server = pakkumdb[server_id]
        self.server_col = self.server["servers"]


    class User:
        def __init__(self, server_id, user_id):
            self.server_id = server_id
            self.user_id = user_id
            self.server = pakkumdb[server_id]
            self.server_col = self.server["users"]

        def add(server_id, user_id):
            server = pakkucol[server_id]["users"]
            if server.find_one({"user_id": user_id}):
                return False
            else:
                server.insert_one({"user_id": user_id})
                return True

        def remove(server_id, user_id):
            server = pakkucol[server_id]["users"]
            if server.find_one({"user_id": user_id}):
                server.delete_one({"user_id": user_id})
                return True
            else:
                return False


        class Add:
            def __init__(self, server_id, user_id):
                self.server_id = server_id
                self.user_id = user_id
                self.server = pakkumdb[server_id]
                self.server_col = self.server["users"]

            def prole(server_id, user_id, role_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"proles": role_id}})
                return True

            def warn(server_id, user_id, warn_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"warns": warn_content}})
                return True

            def note(server_id, user_id, note_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"notes": note_content}})
                return True

            def ban(server_id, user_id, ban_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"bans": ban_reason}})
                return True

            def kick(server_id, user_id, kick_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"kicks": kick_reason}})
                return True

            def mute(server_id, user_id, mute_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {"mutes": mute_reason}})
                return True

            def custom(server_id, user_id, custom_name, custom_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$push": {custom_name: custom_content}})
                return True


        class Remove:
            def __init__(self, server_id, user_id):
                self.server_id = server_id
                self.user_id = user_id
                self.server = pakkumdb[server_id]
                self.server_col = self.server["users"]

            def prole(server_id, user_id, role_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"proles": role_id}})
                return True

            def warn(server_id, user_id, warn_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"warns": warn_content}})
                return True

            def note(server_id, user_id, note_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"notes": note_content}})
                return True

            def ban(server_id, user_id, ban_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"bans": ban_reason}})
                return True

            def kick(server_id, user_id, kick_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"kicks": kick_reason}})
                return True

            def mute(server_id, user_id, mute_reason):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {"mutes": mute_reason}})
                return True

            def custom(server_id, user_id, custom_name, custom_content):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                server.update_one({"user_id": user_id}, {"$pull": {custom_name: custom_content}})
                return True


        class Get:
            def __init__(self, server_id, user_id):
                self.server_id = server_id
                self.user_id = user_id
                self.server = pakkumdb[server_id]
                self.server_col = self.server["users"]

            def all(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                return server.find_one({"user_id": user_id})

            def proles(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    proles = user["proles"]
                except:
                    proles = "None"
                return proles

            def warns(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    warns = user["warns"]
                except:
                    warns = "None"
                return warns

            def notes(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    warns = user["warns"]
                except:
                    warns = "None"
                return warns

            def bans(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    bans = user["bans"]
                except:
                    bans = "None"
                return bans

            def kicks(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    kicks = user["kicks"]
                except:
                    kicks = "None"
                return kicks

            def mutes(server_id, user_id):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    mutes = user["mutes"]
                except:
                    mutes = "None"
                return mutes

            def custom(server_id, user_id, custom_name):
                server = pakkucol[server_id]["users"]
                if not server.find_one({"user_id": user_id}):
                    server.insert_one({"user_id": user_id})
                try:
                    user = server.find_one({"user_id": user_id})
                    custom = user[custom_name]
                except:
                    custom = "None"
                return custom


    class Get:
        #NOT WORKING YET
        def __init__(self, server_id):
            self.server_id = server_id
            self.server = pakkumdb[server_id]
            self.server_col = self.server["servers"]

        def all():
            return pakkucol.find()

        def all_users(server_id):
            server = pakkucol[server_id]["users"]
            users = server["users"]
            users = users.find()
            user_list = []
            for user in users:
                user_list.append(user["user_id"])
            return user_list

        def custom(server_id, custom_name):
            server = pakkucol[server_id]["servers"]
            try:
                custom = server.find_one({"custom": custom_name})
                custom = custom[custom_name]
            except:
                custom = "None"
            return custom

        def actions(server_id):
            server = pakkucol[server_id]["logs"]
            try:
                actions = server.find_one({"logs": "actions"})
                actions = actions["actions"]
            except:
                actions = "None"
            return actions


    class Add:
        def __init__(self, server_id):
            self.server_id = server_id
            self.server = pakkumdb[server_id]
            self.server_col = self.server["servers"]

        def custom(server_id, custom_name, custom_value):
            server = pakkucol[server_id]["custom"]
            if not server.find_one({"custom": custom_name}):
                server.insert_one({"custom": custom_name})
            server.update_one({"custom": custom_name}, {"$push": {"value": custom_value}})
            return True

        def action(server_id, action_content):
            server = pakkucol[server_id]["logs"]
            if not server.find_one({"logs": "actions"}):
                server.insert_one({"logs": "actions"})
            server.update_one({"logs": "actions"}, {"$push": {"actions": action_content}})
            return True

    def add(server_id):
        pakkucol.insert_one({"server_id": server_id})
        return True

    def remove(server_id):
        pakkucol.delete_one({"server_id": server_id})
        return True


print("All checks complete\nDB Accessible")

#print(Server.User.add("5", "1234"))
#print(Server.User.Add.prole("5", "1234", "1234"))
#print(Server.Add.action("953778083041800293", "test"))
#print(Server.Get.actions("953778083041800293"))
#print(Server.User.Get.mutes("953778083041800293", "877193079952654427"))