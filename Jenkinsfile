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
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "python3.10 -m prowler aws -S -f ap-south-1 -C /tmp/checks_gdpr_aws.json -o ./scan_result"
                }
            }
        }
        stage('Sending to slack') {
            steps {
                sh 'zip -r scan_result.zip scan_result/'
                sh 'mv scan_result.zip /tmp/'
                sh 'python3.10 -m pip install slack-sdk'
                sh 'python3.10 /tmp/send_slack_message.py'
                sh 'rm -rf /tmp/scan_result.zip'
            }
        }
    }
}