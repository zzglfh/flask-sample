pipeline {
  agent any
  stages {
    stage('build') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        sh 'docker build -t "flaskr" .'
      }
    }
  }
}