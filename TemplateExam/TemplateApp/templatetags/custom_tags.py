from django import template
from datetime import datetime
import math

register = template.Library()

@register.filter(name="calculate_datetime_to_now")
def calculate_datetime_to_now(value):
    joined_datetime = datetime.strptime(value, "%Y/%m/%d")
    now_datetime = datetime.now()
    diff_datetime = now_datetime - joined_datetime
    diff_days = diff_datetime.days
