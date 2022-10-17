pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('python version check') {
            steps {
                sh 'python --version'
            }
        }
    }
}