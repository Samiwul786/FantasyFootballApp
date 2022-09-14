pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                python app.py
            }
        }
        stage('Test') {
            steps {
                python -m pytest --cov
                python -m pytest --cov=test_app
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}
