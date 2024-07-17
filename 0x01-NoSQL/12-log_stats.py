#!/usr/bin/env python3
"""log stats"""
from pymongo import MongoClient


client = MongoClient()
logs = client.logs.nginx

print(logs.count_documents({}), "logs")
print("Methods:")
print("\tmethod GET:", logs.count_documents({"method": "GET"}))
print("\tmethod POST:", logs.count_documents({"method": "POST"}))
print("\tmethod PUT:", logs.count_documents({"method": "PUT"}))
print("\tmethod PATCH:", logs.count_documents({"method": "PATCH"}))
print("\tmethod DELETE:", logs.count_documents({"method": "DELETE"}))
print(logs.count_documents(
    {"method": "GET", "path": "/status"}), "status check")
