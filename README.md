# nyctaxiserver
 
 # Description
 A python based Web API for returning statistics related to trips made by new york taxis based on Google BigQuery Data

## Steps to run
### All commands may require sudo/admin privileges
1. *Python 3+* should be installed on the system (the code has been verified on *Python 3.5.2*)

2. **Setup : Perform Only Once. If setup has been completed earlier, please go to Step 3**

    a. Setup the environment using following commands from bash shell (or command line on windows). You will need navigate (*cd*) to the folder *nyctaxiserver*( the one that contains the file *README.md* and folder *app* ) and then run commands to install and activate the virtual environment in which the API server would run.
 
        -- Linux:   
            
            test@testmachine:~/test/repodir$ cd nyctaxiserver
            test@testmachine:~/test/repodir/nyctaxiserver$ source envsetup.sh
            (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python run.py
                    
        -- Windows: 

            C:/../testdir/<TBD>

    

   b. In case there are isses with running above file you may *install/configure* a virtual environment as follows
    
        -- Linux 
            
            test@testmachine:~/test/repodir$ cd nyctaxiserver
            test@testmachine:~/test/repodir/nyctaxiserver$ python3 -m pip install --user virtualenv
            test@testmachine:~/test/repodir/nyctaxiserver$ python3 -m virtualenv venvtaxiapi
            test@testmachine:~/test/repodir/nyctaxiserver$ source venvtaxiapi/bin/activate
            (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python -m pip install -r requirements.txt
            (venvtaxiapi) test@testmachine:~/test/repodir/nyctaxiserver$ python run.py

        -- Windows:
            

 

3. **Use this step if environment has already been setup and you want to start the API Server. Ignore this step if coming from Step 2.** 

    Navigate (*cd*) to the folder *nyctaxiserver* folder and run the following commands to run the API server

        -- Linux:   
            
            test@testmachine:~/test/repodir$ cd nyctaxiserver
            test@testmachine:~/test/repodir/nyctaxiserver$ source venvtaxiapi/bin/activate/
            (venvtaxiapi) test@testmachine:~/testdir/repodir$ python run.py
                    
        -- Windows  : 

            C:/../testdir...

4. TBC ...