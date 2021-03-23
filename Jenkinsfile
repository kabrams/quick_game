pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Hello World'
                sh 'ls'
            }
        }
    }
 }

    

