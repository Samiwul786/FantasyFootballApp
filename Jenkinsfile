pipeline {
    agent {
	docker { image 'python:3' }
}
    stages {
        stage('Build') {
            steps {
	       sh "sudo apt-get install python3-pip"
               sh "pip3 install -r requirements.txt"
               sh "python3 app.py"       
            }
        }
        stage('Test') {
            steps {
	       sh "python3 -m pytest --cov"

                
            }
        }
    
        }
    }

