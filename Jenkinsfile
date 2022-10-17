pipeline {
    agent {
        docker {
            image 'python:3.10.7-alpine'
            args '-u root:root'
        }
    }
    stages {
        stage('Setup') {
            steps {
                sh 'apk add libpq-dev python3-dev postgresql-dev gcc musl-dev'
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