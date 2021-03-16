pipeline {
    agent { dockerfile true }
     environment {
        PATH = "$PATH:/usr/local/bin"
    }
    stages {
        stage('Checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
 }

    

