











#bulk inserts
new_posts = [{
            "author": "Mike",
            "text": "Another post",
            "Tags": ["bulk", "post", "insert"],
            "date": datetime.datetime.utcnow()}
             {
             "author": "Joao",
            "text": Post from Joao. New post available",
            "Title": "Mongo is fun",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]
            
        
result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nRecuperação final")
pprint.pprint(db.posts.find_one({"author": "Joao"}))