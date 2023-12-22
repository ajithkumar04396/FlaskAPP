pipeline{
    agent any
        stages{
            stage('Clone Repository...!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    checkout scm
                }
            }
            stage('Install Dependencies...!'){
                /*  Install the dependencies from requirements.txt */
                steps{
                    sh '''. venv/bin/activate && pip install -r requirements.txt'''
                   
                }
            }
            stage('Deploying...!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    sh ''' 
                    sudo chmod -R 777 /var/lib/jenkins/workspace/FlaskAppPipeLine'''
                }
            }
            stage('Restarting the server...!'){
                /*  cloning the repository to Jenkins workspace */
                steps{
                    sh ''' sudo service flaskApp restart '''
                }
            }
        }
}
