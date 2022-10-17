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
                sh 'apk add --update --no-cache openssh'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Kubernetes') {
            steps {
                sshagent(['laptop']) {
                    sh 'ssh user@host.docker.internal minikube --version'
                }
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