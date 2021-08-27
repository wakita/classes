{% for course in site.data.classes %}
{% if course.Name == page.title %}
# {{ course.Number }}

{{ course.AcademicYear }}年度{{ course.Quarter}} {{ course.Name }}: {{ course.Number }}

担当教員
: {{ course.Instructors }}

授業の形式
: {{ course.Components }} - {{ course.Credits }}単位; {{ course.Room }}

使用言語
: {{ course.LanguageUsed }}

{% if course.T2Schola %}
T2Schola
: [T2Scholaへのリンク]({{ course.T2Schola }})
{% endif %}

{% if course.Syllabus %}
シラバス
: <a href="{{ course.Syllabus }}" target="_blank">シラバスへのリンク</a>
{% endif %}

{% endif %}
{% endfor %}
