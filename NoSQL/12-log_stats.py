#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Display stats about Nginx logs in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Ümumi log sayı
    total = collection.count_documents({})
    print(f"{total} logs")

    # Metodların siyahısı
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        # DİQQƏT: Burada \t yerinə dəqiq 4 boşluq istifadə edirik
        print(f"    method {method}: {count}")

    # Status check (method=GET və path=/status)
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
