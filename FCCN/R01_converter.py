# -*- coding: utf-8 -*-
import csv
import sys
import json

#columns of the CSV file:
#JobIDRaw|User|Account|Partition|Submit|Start|Elapsed|AllocCPUS|CPUTime|CPUTimeRAW|MaxRSS|State|NodeList

# 0 JobIDRaw
# 1 User
# 2 Account
# 3 Partition
# 4 Submit
# 5 Start
# 6 Elapsed
# 7 AllocCPUS
# 8 CPUTime
# 9 CPUTimeRAW
# 10 MaxRSS
# 11 State
# 12 NodeList

sample_data_HPC ={
    "report_type": "Resource_Usage_HPC",
    "report_version": "1.0",
    "report_date": "_sample_",
    "RNCA_resource_id": "_sample_",
    "items": []
} 
filen="R01_slurm_sample.csv"
with open(filen) as csvfile:
  readCSV = csv.reader(csvfile, delimiter='|')
  lineno=0
  for row in readCSV:
    lineno+=1
    if lineno==1:
      if row[1]!='User' or row[11]!='State':
          print("error 1")
          sys.exit(1)
      else:
          continue
    #print(row)
    item={
          "RNCA_proj_ID": "",
          "job_id": "",
          "job_state": "",
          "CPUcore_sec": "",
          "GPU_sec": "",
          "RAM_GB": "",
          "Disk_GB": "",
    }
    item["RNCA_proj_ID"]=row[2]
    item["job_id"]=row[0]
    item["job_state"]=row[11]
    item["CPUcore_sec"]=row[9]
    #sample_data_HPC["items"].append(item.copy())
    sample_data_HPC["items"].append(item)

json_object = json.dumps(sample_data_HPC, indent = 4)
print(json_object)
