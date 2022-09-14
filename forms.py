from flask_wtf import FlaskForm       
from wtforms import StringField, SubmitField, SelectField, IntegerField

class TeamForm(FlaskForm):  
        team_name = StringField('Team Name: ')
        league_name = StringField('League Name: ')
        sponsor_name = StringField('Sponsor Name: ')
        submit = SubmitField('Add Team')
        
class PlayerForm(FlaskForm):
        player_name = StringField('Player Name: ')
        position = SelectField('Player Position:', choices=[('goalkeeper', 'GoalKeeper'), ('defender', 'Defender'), ('midfield','Midfield'), ('striker', 'Striker')])
        submit = SubmitField('Add Player') 
        
class UpdateTeamForm(FlaskForm):
        team_name = StringField('Team Name: ')
        league_name = StringField('League Name: ')
        sponsor_name = StringField('Sponsor Name: ')
        submit = SubmitField('Update Team Details')        
                
