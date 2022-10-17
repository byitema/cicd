pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('Setup') {
            steps {
                sh 'apt-get install libpq-dev python-dev'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Pytest') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}