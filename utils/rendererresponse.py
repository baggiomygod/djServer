"""
自定义返回处理
"""

from rest_framework.renderers import JSONRenderer


class CustomerRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print('data:', data)
        print('accepted_media_type:', accepted_media_type)
        print('renderer_context:', renderer_context)
        if renderer_context:
            # 如果返回的data为字典
            if isinstance(data, dict):
                msg = data.pop('message', 'success')
                code = data.pop('code', renderer_context['response'].status_code)
            # 如果不是字典则将msg内容改为请求成功 code改为请求的状态码
            else:
                msg = 'success'
                code = renderer_context['response'].status_code

            ret = {
                'msg': msg,
                'code': code,
                'data': data
            }
            return super().render(ret, accepted_media_type, renderer_context)

        else:
            return super().render(data, accepted_media_type, renderer_context)
