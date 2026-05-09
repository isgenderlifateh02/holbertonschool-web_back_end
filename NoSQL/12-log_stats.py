#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays stats about Nginx logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Ümumi loq sayı
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Metodlar
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # Burada tam olaraq 4 boşluq (və ya \t) olmalıdır
        print(f"    method {method}: {count}")

    # 3. Status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
