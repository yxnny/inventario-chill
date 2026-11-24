
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Descargar codigo') {
            steps {
                checkout scm
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh '''
                    docker build -f Dockerfile.test \
                        -t inventario-chill-test:${BUILD_NUMBER} .
                    docker run --rm inventario-chill-test:${BUILD_NUMBER}
                '''
            }
        }

        stage('Construir imagen de la aplicacion') {
            steps {
                sh '''
                    docker build \
                        -t inventario-chill:${BUILD_NUMBER} .
                '''
            }
        }
    }
}
