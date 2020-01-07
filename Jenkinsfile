pipeline {
   agent any

   stages {
      stage('Build') {
          agent any
          steps {
            // Get some code from a GitHub repository
            // sh 'cd /CH_096_TAQC/'
            git 'https://github.com/sboris-git/CI_jenkins.git'
        }
      }
      
      
      stage('Test') {
          agent { 
             docker {
                image  'node:7-alpine' 
                args  '-it'
                }
           }
           steps {
               sh 'node --version'
           }
       }
      
      
     
   }
}

// 'https://www.edureka.co/community/43657/use-a-docker-image-with-jenkins-declarative-pipeline'
