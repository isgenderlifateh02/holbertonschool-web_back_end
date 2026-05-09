#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays stats about Nginx logs.
    """
    # MongoDB-yə qoşuluruq
    client = MongoClient('mongodb://127.0.0.1:27017')
    # logs database-ni və nginx collection-u seçirik
    nginx_collection = client.logs.nginx

    # 1. Ümumi loq sayını tapırıq
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Metodlar üzrə statistika
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status check (method=GET, path=/status) sayını tapırıq
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
