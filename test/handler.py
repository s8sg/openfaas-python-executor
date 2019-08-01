import json
import os
import os.path
import sys

def handle(data):
    res = ""

    req = None
    
    try:
        req = json.loads(data)
    except Exception:
        res = "failed yo load json"
        return res
    job_id = req.get("job-id", "")
    if job_id == "":
        res = "job-id not provided"
        return res
    git_url = req.get("git-url", "")
    if git_url == "":
        res = "git-url not provided"
        return res
    script_name = req.get("script", "")
    if script_name == "":
        res = "script not provided"
        return res
    params = req.get("params", "")

    commands = []

    mkdir_command = 'mkdir -p /tmp/' + job_id + '/git'
    commands.append(mkdir_command)
    clone_command = 'git clone ' + git_url + ' /tmp/' + job_id + '/git'
    commands.append(clone_command)
    mv_command = 'mv /tmp/' + job_id + '/git/' + script_name + ' /tmp/' + job_id + '/git/main.py'
    commands.append(mv_command)

    #touch_command = 'touch ./'+ job_id + '/git/__init__.py;' + 'touch ./'+ job_id + '/__init__.py'
    #commands.append(touch_command)

    for command in commands:
        os.system(command)
    
    if os.path.isfile('/tmp/' + job_id + '/git/requirements.txt'):
        install_requirments = 'pip install -r ' + '/tmp/' + job_id + '/git/requirements.txt' 
        os.system(install_requirments)


    importlocation = '/tmp/' + job_id + '/git'

    sys.path.append(importlocation)
    try:
        from main import run 
        res = run(params=params)
    except Exception as e:
        res = "failed to import script: " + str(e)
    sys.path.remove(importlocation)

    return res
