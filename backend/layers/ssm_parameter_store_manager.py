# This is a Lambda layer that handles writes and reads on the SSM Parameter store
# https://eu-west-1.console.aws.amazon.com/systems-manager/parameters?region=eu-west-1
# https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

import json
import boto3

session = boto3.Session(region_name='eu-west-1')
ssm = boto3.client('ssm')

# get_ssm_param(dataToRead) retrieves the value for parameters in SSM Parameter Store
# and returns a JSON with parameters and value
# dataToRead is a JSON message with an array param_names 
# {
#    param_names: ['param1','param2'...]
# }
def get_ssm_param(dataToRead):
    param_names = (json.loads(dataToRead))['param_names']

    parameters = ssm.get_parameters(
        Names=param_names,
        WithDecryption=True,
    )
    response = {}
    for param in parameters['Parameters']:
       response[param.get('Name')] = param.get('Value')
   
    return json.dumps(response)


# get_ssm_param(dataToStore) write parameter/value in SSM Parameter Store with encryption ON
# and returns boolean (true: operation went well, false: problem writting)
# dataToStore is a JSON message 
# {
#   'Name' : 'nameOfTheParameter',
#   'Value': 'valueOfTheParameter'
# }
# if the parameter exists already, it will be overwritten
def set_ssm_param(dataToStore):
        data = json.loads(dataToStore)
        response = ssm.put_parameter(
                Name=data['Name'],
                Value=data['Value'],
                Type='SecureString',
                Overwrite=True
                )
        return response


# delete_ssm_param(dataToDelete) deletes parameter entries in SSM Parameter Store
# and returns a JSON with parameters and values
# dataToDelete is a JSON message with an array param_names 
# {
#    param_names: ['param1','param2'...]
# }
def delete_ssm_param(dataToDelete):
        #We retrieve the data first 
        response = get_ssm_param(dataToDelete)
        
        data = json.loads(dataToDelete)
        #and delete it

        ssm.delete_parameters(Names=data['param_names'])
        return response
