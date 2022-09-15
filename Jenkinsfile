pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
               pip install -r requirements.txt
               python app.py       
            }
        }
        stage('Test') {
            steps {
	       python -m pytest --cov

                
            }
        }
    
        }
    }

