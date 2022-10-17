pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'apk add libpq-dev python3-dev postgresql-dev gcc musl-dev'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Linters') {
            steps {
                sh 'python -m black app/ --diff'
                sh 'python -m flake8 app/'
                sh 'python -m mypy app/'
            }
        }

        stage('Pytest') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}