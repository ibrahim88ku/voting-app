pipeline {
  agent any
  stages {
    stage('Build Frontend') {
      steps {
        sh 'docker build -t voting-frontend ./frontend'
      }
    }
    stage('Build Backend') {
      steps {
        sh 'docker build -t voting-backend ./backend'
      }
    }
  }
}
