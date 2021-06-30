
def send_factura(factura):
    

def lambda_handler(event, context): 
    """AWS Lambda Function entrypoint to cancel booking

    Parameters
    ----------
    event: dict, required
        facturaId:

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    -------
    boolean

    """

    factura_id = event.get("facturaId")
    if not factura_id:
        raise ValueError("Factura Invalida")

    try:
        
        # response = send_factura(factura)
        return { 'code': 200, "message": "Factura enviada a la cola"}
    except Exception as err:
        raise ValueError({"operation": "failed send the queue"})
