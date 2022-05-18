from rest_framework.views import exception_handler, Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # 先调用Rest framework 默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    context_view = context.get("view", None)
    context_path = context.get('request').path
    context_method = context.get('request').method
    context_ip = context.get('request').META.get("REMOTE_ADDR")

    print('exc:', exc)
    print('context:', context)
    print('response:', response)
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
        print('detail:', detail)
        print('exc_code:', exc_code)
        print('non_field_errors:', non_field_errors)

        return Response({
            'errorCode': exc_code,
            'errorDetail': detail,
        }, status=response.status_code, exception=True)

    return response
