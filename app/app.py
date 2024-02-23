from flask import Response, json
from presentation.route import wsgi
from werkzeug.exceptions import HTTPException


@wsgi.errorhandler(HTTPException)
def handle_exception(e: HTTPException):
    """Return JSON instead of HTML for HTTP errors."""
    return Response(
        response=json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }),
        status=e.code,
        content_type="application/json"
    )

if __name__ == "__main__":
    wsgi.run(host="0.0.0.0", port=8080, debug=True)
