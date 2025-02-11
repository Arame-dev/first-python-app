pipeline{
    agent any
    
    environment{
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        DOCKER_IMAGE = 'aramedev/server:latest'
        EMAIL = 'aramemarutyan14@gmail.com'
    }

    stages{
        stage('Test'){
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
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                        sh """
                        docker build -t ${env.DOCKER_IMAGE} .
                        docker push ${env.DOCKER_IMAGE}
                        """
                    }
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
                    subject: "Jenkins Job: ${env.JOB_NAME} - ${currentBuild.result}",
                    body: """<p>Job details:</p>
                            <ul>
                              <li>Status: ${currentBuild.result}</li>
                              <br><hr>
                              <li>URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></li>
                            </ul>""",
                    mimeType: 'text/html'
                )
            }
        }
    }
}
