from app import app
from functools import wraps
def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception
    @wraps(handle_http_exception)
    def ret_val(exception):
        exc = handle_http_exception(exception)  
        return {'status_code':exc.code, "name": exc.name, 'description':exc.description}, exc.code
    return ret_val

# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)

