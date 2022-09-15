pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
              sh pip install -r requirements.txt
              sh python app.py       
            }
        }
        stage('Test') {
            steps {
		sh python -m pytest --cov
                
            }
        }
    
        }
    }
}
