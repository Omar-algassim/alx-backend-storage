#!/usr/bin/env python3
"""log stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient(host="localhost", port=27017)
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
    print("IPs:")
    ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
    