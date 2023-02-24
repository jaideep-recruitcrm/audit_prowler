pipeline {
    agent any
    stages {
        stage('Upgrading pip') {
            steps {
                sh 'python3.10 -m pip install --upgrade pip'
            }
        }
        stage('Installing Prowler') {
            steps {
                sh 'python3.10 -m pip install prowler'
            }
        }
        stage('Cleaning Previous Results') {
            steps {
                sh 'rm -rf scan_result 2> /dev/null'
            }
        }
        stage('Running Prowler Script') {
            environment {
                AWS_ACCESS_KEY_ID = credentials("aws-access-key-id")
                AWS_SECRET_ACCESS_KEY = credentials("aws-secret-access-key")
            }
            steps {
                sh "export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}"
                sh "export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}"
                sh "python3.10 -m prowler aws -S -f ap-south-1 -C /tmp/checks_passing.json -o ./scan_result"
            }
        }
    }
}