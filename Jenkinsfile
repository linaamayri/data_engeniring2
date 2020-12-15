pipeline {
  agent any
  stages {
    stage('Build Flask app') {
      steps {
        sh 'docker build -t docker-flask:latest .'
      }
    }

    stage('Run docker images') {
      steps {
        sh 'docker run -p 5000:5000 docker-flask:latest'
      }
    }
    
    stage('stop docker container') {
      steps {
        sh 'docker rm -f $(docker container ls -qa)'

      }
    }

  }
}
