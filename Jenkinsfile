pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "aadilmhusain/cyberbullying-detection"   // Change to your Docker Hub repository
    }

    stages {

	stage('Setup Permissions') {
            steps {
                script {
                    sh '''
            echo "Granting permissions to the Jenkins user.."
            sudo usermod -aG docker jenkins
            sudo mkdir -p /var/lib/jenkins/.ssh
            sudo chown -R jenkins:jenkins /var/lib/jenkins/.ssh
            sudo chmod 700 /var/lib/jenkins/.ssh
                  '''
                }
            }
        }	

        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git branch:'main', url:'https://github.com/AadilMdhusain/SPE-Project-MLOPs.git'
            }
        }

        stage('Docker Build') {
            steps {

                // Build Docker image
		sh 'ls -l'
		sh 'sudo docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials-id', 
                                                  usernameVariable: 'DOCKER_USERNAME', 
                                                  passwordVariable: 'DOCKER_PASSWORD')]){
		sh '''
                    echo "Logging in to Docker Hub..."
                    echo "${DOCKER_PASSWORD}" | sudo docker login -u "${DOCKER_USERNAME}" --password-stdin
                    sudo docker push ${DOCKER_IMAGE}
                    '''
		}
            }
        }

        stage('Start Minikube and Apply Kubernetes Resources') {
            steps {
                script {
                    // Starting Minikube if not already started
                    echo "Starting Minikube..."
                    sh 'minikube start --driver=docker'

                    // Applying Kubernetes resources (deployment, service, etc.)
                    echo "Applying Kubernetes resources..."
                    sh 'kubectl apply -f kubernetes/'
                }
            }
        }
	
	stage('Deploy to Kubernetes') {
          steps {
           script {
            echo "Deploying webapp to Kubernetes..."
            sh 'kubectl set image deployment/webapp-deployment webapp-container=${DOCKER_IMAGE}'
            }
         }
      }
        stage('Verify Deployment') {
            steps {
                script {
                    // Verifying the deployment on Kubernetes
                    echo "Verifying the Kubernetes deployments..."
                    sh 'kubectl get pods'
                    sh 'kubectl get services'
                }
            }
        }
    }


    }

    post {
        success {
            echo 'Build and push succeeded!'
        }
        failure {
            echo 'Build or push failed!'
        }
    }
}
