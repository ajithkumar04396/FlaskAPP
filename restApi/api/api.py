from restApi.restApi import restApi
from app import app, limiter, validate_json
from flask import request, session, abort


@restApi.route("/getHeaders", methods=['GET'])
@limiter.limit(limit_value="20 per day", error_message="You have reached the maximum limit for the day", override_defaults=False)
def getHeaders():
    app.logger.info('Getting http headers...!')
    return {"status": True}


@restApi.route("/validator", methods=["POST"])
@limiter.limit(limit_value="20 per day", error_message="You have reached the maximum limit for the day", override_defaults=False)
@validate_json({
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
    },
    'required': ['name']
})
def validator():
    app.logger.info(request.json)
    return {"status": True, "data": request.json}


@restApi.route("/validatorAbort", methods=["POST"])
@limiter.limit(limit_value="20 per day", error_message="You have reached the maximum limit for the day", override_defaults=False)
def validatorAbort():
    abort(500, "I'm not in the mood to talk!")