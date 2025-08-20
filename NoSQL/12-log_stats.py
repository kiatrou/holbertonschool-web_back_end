#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
"""
import pymongo


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB

    Connects to MongoDB and displays:
    - Total number of logs
    - Count of each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Count of GET requests to /status path
    """
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Get total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Display methods section
    print("Methods:")

    # List of methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count documents for each method
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count GET requests to /status
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
