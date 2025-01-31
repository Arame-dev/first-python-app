pipeline{
    agent any
    
    environment{
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        DOCKER_IMAGE = 'aramedev/server:latest'
        EMAIL = 'aramemarutyan14@gmail.com'
    }

    stages{
        stage('Test'){
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                checkout scm
                sh 'python --version'
                sh 'python ./Encrypting.py'
            }
        }

        stage('Build & Push to DockerHub') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub-creds', url: 'https://registry.hub.docker.com'){
                    sh """
                        docker build -t ${env.DOCKER_IMAGE} .
                        docker push ${env.DOCKER_IMAGE}
                    """
                }
            }
        }
    }

    post{
        always{
            script{
                def status = currentBuild.result ?: 'SUCCESS'
                emailext (
                    to: "${env.EMAIL}",
                    subject: "Jenkins Job: ${env.JOB_NAME} - ${status}",
                    body: "Job ${env.JOB_NAME} with build number ${env.BUILD_NUMBER} finished with status: ${status}. Link - ${env.BUILD_URL}.",
                )
            }
        }
    }
}
}
