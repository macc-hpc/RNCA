##############################################
#
#  RNCA reporting syntax for technical reporting
#  September 2021
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
sample_data_cloud ={
    "report_type": "Resource_Usage_cloud",
    "report_version": "1.0",
    "report_date": "2021-04-09 10:47:00",
    "RNCA_resource_id": "6b4e1dae-c64d-47da-b740-83454815d773",
    "items": [
        {
            "RNCA_proj_ID": "CPCA21/4",
            "CPUcore_sec": "1100",
            "Disk_GB": "20900",
            "RAM_MB": "2000",
            "Servers_number": "3",
        },
        {
            "RNCA_proj_ID": "CPCA21/4",
            "CPUcore_sec": "1100",
            "Disk_GB": "20900",
            "RAM_MB": "2000",
            "Servers_number": "3",
        },
    ]
} 
      
json_object = json.dumps(sample_data_HPC, indent = 4)
print(json_object)

json_object = json.dumps(sample_data_cloud, indent = 4) 
print(json_object)

# More information:

#     "RNCA_resource_id" = ID given by FCT. ID of the technological platform
#        on a operational center
       
#     "RNCA_proj_ID" = ID given by FCT. ID of an approved project by FCT

    
#############################
#https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
# head  HPC01_202108300100_usage.CSV
#JobIDRaw|User|Partition|Submit|Start|Elapsed|AllocCPUS|CPUTime|CPUTimeRAW|MaxRSS|State|NodeList|Account
    ############
#    JobIDRaw|User|Account|Partition|Submit|Start|Elapsed|AllocTRES|CPUTime|CPUTimeRAW|MaxRSS|State|NodeList

#52985|psilva|base|2021-08-05T11:05:32|2021-08-29T18:55:04|02:25:45|1152|116-14:24:00|10074240||COMPLETED|c805-[901,903-904],c817-[001-002,102-104,201-202,502-503,601-604,701-704,802-804,901-904],c821-[002-004,101-104,201-204,702-704,802-804,901,903-904],c823-[001-004,101-104,201,303-304,401-404,501-504,601,704,801-804]|cpca_a2_7085_2020

####################
#Account,CPU Hours,Disk GB-Hours,RAM MB-Hours,Servers
#covid-synergy,2688.0,6720.0,5505024.0,1
#epicovpt,None,None,None,None
#inescid,1848.0,15120.0,2236416.0,3
