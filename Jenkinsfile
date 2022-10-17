pipeline {
    agent {
        docker {
            image 'python:3.10.7-alpine'
            args '--add-host host.docker.internal:host-gateway -u root:root'
        }
    }

    stages {

        stage('Kubernetes') {
            steps {
                sh 'apk add --update --no-cache openssh'
                sshagent(['laptop']) {
                    sh 'ssh -o StrictHostKeyChecking=no user@host.docker.internal minikube --version'
                }
            }
        }

        stage('Setup') {
            steps {
                sh 'apk add libpq-dev python3-dev postgresql-dev gcc musl-dev'
                sh 'apk add --update --no-cache openssh'
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