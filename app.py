
from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm    
from forms import TeamForm, PlayerForm,UpdateTeamForm
    

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SECRET_KEY'] = 'this is a secret key'

db = SQLAlchemy(app)

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(255),  nullable=False)
    league_name = db.Column(db.String(255), nullable=False)
    sponsor_name = db.Column(db.String(255), nullable=False)
    players = db.relationship('Players', backref='players')
    
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(50), nullable=False) # make this field a selection field
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    
    
    
    

@app.route('/home')
def home():
    message = ""
    form = TeamForm()
    
    if request.method == 'POST':
        team_name = form.team_name.data
        league_name = form.league_name.data
        sponsor_name = form.sponsor_name.data
        
      
        
        if len(team_name) == 0 or len(league_name) == 0 or len(sponsor_name) == 0:
            message = "Please fill in all fields"
        else:
            team = Teams(team_name,  league_name, sponsor_name)
            db.session.add(team)
            db.session.commit()
            message = f"Thank you, {team_name} {league_name} {sponsor_name}"
                
    return render_template('home.html', form=form, message=message) # make this a method called create a team with players       

@app.route('/createteam', methods=['GET' ,'POST'])
def create_team():
    message = ""
    form = TeamForm()
    
    if request.method == 'POST':
        team_name = form.team_name.data
        league_name = form.league_name.data
        sponsor_name = form.sponsor_name.data
        
        
        if len(team_name) == 0 or len(league_name) == 0 or len(sponsor_name) == 0:
            message = "Please supply all fields"
        else:
            # Do the databse stuff here like Teams(team_name, league_name,sponsor_name)
            #team = Teams(team_name, league_name,sponsor_name)
            message = f"Thank you, {team_name} {league_name} {sponsor_name}"
            
    return render_template('createteam.html', form=form, message=message)                


@app.route('/createplayer', methods=['GET' ,'POST'])
def create_player():
    message = ""
    form = PlayerForm()
    
    if request.method == 'POST':
        player_name = form.player_name.data
        position = form.position.data
        team_id = form.team_id.data

        
        if len(player_name) == 0 or len(position) == 0:
            message = "Please supply all fields"
        else:
            # Do the databse stuff here like Players(player_name, position, the team id)
            # player = Players(player_name, position, team_id)
            message = f"Thank you, {player_name} {position} {team_id} "
            
    return render_template('createplayer.html', form=form, message=message)                


@app.route('/', methods=['GET' ,'POST'])
@app.route('/teams', methods=['GET', 'POST'])
def teams():
    data = Teams.query.all()
    
    message = ""
    form = TeamForm()
    
    if request.method == 'POST':
        new_team_name = form.team_name.data
        new_league_name = form.league_name.data
        new_sponsor_name = form.sponsor_name.data
        
      
        
        if len(new_team_name) == 0 or len(new_league_name) == 0 or len(new_sponsor_name) == 0:
            message = "Please fill in all fields"
        else:
            new_team = Teams(team_name=new_team_name,  league_name=new_league_name, sponsor_name=new_sponsor_name)
            db.session.add(new_team)
            db.session.commit()
            message = f"Thank you, Your team was successfully created {new_team_name} | {new_league_name}  | {new_sponsor_name}"
            return redirect('/')
                
    
    return render_template('teams.html', content=data, form=form, message=message) 


@app.route('/team/<int:x>/players', methods=['GET', 'POST'])
def players(x):
    
    
    team = Teams.query.get(x)# this will get a specific team
    data = Players.query.filter_by(team_id=x) # this will get a specific player from a team
    
    team_new_id = team.id
    
    message = ""
    form = PlayerForm()
    
    if request.method == 'POST':
        new_player_name = form.player_name.data
        new_position = str(form.position.data)
        
        
        if len(new_player_name) == 0:
            message = "Please enter in all fields"
        else:
            new_player = Players(player_name=new_player_name, position=new_position, team_id=team_new_id)    
            db.session.add(new_player)
            db.session.commit()
            message = f"Thank you, Your team was successfully created {new_player_name} | {new_position}"
            
    # Where do i need to put the form parameter e.g. form=form           
    return render_template('players.html', message=message,form=form, content=data, team=team)


 #Check this function       
@app.route('/deleteteam/<int:id>', methods=['GET', 'POST'])
def delete_team(id):
    team_to_delete = Teams.query.get_or_404(id)
    
    db.session.delete(team_to_delete)
    db.session.commit()
    return redirect('/')
    

@app.route('/updateteam/<int:id>', methods=['GET','POST'])
def update_team(id):
    
    team = Teams.query.get_or_404(id)
    
    message = ""
    form = UpdateTeamForm()
    
    if request.method == 'POST':
        new_team_name = form.team_name.data
        new_league_name = form.league_name.data
        new_sponsor_name = form.sponsor_name.data
        
      
        
        if len(new_team_name) == 0 or len(new_league_name) == 0 or len(new_sponsor_name) == 0:
            message = "Please fill in all fields"
        else:
           # new_team = Teams(team_name=new_team_name,  league_name=new_league_name, sponsor_name=new_sponsor_name)
          #  db.session.add(new_team)
            team.team_name = new_team_name
            team.league_name = new_league_name
            team.sponsor_name = new_sponsor_name
            db.session.commit()
            message = f"Thank you, Your team was successfully created {new_team_name} | {new_league_name}  | {new_sponsor_name}"
            return redirect('/')
                
    
    return render_template('updateTeams.html', form=form, message=message, team=team) 


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, host="0.0.0.0")




