import datetime
import json
import logging

LOG = logging.getLogger("AWS_LAMBDA_LOGGER")
LOG.setLevel(logging.INFO)
LOG.info("Init phase")


def lambda_handler(event, context):
    """
    Simple function to test the AWS API gateway integration, printing the incoming event
    and then returning the current date, with a custom header.
    """
    LOG.info("Invoke phase")
    LOG.info(event)

    now = datetime.datetime.now().isoformat()
    return {
        "statusCode": 200,
        "headers": {
            "X-custom-header": "my-custom-header",
            "content-type": "application/json",
        },
        "body": json.dumps({"invoke_time": now}),
    }
