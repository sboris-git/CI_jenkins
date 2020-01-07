#!groovy
def dockerHome = tool 'myDocker'
def env.PATH = "${dockerHome}/bin:${env.PATH}"

pipeline {
    
    agent any

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
