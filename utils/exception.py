from rest_framework.views import exception_handler, Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # 先调用Rest framework 默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    print('exc:', exc)
    print('context:', context)
    print('response:', response)
    print('exception = %s - %s - %s' % (context['view'], context['request'].method, exc))

    if response is None:
        return Response({
            'message': '服务器错误:{exc}'.format(exc=exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    else:
        return Response({
            'message': '服务器错误:{exc}'.format(exc=exc),
        }, status=response.status_code, exception=True)

    return response
