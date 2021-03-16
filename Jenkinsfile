pipeline {
    agent { dockerfile true }
    stages {
        stage('Initialize'){
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
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

    

