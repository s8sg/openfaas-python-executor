import json
import os
import importlib
import os.path

def handle(data):
    res = ""

    req = None
    
    try:
        req = json.loads(data)
    except Exception:
        res = "failed yo load json"
        return res
    job_id = req["job-id"]
    if job_id == "":
        res = "job-id not provided"
        return res
    git_url = req["git-url"]
    if git_url == "":
        res = "git-url not provided"
        return res
    script_name = req["script"]
    if script_name == "":
        res = "script not provided"
        return res
    params = req["params"]
    if params == "":
        res = "params not provided"
        return res


    commands = []

    mkdir_command = 'mkdir -p /tmp/' + job_id + '/git'
    commands.append(mkdir_command)
    clone_command = 'git clone ' + git_url + ' /tmp/' + job_id + '/git'
    commands.append(clone_command)


    for index in commands:
        os.system(commands[index])
    
    if os.path.isfile('/tmp/' + job_id + '/git/requirements.txt'):
        install_requirments = 'pip install -r ' + '/tmp/' + job_id + '/git/requirements.txt' 
        os.system(install_requirments)

    importlocation = '/tmp/' + job_id + '/git/' + script_name

    script_module = None
    try:
        script_module = importlib.import_module(importlocation)
    except Exception:
        res = "failed to import script"
        return res

    res = script_module.run()

    return res
