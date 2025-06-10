from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

{% for tag in tags %}
from .cache_{{ tag }} import {{ tag | capitalize }}CacheModel
{% endfor %}

__all__ = [
    {% for tag in tags %}
    "{{ tag | capitalize }}CacheModel",
    {% endfor %}
]
