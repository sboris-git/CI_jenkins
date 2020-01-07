#!groovy
def dockerHome = tool 'myDocker'
env.PATH = "${dockerHome}/bin:${env.PATH}"

pipeline {
    
    agent any

    stages {

        stage('Initialize'){
            steps{
                 script {
                    echo 'script'
                }
            }
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
