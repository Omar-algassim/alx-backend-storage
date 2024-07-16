#!/usr/bin/env python3
"""update and add topic to the school document"""


def update_topics(mongo_collection, name, topics):
    """update and add topic to the school document"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
