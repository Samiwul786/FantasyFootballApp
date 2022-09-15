pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
		       
               sh "pip3 install -r requirements.txt"
                      
            }
        }
        stage('Test') {
            steps {
	       sh "python3 test_app.py"

               sh "python3 -m pytest --cov" 
            }
        }
	
}
}
    
     
    

