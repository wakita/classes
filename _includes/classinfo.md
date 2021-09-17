<style>
.entry-title {
background-color: #ddd;
}
</style>

{% assign class_id = "all" %}
{% if page.class_id %}
  {% assign class_id = page.class_id %}
{% endif %}

{% assign classes = site.data.classes[page.year].classes %}

{% for class in site.data.classes[page.year].classes %}
{% if class_id == "all" or class.ID == class_id %}

# {{ class.Number }}
{{ page.year }}年度{{ class.Quarter}} {{ class.Name }}

担当教員
: {{ class.Instructors }}

授業の形式
: {{ class.Components }} - {{ class.Credits }}単位; {{ class.Room }}

使用言語
: {{ class.LanguageUsed }}

{% if class.T2Schola != "" %}
T2Schola
: [T2Scholaへのリンク]({{ class.T2Schola }})
{% endif %}

{% if class.Syllabus != "" %}
シラバス
: <a href="{{ class.Syllabus }}" target="_blank">シラバスへのリンク</a>
{% endif %}

{% endif %}
{% endfor %}
