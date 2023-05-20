import datetime
import json
import pathlib

from aws_lambda_powertools import Logger, Metrics
from aws_lambda_powertools.metrics import MetricResolution, MetricUnit
from mako.template import Template

LOG = Logger()
LOG.info("Init phase")


metrics = Metrics()
metrics.add_metric(
    name="NumColdStarts",
    unit=MetricUnit.Count,
    value=1,
    resolution=MetricResolution.High,
)

CONTENT_TYPES = {"JSON": "application/json", "HTML": "text/html"}


@metrics.log_metrics  # ensures metrics are flushed upon request completion/failure
@LOG.inject_lambda_context(log_event=True)
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

    # Let's add an additional parameter to our structured logging
    LOG.append_keys(is_json=should_render_json)
    LOG.info("Rendering response")

    # And here we are capturing some "business metrics"
    if should_render_json:
        metrics.add_metric(
            name="NumJsonResponses",
            unit=MetricUnit.Count,
            value=1,
            resolution=MetricResolution.High,
        )
        payload = json_payload(now)
    else:
        metrics.add_metric(
            name="NumHtmlResponses",
            unit=MetricUnit.Count,
            value=1,
            resolution=MetricResolution.High,
        )
        payload = html_payload(now)
    return payload


def json_payload(invoke_time):
    """
    Produces the JSON response
    """
    return {
        "statusCode": 200,
        "headers": {
            "X-custom-header": "Demo 04",
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
            "X-custom-header": "Demo 04",
            "Content-Type": CONTENT_TYPES["HTML"],
        },
        "body": html_content,
    }
