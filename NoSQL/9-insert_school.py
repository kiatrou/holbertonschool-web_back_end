#!/usr/bin/env python3
"""
A function that inserts a new document in a collection based on keyword arguments
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Args:
       mongo_collection: pymongo collection object
       **kwargs: keyword arguments that will become the document fields

   Returns:
       ObjectId: the _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
