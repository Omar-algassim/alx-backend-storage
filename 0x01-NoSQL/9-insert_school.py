#!/usr/bin/env python3
"""add data from dictionary to collection"""


def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
