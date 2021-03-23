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
    }
 }

    

