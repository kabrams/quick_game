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
                sh 'docker run -it --rm --name my-running-app -v /Users/kabrams/ken_projects/quick_game:/usr/src/app -w /usr/src/app my-python-app'
            }
        }
    }
 }

    

