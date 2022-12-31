1. Documentation
My app is a fanatsy football web app, that when someone adds a team, they can add players to that team. 

The flask app will be One-To-Many so will have One team that will have many players


Explantion of how the app works
The app coontains a table with teams which can be created from the home page. Once the team has been created, the user will have options to add players to the team once they click on that option. They can also delete the team and update the teams details. The user will be able to put in the details through the forms so the user will be able to see the team details to enter, and when the team has been created they can add players to the form by clicking on add players. This will specifically add players to the team row the user clicked on. 


Pipeline Documentation:
The pipeline only works for building and testing. The pipeline worked by adding a file called a Jenkinsfile. This file contains all the stages which has steps within the stage that contains shell commands to run the build and test stages.
Docker was used to dockerise the flask application. This was done thorugh the use of a Dockerfile that contained instructions to build the image. This is then used to run a container through the Azure VM cloud shell. Docker Swarm was used to build the nginx service. 

For future improvements i would beautify the application to make it more creative and more appealing to the audience



ERD Diagram link: 
https://1drv.ms/u/s!AtYvnpKjXPBuhOgLFkRUI1u-OOuF7g?e=70ab28

CI-CD Diagram
https://1drv.ms/u/s!AtYvnpKjXPBuhOgMULxodrkS0f9o_w?e=hyuUD7

Videos for evidence of working flask application
https://1drv.ms/u/s!AtYvnpKjXPBuhOgNYujuXFhaRVwxZw?e=9zKkn2




