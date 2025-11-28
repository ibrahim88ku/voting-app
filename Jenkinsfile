pipeline {
    agent any

    environment {
        // dockerhub is a "Username with password" credential
        DOCKERHUB = credentials('dockerhub')

        // minikube-kubeconfig should be a "Secret file" credential
        // that contains your kubeconfig
        MINIKUBE_KUBECONFIG = credentials('minikube-kubeconfig')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/ibrahim88ku/voting-app.git'
            }
        }

        // TODO: enable SonarQube later with SonarScanner (not Maven)
        /*
        stage('SonarQube Scan') {
            steps {
                script {
                    withSonarQubeEnv('Sonar-Server') {
                        // This only works for Maven projects with pom.xml
                        // sh 'mvn clean verify sonar:sonar'
                    }
                }
            }
        }
        */

        stage('Build Docker Images') {
            steps {
                sh """
                docker build -t ${DOCKERHUB_USR}/vote-frontend:latest frontend/
                docker build -t ${DOCKERHUB_USR}/vote-backend:latest backend/
                """
            }
        }

        stage('Push Docker Images') {
            steps {
                sh """
                echo "${DOCKERHUB_PSW}" | docker login -u "${DOCKERHUB_USR}" --password-stdin
                docker push ${DOCKERHUB_USR}/vote-frontend:latest
                docker push ${DOCKERHUB_USR}/vote-backend:latest
                """
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh """
                kubectl --kubeconfig=${MINIKUBE_KUBECONFIG} apply -f k8s/staging/
                """
            }
        }

        stage('Manual Approval for Production') {
            steps {
                input "Deploy to Production?"
            }
        }

        stage('Deploy to Production') {
            steps {
                sh """
                kubectl --kubeconfig=${MINIKUBE_KUBECONFIG} apply -f k8s/production/
                """
            }
        }
    }
}
