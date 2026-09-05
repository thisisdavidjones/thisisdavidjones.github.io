{{ $pages := where site.RegularPages "Params.featured" true }}
{{ $pages = sort $pages "Params.featured_weight" }}
<ul class="selected-writing">
{{ range $pages }}
  <li>
    <a href="{{ .RelPermalink }}">{{ .Title }}</a>
    {{ with .Params.topics }}<small>{{ partial "topiclinks.html" . }}</small>{{ end }}
  </li>
{{ end }}
</ul>
<p class="more"><a href="{{ "/writing/" | relURL }}">All writing</a></p>
