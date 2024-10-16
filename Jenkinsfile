pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/Swapnilbarsagade/webhookpublic.git'
            }
        }

        stage('Build') {
            steps {
                // Commands to build your project, for example for a Java project:
                // sh 'mvn clean install'
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                // Commands to run tests, e.g., for a Java project:
                // sh 'mvn test'
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy or package steps can be added here
                echo 'Deploying the project...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up after the build if needed
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
