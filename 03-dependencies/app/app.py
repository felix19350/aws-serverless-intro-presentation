import datetime
import json
import logging
import pathlib

from mako.template import Template

LOG = logging.getLogger("AWS_LAMBDA_LOGGER")
LOG.info("Init phase")

CONTENT_TYPES = {"JSON": "application/json", "HTML": "text/html"}


def lambda_handler(event, context):
    """
    Function that does content negotiation and displays different content according to
    what is received in the Accept header of the HTTP request.
    """
    LOG.info("Invoke phase")
    LOG.info(event)

    now = datetime.datetime.now().isoformat()

    # Very basic content negotiation
    accepted_content_types = event.get("headers").get("Accept")
    should_render_json = CONTENT_TYPES["JSON"] in accepted_content_types

    if should_render_json:
        payload = json_payload(now)
    else:
        payload = html_payload(now)
    return payload


def json_payload(invoke_time):
    """
    Produces the JSON response
    """
    return {
        "statusCode": 200,
        "headers": {
            "X-custom-header": "special json response",
            "Content-Type": CONTENT_TYPES["JSON"],
        },
        "body": json.dumps({"invoke_time": invoke_time}),
    }


def html_payload(invoke_time):
    """
    Produces the HTML response
    """
    path = pathlib.Path(__file__).parent.absolute()
    html_content = Template(filename=f"{path}/templates/home.html").render(
        invoke_time=invoke_time
    )
    return {
        "statusCode": 200,
        "headers": {
            "X-custom-header": "special html payload",
            "Content-Type": CONTENT_TYPES["HTML"],
        },
        "body": html_content,
    }
