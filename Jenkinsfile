pipeline {
    agent { dockerfile true }
     environment {
        PATH = "$PATH:/usr/local/bin"
        sh = "$PATH:/bin/sh"
    }
    stages {
        stage('Checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Test') {
            steps {
                sh 'docker build -t node .'
                sh 'docker run -it --name test_app_py node'
            }
        }
    }
 }

    

