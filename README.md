# nyctaxiserver
 
 # Description
  A python (flask-restplus) based Web API for returning statistics related to trips made by new york taxis based on Google BigQuery Data

## Steps to run
### All commands may require sudo/admin privileges
1. *Python 3+* should be installed on the system (the code has been verified on *Python 3.5.2*)


2. **Google Service Account Configuration** : In case you need to use your own google service account (and not the default which I have provided) follow the below steps else go to Step 3.

    a. Login to your google account and follow the steps mentioned at [https://support.google.com/a/answer/7378726?hl=en](https://support.google.com/a/answer/7378726?hl=e).  It will download your service account key information as a  ```.json``` file to your machine
    
    b. Replace the contents of the file ```bqconfig.json``` file present at location ```test@testmachine:~/test/repodir/nyctaxiserver/app/configuration/``` with the contents of ```.json``` file that was downloaded to your machine in previous Step (i.e. 2a)

    c. Open ```bqconfig.json``` and copy the value for the key  ```"project_id"```. For example in case your ```bqconfig.json``` contents look like below you need to copy `"ABC123"`.  Close the file ```bqconfig.json``` 

            {
                "type": "service_account",
                "project_id": "ABC:123",
                ...

    d. Open ```dbonfig.py``` present at location ```test@testmachine:~/test/repodir/nyctaxiserver/app/configuration/``` and set the value of the variable **SVC_ACCNT_PROJECT_NAME** to the value copied in prevous Step 2c. (i.e `"ABC:123"` as based on above example) . Below is an illustration on how the file 
    ```dbonfig.py``` should look after changes. Save and close ```dbconfig.py``` after making changes.


            import os
            configdir = os.path.abspath(os.path.dirname(__file__))

            SVC_ACCNT_PROJECT_NAME = "ABC:123"



3. **Project Configurations** : You may configure following items are per your conbenience (the project should work with default configurations also if no port conflicts are there)
    
    a. **Port Number** : In case you do not want to use the default port number, open the file ```config.py``` at location ```test@testmachine:~/test/repodir/nyctaxiserver/app/configuration/``` and set the value of the variable **PORT** to the value to the values you desire. Foe example if you want to use the port number 9000 the file ```config.py``` should look like below.  Save and close the file ```config.py``` after making changes.

        import  os
        configdir = os.path.abspath(os.path.dirname(__file__))
        class BaseConfig(object):
            """A class used to store coniguration properties common across all environments"""
            DEBUG = True
            TESTING = False
            PORT = '9000'

                           
    a. **Cache** : In case you do enable caching, open the file ```dbconfig.py``` at location ```test@testmachine:~/test/repodir/nyctaxiserver/app/configuration/``` and set the value of the key variable **caching_enabled** to **True** (present in the dictionary **API_CONFIG**). You may enable caching for a particular API endpoints only (which should supports caching). For example in the below snapshot of file ```dbconfig.py``` caching is enabled for `total_trips` endpoint but not for `avg_speed24h` endpoint. Save and close `the file ```dbconfig.py``` after making changes.


        API_CONFIG = {
               
               'total_trips' : {
                                'bq_key':'bqconfig', 
                                ....
                                'caching_enabled' : True,
                                ....
                               },

               'avg_speed24h' : {
                                'bq_key':'bqconfig', 
                                ....
                                'caching_enabled' : False,
                                ... 
                                },
                    }         
     



4. **Virtual Environment Setup** : (Required Only Once. If setup has been completed earlier, please go to Step 5)

    a.   Setup the environment using following commands from bash shell (or command line on windows). You will need navigate (*cd*) to the folder *nyctaxiserver*( the one that contains the file *README.md* and folder *app* ) and then run commands to install and activate the virtual environment in which the API server would run.

            -- Linux:   
                
                test@testmachine:~/test/repodir$ cd nyctaxiserver
                test@testmachine:~/test/repodir/nyctaxiserver$ source envsetup.sh
                (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python runserver.py
                        
            -- Windows: 

                C:/../testdir/<TBD>

    b. (Optional) In case there are isses with running above file you may *install/configure* a virtual environment by running commands from bash shell (or command line as)as follows
            
            -- Linux 
                
                test@testmachine:~/test/repodir$ cd nyctaxiserver
                test@testmachine:~/test/repodir/nyctaxiserver$ python3 -m pip install --user virtualenv
                test@testmachine:~/test/repodir/nyctaxiserver$ python3 -m virtualenv venvtaxiapi
                test@testmachine:~/test/repodir/nyctaxiserver$ source venvtaxiapi/bin/activate
                (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python -m pip install -r requirements.txt
                (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python runserver.py

            -- Windows:
        
    In case this step is successfull you should see the server running at ['http://localhost:5000/']('http://localhost:5000/') (port number may differ if you changed it in Step 3)
        
 

5. **Use this step if conifguration (Step 2) and environment (Step 3) has already been setup and you want to start the API Server. You may ggnore this step if coming from Step 3. as Step 3. should have already started the Server** 

    Navigate (*cd*) to the folder *nyctaxiserver* folder and run the following commands to run the API server

        -- Linux:   
            
            test@testmachine:~/test/repodir$ cd nyctaxiserver
            test@testmachine:~/test/repodir/nyctaxiserver$ source venvtaxiapi/bin/activate/
            (venvtaxiapi) test@testmachine:~/testdir/repodir$ python runserver.py
                    
        -- Windows  : 

            C:/../testdir...

    In case this step is successfull you should see the server running at ['http://localhost:5000/']('http://localhost:5000/') (port number may differ if you changed it in Step 3)



6. **Runing Tests**  : In order to execute the testcases run the following command from shell. Before this please make sure to perform Step 2 (configuration) and Step 3 (Virtual Envirobment Set up) if not done already.

        -- Linux:   
            
            test@testmachine:~/test/repodir$ cd nyctaxiserver
            test@testmachine:~/test/repodir/nyctaxiserver$ source venvtaxiapi/bin/activate/
            (venvtaxiapi) test@testmachine:~/testdir/repodir$ pytest
                    
        -- Windows  : 

            C:/../testdir...

5. Logs ...<TBC>