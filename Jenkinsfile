#!groovy

def dockerHome = tool 'myDocker'
// How to implement this?
// environment {
//    def dockerHome = tool 'myDocker'
//   }

pipeline {
    
    agent any 
    
    environment {
        env.PATH = "${dockerHome}/bin:${env.PATH}" 
    }
    
    stages { 
        
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
