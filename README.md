# FlaskAPP
This is a basic flask App with Redis for performing CICD pipeline using Jenkins

**Deployment-**<br>
&ensp;&ensp;_-systemd.service in Ubuntu_<br>
&ensp;&ensp;_-Docker_<br>


**system.service**<br>
If you are deploying your App as system.service:<br>
&ensp;&ensp;_-create a service file in "/etc/systemd/system/"_

      cd /etc/systemd/system/

&ensp;&ensp; _-use nano editor create and configure your service file_

      nano APPNAME.service

&ensp;&ensp; _-replace APPNAME with your application service name._

      [Unit]
      #  specifies metadata and dependencies
      Description=uWSGI instance to serve Flask App
      #After=network.target
      After=syslog.target
      # tells the init system to only start this after the networking target has been reached
      # We will give our regular user account ownership of the process since it owns all of the relevant files
      [Service]
      # Service specify the user and group under which our process will run.
      User=jenkins
      # give group ownership to the www-data group so that Nginx can communicate easily with the uWSGI processes.
      Group=www-data
      # We'll then map out the working directory and set the PATH environmental variable so that the init system knows where our the executables for the process are located (within our v>
      WorkingDirectory=/var/lib/jenkins/workspace/FlaskApp # replace your jenkins workspace path
      Environment="PATH=/FlaskAPP/venv/bin" # replace your python environment
      # We'll then specify the commanded to start the service
      ExecStart=/FlaskAPP/venv/bin/uwsgi --http 127.0.0.1:8000 --master --enable-threads -p 2 -w wsgi:app
      SuccessExitStatus=143
      TimeoutStopSec=20
      Restart=on-failure
      RestartSec=5
      # This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running:
      [Install]
      WantedBy=multi-user.target

&ensp;&ensp;_-make sure all the libraries required for the project is installed in the configured python environment_

    source /FlaskApp/venv/bin/activate && pip install -r /var/lib/jenkins/workspace/FlaskApp/requirements.txt


    
      

  
  
