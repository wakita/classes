---
layout: collection
entries_layout: grid
title: 'Courses'
collection: courses
permalink: /
---

<!--
このサイトのメニューはこのサイトの右上端に表示されている三本線[^hamburder_menu]です。

[^hamburder_menu]: ハンバーガーメニューと呼びます。

# 開講授業

{% for course in site.data.classes %}
- {{ course.OfferedQuarter }}: [{{ course.Number }} -- {{ course.Name }}](courses/{{ course.ID }}/)

{% endfor %}
-->
