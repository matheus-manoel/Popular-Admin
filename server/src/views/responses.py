from http import HTTPStatus
import json


def build_response(raw_response, created=False):
    """Build a full response"""
    if raw_response is not None:
        status_code = 201 if created else 200
    else:
        status_code = 404
    return json.dumps(raw_response), status_code, {'Content-Type': 'application/json'}


def _assemble_response(success, custom_message, code, content_type={'Content-Type': 'application/json'}):
    """Assemble a response"""
    response = {'success': success}
    if custom_message:
        response['message'] = custom_message

    return json.dumps(response), code, content_type


custom_message = 'A required query parameter was not specified for this request.'
def missing_required_query_parameter(custom_message=custom_message):
    """Return a 400 (Bad Request) and a failure message"""
    return _assemble_response(False, custom_message, 400)


custom_message = 'A required payload parameter was not specified for this request.'
def missing_required_payload_parameter(custom_message=custom_message):
    """Return a 400 (Bad Request) and a failure message"""
    return _assemble_response(False, custom_message, 400)


def success(custom_message=None):
    """Return a 200 and a success message"""
    return _assemble_response(True, custom_message, 200)


def fail(custom_message=None):
    """Return a 404 and a failure message"""
    return _assemble_response(False, custom_message, 404)

custom_message = ''
def forbidden(custom_message=None):
    """Return a 403 and a forbbiden message"""
    return _assemble_response(False, custom_message, 403)


def unprocessable_entity(custom_message):
    """Return a 422 and a message explaining why the entity is unprocessable."""
    return _assemble_response(False, custom_message, 422)


def unauthorized(custom_message=HTTPStatus.UNAUTHORIZED.description):
    '''Return a 401 and a message explaining the agent was unaithorized.'''
    return _assemble_response(False, custom_message, HTTPStatus.UNAUTHORIZED.value)
