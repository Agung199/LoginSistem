# membuat middleware logging
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        print(f"Request URL: {request.url}")
        print(f"Request Methode: {request.method}")

        response = await call_next(request)

        print(f"Response status: {response.status_code}")

        return response
