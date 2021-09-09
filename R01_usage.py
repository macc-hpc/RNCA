##############################################
#
#  RNCA practical reporting syntax for technical reporting
#
#  Generates sample JSON output
#
#  Please read
#       R01_usage_output.txt
#       R01_usage_output_explained.txt
#
#  September 2021, FCT-FCCN
#

import json 

sample_data_HPC ={
    "report_type": "Resource_Usage_HPC",
    "report_version": "1.0",
    "report_date": "2021-04-09 10:47:00",
    "RNCA_resource_id": "2fa8f900-f896-4fe4-8bc1-2691b8ac8fda",
    "items": [
        {
            "RNCA_proj_ID": "CPCA21/1",
            "job_id": "123",
            "job_state": "COMPLETED",
            "CPUcore_sec": "1000",
            "GPU_sec": "100",
            "RAM_GB": "200",
            "Disk_GB": "2000",
        },
        {
            "RNCA_proj_ID": "CPCA21/1",
            "job_id": "124",
            "job_state": "FAILED",
            "CPUcore_sec": "1000",
            "GPU_sec": "100",
            "RAM_GB": "200",
            "Disk_GB": "2000",
        },
    ]
}
####################
# version history:
# V1.1- added GPU capability
sample_data_cloud ={
    "report_type": "Resource_Usage_cloud",
    "report_version": "1.1",
    "report_date": "2021-04-09 10:47:00",
    "RNCA_resource_id": "6b4e1dae-c64d-47da-b740-83454815d773",
    "items": [
        {
            "RNCA_proj_ID": "CPCA21/4",
            "CPUcore_hours": "1100",
            "GPU_hours": "",
            "Disk_GB_hours": "20900",
            "RAM_MB_hours": "2000",
            "Servers_number": "3",
        },
        {
            "RNCA_proj_ID": "CPCA21/5",
            "CPUcore_hours": "100",
            "GPU_hours": "100",
            "Disk_GB_hours": "2000",
            "RAM_MB_hours": "200",
            "Servers_number": "1",
        },
    ]
} 
      
json_object = json.dumps(sample_data_HPC, indent = 4)
print(json_object)

json_object = json.dumps(sample_data_cloud, indent = 4) 
print(json_object)

