import logging
from django.utils.deprecation import MiddlewareMixin

application_logger = logging.getLogger("application-logger")
error_logger = logging.getLogger("error-loger")

class MyMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        application_logger.info(request.get_full_path())

    def process_exception(self, request, exception):
        error_logger, 