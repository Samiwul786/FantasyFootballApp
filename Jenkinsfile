pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
		sh "apt install python3-pip"	       
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
    

