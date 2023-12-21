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
                    sh '''sudo rm -dfr /home/ajith/Documents/Learnings/Python_Learning/Flask_/* && sudo cp -r /var/lib/jenkins/workspace/FlaskAppPipeLine/. /home/ajith/Documents/Learnings/Python_Learning/Flask_/'''
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
