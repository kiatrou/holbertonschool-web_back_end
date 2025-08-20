#!/usr/bin/env python3
"""
Module for querying MongoDB documents by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
   """
   Returns the list of schools having a specific topic

   Args:
       mongo_collection: pymongo collection object
       topic (str): the topic to search for

   Returns:
       list: list of school documents that have the specified topic

   Example:
       >>> collection = db.schools
       >>> schools = schools_by_topic(collection, "Python")
       >>> print(schools)
       [
           {"name": "Holberton school", "topics": ["Python", "C", "Javascript"]},
           {"name": "UCSF", "topics": ["Python", "Biology"]}
       ]
   """
   schools = list(mongo_collection.find({"topics": topic}))
   return schools
