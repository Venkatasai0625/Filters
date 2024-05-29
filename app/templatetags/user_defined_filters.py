from django import template
register=template.Library()
def swap(str1):
    return str1.swapcase()
register.filter('swapcase',swap)

#@register.filter()
@register.filter(name="remo")
def remove(str1,chr):
    return str1.replace(chr,"")

#register.filter('rem',remove)

