#!/usr/bin/env python3
"""
Module for updating MongoDB documents
"""
import pymongo


def update_topics(mongo_collection, name, topics):
   """
   Changes all topics of a school document based on the name

   Args:
       mongo_collection: pymongo collection object
       name (str): the school name to update
       topics (list of str): the list of topics approached in the school

   Returns:
       None

   Example:
       >>> collection = db.schools
       >>> update_topics(collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
       >>> # Updates the document where name="Holberton school" 
       >>> # Sets topics field to ["Sys admin", "AI", "Algorithm"]
   """
   mongo_collection.update_many(
       {"name": name},
       {"$set": {"topics": topics}}
   )
