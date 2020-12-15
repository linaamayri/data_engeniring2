pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker build -t docker-flask:latest .'
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Flask App'){
          steps{
            sh 'docker run -p 5000:5000 docker-flask:latest'
          }
        }
      }
    }
   
  }
}
