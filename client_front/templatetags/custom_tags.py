from django import template

from common.dict.dicts import CeleryStatusTypeDict

register = template.Library()


@register.inclusion_tag('tags/tag_status.html')
def status_tag(code):
    status = CeleryStatusTypeDict.objects.get(code=code)
    return {"status": status}
