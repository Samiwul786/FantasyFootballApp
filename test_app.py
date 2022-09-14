from flask import url_for
from flask_testing import TestCase

from app import app, db, Teams, Players


# Create the base class
class TestBase(TestCase):
    
    def create_app(self):
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='TEST_SECRET_KEY',
                          Debug=True,
                          WTF_CSRF_ENABLED=False)
        return app
    
    def setUp(self):
        
        #Create the table
        db.create_all()
        
        # testing the one-to-many relationship
        team_test_sample = Teams(id=1, team_name="Manchester City", league_name="Premier League", sponsor_name="OKX")
        
        # The team_id argument might not work
        player_test_sample = Players(id=1, player_name="David Silva", position="midfileder", team_id=team_test_sample) 
        
        
        # save team to the in memory database
        db.session.add(team_test_sample)
        
        #save player to the in memory database
        db.session.add(player_test_sample)
        
        # will be called after every test
        def tearDown(self):
            
            # Close the database session and remove all contents of the test_app.data.db file
            db.session.remove()
            db.drop_all()
            
# Write a test class for adding a team to the database
class TestAdd(TestBase):
    
    def test_add_team(self):
        
        # add a new team to the database
        response = self.client.post(
            url_for('teams'),
            data = dict(team_name="Chelsea", league_name="Premier League", sponsor_name="Three"),
            follow_redirects = True       
        )
        
        assert Teams.query.filter_by(id=2)

            
# Write a test class to test the Read functionality        
class TestViews(TestBase):
        
    # Check this method    
    def test_home_get(self):
        
        response = self.client.get(url_for('home'))
       # print("This is the ++++++++++++++++++______", response.data)
        self.assertEqual(response.status_code, 200)
        
        self.assertIn(b'Fantasy Football Team Web App', response.data)





# #Write a test class for deleting a team from the database
# class TestDelete(TestBase):
    
#     def test_delete_team(self):
        
#         # delete Manchester City from the database
        
#         response = self.client.delete(
#             url_for('delete_team', id=2),
#             data = dict(id=2),
#             follow_redirects = True
#         )
        
#         print("This is the ++++++++++++______________***", response)
        
#         # query the teams table - if "chelsea" team is deleted
#         # the query should return an empty list
#         assert len(Teams.query.all()) == 1

            