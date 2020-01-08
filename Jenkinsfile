// def dockerHome = tool 'myDocker'
// How to implement this?
// environment {
//    def dockerHome = tool 'myDocker'
//   }

node {
    
    agent any 
    
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
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
