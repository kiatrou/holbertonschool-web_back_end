#!/usr/bin/env python3
"""
This is a function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or empty list if no documents
    """
    documents = list(mongo_collection.find())
    return documents
