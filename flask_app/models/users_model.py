from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

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
                new_user = cls(user)
                users.append( new_user)
        
        return users

    @classmethod
    def get_one(cls,id):

        data = {
            "id" : id
        }

        query = """

            SELECT * FROM users
            WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)

        user = cls(results[0])

        return user
    
    @classmethod
    def get_newest_user(cls):

        query = """

            SELECT * FROM users
            ORDER BY id DESC
            LIMIT 1;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        return results[0]#['id']
        

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users(first_name, last_name, email) VALUE(%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data);

    @classmethod
    def update(cls, data):

        query = """
            UPDATE users
            SET
            first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s
            WHERE id = %(id)s;
        """
        print("I sent it!")
        return connectToMySQL(DATABASE).query_db(query, data);
    
    @classmethod
    def delete_user(cls, id):

        data = {
            "id" : id,
        }

        query = """

            DELETE FROM users
            WHERE id = %(id)s;

        """

        connectToMySQL(DATABASE).query_db(query, data);