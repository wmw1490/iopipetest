from iopipe import IOpipe


@iopipe
def handler(event, context):
    
    return {"message": "Successfully executed"}
