# FLLM CLI

## Getting started

- Install the FLLM CLI using the following:

    ```python
    pip install fllm-cli==1.0.0b5
    pip install fllm-cli-core==1.0.0b5
    ```

- Install the FLLM extension

    ```PowerShell
    fllm extension list
    fllm extension remove --name fllm-cli-extension
    fllm extension add --name fllm
    ```

- Login to Azure Cloud (this is necessary to get a user context)

    ```powershell
    fllm cloud set --name AzureCloud
    fllm login
    ```

- Create a new FLLM cloud (one for each FLLM instance you have, ex. DEV, PROD, STAGE, TEST)

    - Record your mgmt api uri for the target env
    - Find your `tenantId`, `clientId` and `resourceId` in the `Microsoft Entra` Azure Portal.  The clientId is the id of the `FoundataionaLLM.ManagementClient` application and the resourceId is the id of the `FoundataionaLLm.Management` application.  The instance id can be found in your Application Config instance under the `FoundationaLLM:Instance:Id` key in the Azure Portal:

        ```powershell
        #mgmt api tenant id
		$tenantId = "d280491c-b27a-41bf-9623-21b60cf430b3"
		#mgmt api client id
		$clientId = "aa5cba99-e753-4d91-b2f8-85a6b650d022"
		#mgmt api client resource id 
		$resourceId = "dc4b7d98-e404-4044-8040-4c7a5551e862"
		#mgmt api scope
		$scope = "$resourceId/.default"
        #FLLM instance id
        $instanceId = "1e22cd2a-7b81-4160-b79f-f6443e3a6ac2"
        ```

	- Register a new FLLM Cloud. Set the `endpoint-resource-manager` to the Management API endpoint (ex `https://localhost:63267`):

        ```powershell
        $cloud_name = "FllmCloud"
        fllm cloud unregister --name $cloud_name
        fllm cloud register --name $cloud_name --endpoint-resource-manager "https://localhost:63267" --endpoint-active-directory "https://login.microsoftonline.com" --endpoint-active-directory-resource-id "https://management.core.windows.net/" --endpoint-active-directory-graph-resource-id "https://graph.windows.net/" --client-id $clientId --instance-id $instanceId --management-client-id $resourceId
        fllm cloud set --name $cloud_name
        ```

	- Login to your instance by finding your `tenantId`, `clientId` and `resourceId`.  All three values are found in the `Microsoft Entra` Azure Portal.  The clientId is the id of the `FoundataionaLLM.ManagementClient` application and the resourceId is the id of the `FoundataionaLLm.Management` application:

        ```powershell
		fllm login -t $tenantId -c $clientId -r $resourceId --scope $scope
        ```

	- Test your FLLM CLI cloud:

    	```PowerShell
        fllm agent list --instance-id $instanceId
        fllm prompt list --instance-id $instanceId
        fllm vectorization contentsourceprofile list --instance-id $instanceId
        fllm vectorization textpartitioningprofile list --instance-id $instanceId
        fllm vectorization textembeddingprofile list --instance-id $instanceId
        fllm vectorization indexingprofile list --instance-id $instanceId
        fllm vectorization vectorizationrequest list --instance-id $instanceId
        ```

### If using Fiddler or localhost FLLM environment, set the following environment variables

        ```cmd
        PYTHONHTTPSVERIFY = "0"
        HTTP_PROXY = "http://127.0.0.0:8888"
        HTTPS_PROXY = "http://127.0.0.0:8888"
        ```

	- Export the fiddler Root certificate using Fiddler application
	- Encode it:
    	```powershell
    	certutil -encode FiddlerRoot.cer FiddlerRoot.pem
        ```

	- Set the path to the PEM

        ```cmd
        REQUESTS_CA_BUNDLE = "C:/Users/given/OneDrive/Desktop/FiddlerRoot.pem",
        ```

	- If running the Mgmt API locally, export the web app/visual studio SSL cert
	    - Open the web application in browser
	    - Click the browser security icon
	    - Select to download the PEM cert
	    - Add to the FiddlerRoot.pem file you generated previously (or on its own)

## FLLM Development Setup

- Clone the following to c:\github\solliancenet:
    - https://github.com/solliancenet/fllm-cli
    - https://github.com/solliancenet/fllm-rest-api-specs
    - https://github.com/solliancenet/fllm-cli-extensions
    - https://github.com/solliancenet/fllm-cli-core
    - https://github.com/solliancenet/fllm-aaz-dev-tools

- Clone the FLLM repo:
    - https://github.com/solliancenet/foundationallm
- Run the FLLM project (specifically the Management API)
- Browse to the Mgmt API and the `/swagger` endpoint, select the link to view the swagger file
- Copy the swagger file contents to the following folders:
    - C:\github\solliancenet\fllm-rest-api-specs\specification\fllm\resource-manager\FoundationLL.* folders
    - Agent
    - Configuration
    - Prompt
    - Vectorization
- Remove the /status* endpoints from each

- Run the fllm-aaz-dev-tools (two projects - web/api)
- Open Visual Studio code to the main folders
    - Update the "aaz-dev-tools" debug configuration file paths
    - Run the "aaz-dev-tools" debug configuration

- Open a new terminal window
- Run the following:
    ```cmd
    cd src/web/ 
    npm start
    ```
        
- Create new workspaces

    - FLLM-Agent
        - Plane = FLLM-Plane
        - Module = FLLM
        - Resource Provider = "FoundationaLLM.Agent"

    - Select all the endpoints
    - Select Submit
    - Select Export, confirm the dialog

    - FLLM-Configuration
        - Plane = FLLM-Plane
        - Module = FLLM
        - Resource Provider = "FoundationaLLM.Configuration"

    - FLLM-Prompt
        - Plane = FLLM-Plane
        - Module = FLLM
        - Resource Provider = "FoundationaLLM.Prompt"

    - FLLM-Vectorization
        - Plane = FLLM-Plane
        - Module = FLLM
        - Resource Provider = "FoundationaLLM.Vectorization"

- Generate CLI code
    - Go to the main page of the web app
    - Select **CLI**
    - Select the **Azure CLI Extension Module** option
    - Select the **FLLM** module
    - Select all the appropriate endpoints
        - agent
        - configuration
        - prompt
        - vectorization
    - Select **Generate**, then **Generate all**

- Create the FLLM core wheel

    - Browse to the FLLM cli extension folders
    - Run the following:
    ```cmd
    cd C:\github\solliancenet\fllm-cli
    python -m venv .venv  
    pip install wheel
    python setup.py bdist_wheel
    ```

    - PyPi:

    ```cmd
    cd C:\github\solliancenet\fllm-cli
    $env:Path += ";C:\Users\given\AppData\Roaming\Python\Python311\Scripts"
    twine upload --repository testpypi dist/*
    twine upload --repository pypi dist/*
    ```

- Create the FLLM cli extension wheel

    - Browse to the FLLM cli extension folders
    - Run the following:
    ```cmd
    cd C:\github\solliancenet\fllm-cli-extensions\src\fllm
    python -m venv .venv
    pip install wheel
    python setup.py bdist_wheel
    ```

    - PyPi:
    ```cmd    
    cd C:\github\solliancenet\fllm-cli-extensions\src\fllm
    $env:Path += ";C:\Users\given\AppData\Roaming\Python\Python311\Scripts"
    twine upload --repository testpypi dist/*
    twine upload --repository pypi dist/*
    ```
        
- Create the FLLM cli core wheel

    ```cmd
    cd C:\github\solliancenet\fllm-cli-core
    python -m venv .venv  
    pip install wheel
    pip install azure-mgmt-core
    python setup.py bdist_wheel
    pip install C:\github\solliancenet\fllm-cli-core\dist\fllm_cli_core-1.0.0-py3-none-any.whl --force-reinstall
    ```
    
    - PyPi:
    
    ```cmd
    cd C:\github\solliancenet\fllm-cli-core	
    twine upload --repository testpypi dist/*
    twine upload --repository pypi dist/*
    ```