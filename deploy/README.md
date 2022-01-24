
Create endpoint

```
manoj@surface$ az ml online-endpoint create -n hf-demo
Command group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Creating or updating online_endpoints
{
  "allow_public_access": true,
  "auth_mode": "key",
  "id": "/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/onlineEndpoints/hf-demo",
  "identity": {
    "principal_id": "1e019465-83a3-45b5-bb09-dc6f23ba3148",
    "tenant_id": "72f988bf-86f1-41af-91ab-2d7cd011db47",
    "type": "system_assigned"
  },
  "location": "eastus2",
  "name": "hf-demo",
  "properties": {
    "AzureAsyncOperationUri": "https://management.azure.com/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/providers/Microsoft.MachineLearningServices/locations/eastus2/mfeOperationsStatus/oe:c5b64b45-4a96-4790-8be2-ff7d3d5dd36c:820bf390-1159-46fc-b8f8-1600f3734f20?api-version=2021-10-01",
    "azureml.onlineendpointid": "/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourcegroups/opendatasetspmrg/providers/microsoft.machinelearningservices/workspaces/opendatasetspmworkspace/onlineendpoints/hf-demo"
  },
  "provisioning_state": "Succeeded",
  "resourceGroup": "OpenDatasetsPMRG",
  "scoring_uri": "https://hf-demo.eastus2.inference.ml.azure.com/score",
  "swagger_uri": "https://hf-demo.eastus2.inference.ml.azure.com/swagger.json",
  "tags": {},
  "traffic": {}
}
```
create local deployment to test before deploying to service

```
manoj@surface$ az ml online-deployment create --local --endpoint hf-demo --file deploy.yml 
Command group 'ml online-deployment' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Creating or updating online_deployments
Updating local deployment (hf-demo / blue) ........Done (0m 40s)
{
  "app_insights_enabled": false,
  "code_configuration": {
    "code": {
      "local_path": "/mnt/c/CODE/repos/HFsamples/deploy/score",
      "name": "26f28a10-9c93-44d9-8ecc-235a6a3ac241",
      "tags": {},
      "version": "1"
    },
    "scoring_script": "score.py"
  },
  "endpoint_name": "hf-demo",
  "environment": {
    "conda_file": {
      "channels": [
        "conda-forge"
      ],
      "dependencies": [
        "python=3.7",
        "numpy=1.21.2",
        "pip=21.2.4",
        {
          "pip": [
            "azureml-defaults==1.33.0",
            "inference-schema[numpy-support]==1.3.0",
            "joblib==1.0.1",
            "torch",
            "tensorflow",
            "transformers"
          ]
        }
      ],
      "name": "hf-model-env"
    },
    "image": "mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
    "name": "d5cc2497-e3ab-4634-9d57-1aec19deb2e2",
    "tags": {},
    "version": "1"
  },
  "environment_variables": {},
  "instance_count": 1,
  "instance_type": "Standard_F2s_v2",
  "model": {
    "flavors": {},
    "local_path": "/mnt/c/CODE/repos/HFsamples/deploy/model",
    "name": "cf850e77-15f8-459b-9ffa-8bd1d1e6c5a0",
    "properties": {},
    "tags": {},
    "version": "1"
  },
  "name": "blue",
  "properties": {},
  "tags": {},
  "type": "managed"
}
```
test local deployment

```
manoj@surface$ cat request.json 
"Microsoft, a company located in Redmond, was founded by Bill Gates"
manoj@surface$ az ml online-endpoint invoke --local --name hf-demo --request-file request.json 
Command group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
"\"[{'entity_group': 'ORG', 'score': 0.9992077, 'word': 'Microsoft', 'start': 1, 'end': 10}, {'entity_group': 'LOC', 'score': 0.9987621, 'word': 'Redmond', 'start': 33, 'end': 40}, {'entity_group': 'PER', 'score': 0.9986434, 'word': 'Bill Gates', 'start': 57, 'end': 67}]\""
manoj@surface$ 

manoj@surface$ az ml online-endpoint show --name hf-demo --localCommand group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus{
  "auth_mode": "key",
  "location": "local",
  "name": "hf-demo",
  "properties": {},
  "provisioning_state": "Succeeded",
  "scoring_uri": "http://localhost:49198/score",
  "tags": {},
  "traffic": {}
}

manoj@surface$ key=`az ml online-endpoint get-credentials --name hf-demo  -o tsv --query primaryKey`
WARNING: Command group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus

manoj@surface$ curl --request POST http://localhost:49198/score --header "Authorization: Bearer $key" --header 'Content-Type: application/json' --data @./request.json 
"[{'entity_group': 'ORG', 'score': 0.9992077, 'word': 'Microsoft', 'start': 1, 'end': 10}, {'entity_group': 'LOC', 'score': 0.9987621, 'word': 'Redmond', 'start': 33, 'end': 40}, {'entity_group': 'PER', 'score': 0.9986434, 'word': 'Bill Gates', 'start': 57, 'end': 67}]"manoj@surface$ 
```
deploy to managed online endpoint in Azure

```
manoj@surface$ az ml online-deployment create --endpoint hf-demo --file deploy.yml                  Command group 'ml online-deployment' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Creating or updating online_deployments
Check: endpoint hf-demo exists
Uploading score:   0%|                                                                                                                | 0.00/1.10k [00:00<?, ?B/s]
Uploading model:   0%|                                                                                                                  | 0.00/756 [00:00<?, ?B/s]
The deployment request OpenDatasetsPMWorkspace-hf-demo-2171952 was accepted. ARM deployment URI for reference: 
https://ms.portal.azure.com/#blade/HubsExtension/DeploymentDetailsBlade/overview/id/%2Fsubscriptions%2F21d8f407-c4c4-452e-87a4-e609bfb86248%2FresourceGroups%2FOpenDatasetsPMRG%2Fproviders%2FMicrosoft.Resources%2Fdeployments%2FOpenDatasetsPMWorkspace-hf-demo-2171952
Registering model version (6d1e450f-8e90-4d16-a0ec-ba38cb8de500 1 )  Done (1s)
Registering code version (f763c14c-c9c9-4514-b7f0-e1e1df256a9b 1 )  Done (0s)
Creating or updating deployment blue   ...........................................................................................................................................................................................................  Done (19m 9s)
Registering environment version (894f4efc-083f-446c-b489-46a95d337b9e 1 )  Done (12s)
Total time : 19m 22s
{
  "app_insights_enabled": false,
  "code_configuration": {
    "code": {
      "code_uri": "https://opendatasetspm6562936819.blob.core.windows.net/azureml-blobstore-c5b64b45-4a96-4790-8be2-ff7d3d5dd36c/LocalUpload/ac08b6e6b87b941a7ada92c6c5f27183/score",
      "id": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/codes/f763c14c-c9c9-4514-b7f0-e1e1df256a9b/versions/1",
      "local_path": "/mnt/c/CODE/repos/HFsamples/deploy/score",
      "name": "f763c14c-c9c9-4514-b7f0-e1e1df256a9b",
      "resourceGroup": "OpenDatasetsPMRG",
      "tags": {},
      "version": "1"
    },
    "scoring_script": "score.py"
  },
  "endpoint_name": "hf-demo",
  "environment": {
    "conda_file": {
      "channels": [
        "conda-forge"
      ],
      "dependencies": [
        "python=3.7",
        "numpy=1.21.2",
        "pip=21.2.4",
        {
          "pip": [
            "azureml-defaults==1.33.0",
            "inference-schema[numpy-support]==1.3.0",
            "joblib==1.0.1",
            "torch",
            "tensorflow",
            "transformers"
          ]
        }
      ],
      "name": "hf-model-env"
    },
    "id": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/environments/894f4efc-083f-446c-b489-46a95d337b9e/versions/1",
    "image": "mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
    "name": "894f4efc-083f-446c-b489-46a95d337b9e",
    "resourceGroup": "OpenDatasetsPMRG",
    "tags": {},
    "version": "1"
  },
  "environment_variables": {},
  "instance_count": 1,
  "instance_type": "Standard_F2s_v2",
  "model": {
    "flavors": {},
    "id": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/models/6d1e450f-8e90-4d16-a0ec-ba38cb8de500/versions/1",
    "local_path": "/mnt/c/CODE/repos/HFsamples/deploy/model",
    "model_uri": "azureml://subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/workspaces/OpenDatasetsPMWorkspace/datastores/workspaceblobstore/paths/LocalUpload/0e0b580d527d72f39abdfe6b4f6cf262/model",
    "name": "6d1e450f-8e90-4d16-a0ec-ba38cb8de500",
    "properties": {},
    "resourceGroup": "OpenDatasetsPMRG",
    "tags": {},
    "version": "1"
  },
  "name": "blue",
  "properties": {},
  "tags": {},
  "type": "managed"
}
```
test Azure deployment

```
manoj@surface$ uri=`az ml online-endpoint show --name hf-demo -o tsv --query scoring_uri`
WARNING: Command group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
manoj@surface$ echo $uri
https://hf-demo.eastus2.inference.ml.azure.com/score
manoj@surface$ key=`az ml online-endpoint get-credentials --name hf-demo  -o tsv --query primaryKey`
WARNING: Command group 'ml online-endpoint' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
manoj@surface$ curl --request POST $uri --header "Authorization: Bearer $key" --header 'Content-Type: application/json' --data @./request.json 
"[{'entity_group': 'ORG', 'score': 0.9992077, 'word': 'Microsoft', 'start': 1, 'end': 10}, {'entity_group': 'LOC', 'score': 0.9987621, 'word': 'Redmond', 'start': 33, 'end': 40}, {'entity_group': 'PER', 'score': 0.9986434, 'word': 'Bill Gates', 'start': 57, 'end': 67}]"
```