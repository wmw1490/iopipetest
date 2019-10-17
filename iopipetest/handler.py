from iopipe import IOpipe

iopipe = IOpipe()

@iopipe
def handler(event, context):
    
    return {"message": "Successfully executed"}
