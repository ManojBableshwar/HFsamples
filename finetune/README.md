
Submit fine-tuning job

```
(base) root@mabablessurface:/mnt/c/CODE/repos/HFsamples/finetune# az ml job create --file pipeline.yml 
Command group 'ml job' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Uploading finetune:   0%|                                                                                            | 0.00/2.26k [00:00<?, ?B/s]
{
  "creation_context": {
    "created_at": "2022-01-24T03:23:36.497333+00:00",
    "created_by": "Manoj Bableshwar",
    "created_by_type": "User"
  },
  "display_name": "purple_raisin_dthc74zh",
  "experiment_name": "finetune",
  "id": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/jobs/3d9064f4-ac8c-4c42-8b39-10e984963d9a",
  "inputs": {},
  "jobs": {
    "fine-tune": {
      "component": "azureml:fc6deb72-5eb4-4d6b-be91-0187dce41e81:1",
      "compute": "azureml:gpu-cluster",
      "inputs": {},
      "outputs": {
        "finetuned_model": {
          "mode": "rw_mount"
        }
      },
      "overrides": {},
      "type": "component"
    }
  },
  "name": "3d9064f4-ac8c-4c42-8b39-10e984963d9a",
  "outputs": {},
  "properties": {
    "azureml.continue_on_step_failure": "False",
    "azureml.git.dirty": "True",
    "azureml.parameters": "{}",
    "azureml.pipelineComponent": "pipelinerun",
    "azureml.runsource": "azureml.PipelineRun",
    "mlflow.source.git.branch": "main",
    "mlflow.source.git.commit": "e9311d3643debcd0103d1fd5cae35551dc6df9ff",
    "mlflow.source.git.repoURL": "https://github.com/ManojBableshwar/HFsamples.git",
    "runSource": "MFE",
    "runType": "HTTP"
  },
  "resourceGroup": "OpenDatasetsPMRG",
  "services": {
    "Studio": {
      "endpoint": "https://ml.azure.com/runs/3d9064f4-ac8c-4c42-8b39-10e984963d9a?wsid=/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourcegroups/OpenDatasetsPMRG/workspaces/OpenDatasetsPMWorkspace&tid=72f988bf-86f1-41af-91ab-2d7cd011db47",
      "job_service_type": "Studio"
    },
    "Tracking": {
      "endpoint": "azureml://eastus2.api.azureml.ms/mlflow/v1.0/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace?",
      "job_service_type": "Tracking"
    }
  },
  "settings": {},
  "status": "Preparing",
  "tags": {
    "azureml.Designer": "true"
  },
  "type": "pipeline"
}
```