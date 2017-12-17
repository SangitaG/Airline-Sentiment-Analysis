import pymongo

# This will change if the AWS instance is restarted.
mongo_IP = '35.163.170.219'
mongo_port = 27016

def mongoDB_create_collection(db_name, collection_name, collection_lst):
    '''
    Create and write a collection list to the mongo DB.
    Note: the host IP address is hard coded. If the AWS
    instance, were the DB resides is rebooted, this IP
    will need to be set again.
    '''
    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP,mongo_port)

    # Handle to  database
    db_ref = client[db_name]
    
    # If collection exists, remove it and rewrite it.
    if (collection_name in db_ref.collection_names()):
        db_ref[collection_name].remove()

    # Create a reference to a collection
    coll_ref = db_ref[collection_name]
        
    # Use the collection reference to insert the ML_page_contents
    for doc in tqdm(collection_lst):
        coll_ref.insert_one(doc)

def mongoDB_read_collection(db_name, collection_name):
    '''
    Read a collection from the mongo DB on AWS.
    Note: the host IP address is hard coded. If the AWS
    instance, were the DB resides is rebooted, this IP
    will need to be set again.
    '''  
    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP,mongo_port)

    # Make a new database
    db_ref = client[db_name]

    # Create a reference to my_collection
    coll_ref = db_ref[collection_name] 
    
    # Read collection into a list.
    coll_lst = list(coll_ref.find())
    
    return(coll_lst)

def mongoDB_read_unique_pages_collection(db_name, collection_name):
    '''
    This method returns a list with unique documents.
    ''' 
    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP,mongo_port)

    # Make a new database
    db_ref = client[db_name]

    # Create a reference to my_collection
    coll_ref = db_ref[collection_name] 
    
    
    # Read collection into a list.
    unique_pgeid_lst = coll_ref.distinct( "pageid" )
    
    # Read collection into a list.
    coll_lst = list(coll_ref.find())
    
    unique_pg_lst=[]
    for p_entry in coll_lst:
        if(len(unique_pgeid_lst) != 0):
            if p_entry['pageid'] in unique_pgeid_lst:
                unique_pg_lst.append(p_entry)
                unique_pgeid_lst.remove(p_entry['pageid'])
        else:
            break
    
    return(unique_pg_lst)
    
def mongoDB_get_DBnames(): 
    '''
    This method returns database names that exist on mongo server.
    '''
    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP , mongo_port)    
    
    # Databases on our MongoDB Server.
    names = client.database_names()
    
    return(names)

def mongoDB_get_collection_names(db_name):
    '''
    This method returns names of collections available on the mongo DB
    '''    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP,mongo_port)    
    
    # Make a new database
    db_ref = client[db_name]
    
    names = db_ref.collection_names()
    
    return(names)

def mongoDB_remove_collection(db_name, collection_name):
    db_ref[collec_name].drop()
    
def mongoDB_insert_collection_item(db_name, collection_name, item):
    
    # Instantiate client to our Mongo Server
    client = pymongo.MongoClient(mongo_IP,mongo_port)    
    
    # Make a new database
    db_ref = client[db_name]
    
    # Create a reference to my_collection
    coll_ref = db_ref[collection_name] 
    
    coll_ref.insert_one(item)
    
    
    