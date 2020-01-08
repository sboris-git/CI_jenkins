def dockerHome
// How to implement this?
// environment {
//    def dockerHome = tool 'myDocker'
//   }

pipeline {
    
    agent any 
    
    stages {
    
        stage('Initialize'){
            dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
        
        stage('Build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}
