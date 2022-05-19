from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler, Response
from rest_framework import status

"""
        print('exc:', exc)
        # context_view = context.get("view", None)
        # context_path = context.get('request').path
        # context_method = context.get('request').method
        # context_ip = context.get('request').META.get("REMOTE_ADDR")
"""


def custom_exception_handler(exc, context):
    print('exc:', exc)
    # ValidationError 校验错误
    if isinstance(exc, ValidationError):
        detail = exc.detail
        key = next(iter(detail))
        error = detail[key]  # [ErrorDetail(string='Unsupported file extension.', code='invalid ext')]
        return Response({
            'errorCode': 'invalid',
            'errorDetail': error[0],

        }, status=status.HTTP_200_OK, exception=True)
    else:  # Http404 PermissionDenied  exceptions.APIException
        # 先调用Rest framework 默认的异常处理方法获得标准错误响应对象
        response = exception_handler(exc, context)
        print('exception = %s - %s - %s' % (context['view'], context['request'].method, exc))

        if response is None:
            return Response({
                'errorCode': '{exc}'.format(exc=exc),
                'errorDetail': '',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
        else:
            detail = response.data.get('detail')
            exc_code = response.data.get('code')
            non_field_errors = response.data.get('non_field_errors')
            print('non_field_errors:', non_field_errors)

            return Response({
                'errorCode': exc_code,
                'errorDetail': detail,
            }, status=response.status_code, exception=True)

        return response
