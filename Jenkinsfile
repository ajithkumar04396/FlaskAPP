pipeline{
    agent any
        stages{
            stage('Clone Repository'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    checkout scm
                }
            }
            stage('Install Dependencies'){
                /*  Install the dependencies from requirements.txt */
                steps{
                    sh '''. venv/bin/activate && pip install -r requirements.txt'''
                   
                }
            }
            stage('Deploying and Restarting the service'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    sh '''service flaskApp restart'''
                }
            }
            stage('Deployment status'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    echo '''Deployement Complete..'''
                }
            }
        }
}
