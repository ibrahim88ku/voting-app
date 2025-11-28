pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/ibrahim88ku/voting-app.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    withSonarQubeEnv('Sonar-Server') {
                        sh 'mvn clean verify sonar:sonar'
                    }
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t youruser/vote-frontend:latest frontend/
                docker build -t youruser/vote-backend:latest backend/
                '''
            }
        }

        stage('Push Docker Images') {
            steps {
                sh '''
                echo "$DOCKERHUB_PSW" | docker login -u "$DOCKERHUB_USR" --password-stdin
                docker push youruser/vote-frontend:latest
                docker push youruser/vote-backend:latest
                '''
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                kubectl --kubeconfig=/var/lib/jenkins/kubeconfigs/minikube apply -f k8s/staging/
                '''
            }
        }

        stage('Manual Approval for Production') {
            steps {
                input "Deploy to Production?"
            }
        }

        stage('Deploy to Production') {
            steps {
                sh '''
                kubectl --kubeconfig=/var/lib/jenkins/kubeconfigs/minikube apply -f k8s/production/
                '''
            }
        }
    }
}
