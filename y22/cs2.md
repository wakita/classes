
title: 'コンピュータサイエンス第二'
class_id: 'cs2'
---

{% include classinfo.md %}

クラス共通情報
: [クラス共通情報のページ]({{ site.baseurl }}{%link years/y22/cs2/course.md %})


---
## 授業の内容

{% for page in site.pages %}
  {% if page.url contains "/y22/cs2/day" %}
- [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
  {% endif %}
{% endfor %}
