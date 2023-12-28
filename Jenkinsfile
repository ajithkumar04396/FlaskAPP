pipeline{
    agent any
        stages{
            stage('Clone Repository...!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    checkout scm
                }
            }
            stage('Add Permission...!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    sh ''' 
                    sudo chmod -R 777 /var/lib/jenkins/workspace/FlaskAppPipeLineDocker'''
                }
            }
            stage('Build && Deploya using Docker!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    sh '''. sudo docker compose up -d'''
                }
            }
        }
}
