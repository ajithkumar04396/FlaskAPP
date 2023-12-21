pipeline{
    agent any
        stages{
            stage('Clone Repository'){
                /*  cloning the repository to jenkins workspace */
                steps{
                    checkout scm
                }
            }
            stage('Install Dependencies'){
                /*  Install the dependencies from requirements.txt */
                steps{
                    sh 'sudo source /var/lib/jenkins/workspace/FlaskApp/venv/bin/activate'
                    sh 'pip install -r /var/lib/jenkins/workspace/FlaskApp/requirements.txt'
                    sh 'deactivate'
                }
            }
            stage('Deploying and Restarting the service'){
                /*  cloning the repository to jenkins workspace */
                steps{
                    sh 'sudo service flaskApp restart'
                }
            }
            stage('Deployment status'){
                /*  cloning the repository to jenkins workspace */
                steps{
                    echo 'Deployement Complete..'
                }
            }
        }
}