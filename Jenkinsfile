#!/usr/bin/env groovy
import hudson.model.*

def dockerHome = tool 'myDocker'
// How to implement this?
// environment {
//    def dockerHome = tool 'myDocker'
//   }

pipeline {
    
    agent any 
    
    environment {
        PATH = "${dockerHome}/bin:${PATH}" 
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
