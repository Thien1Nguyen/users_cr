# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
DATABASE = 'users_schema'
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for user in results:
                new_user = User(user)
                users.append( new_user)
        
        return users

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users(first_name, last_name, email) VALUE(%(first_name)s,%(last_name)s,%(email)s)"
        return connectToMySQL(DATABASE).query_db(query, data)