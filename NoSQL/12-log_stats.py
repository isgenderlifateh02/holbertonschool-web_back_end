#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
"""
from pymongo import MongoClient

if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    
    number_of_logs = nginx_collection.count_documents({})
    print("{} logs".format(number_of_logs))
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods_list:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    
    status_number = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_number))
