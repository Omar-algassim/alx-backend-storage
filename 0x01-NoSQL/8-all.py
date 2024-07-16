#!/usr/bin/env python3
"""list all documents in collection"""


def list_all(mongo_collection):
    """list all documents in collection"""
    return [doc for doc in mongo_collection.find()]
