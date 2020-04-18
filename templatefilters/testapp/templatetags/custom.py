from django import template
register=template.Library()

def truncate_n(value,n):
    res=value[0:n]
    return res

register.filter('truncate',truncate_n)