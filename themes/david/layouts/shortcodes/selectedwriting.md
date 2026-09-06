{{ $selection := index hugo.Data "selected-writing" }}
<ul class="selected-writing">
{{ range $path := $selection }}
  {{ $page := site.GetPage $path }}
  {{ if not $page }}
    {{ errorf "Selected writing manifest refers to missing page %q" $path }}
  {{ else }}
  <li>
    <a href="{{ $page.RelPermalink }}">{{ $page.Title }}</a>
    {{ with $page.Params.topics }}<small>{{ partial "topiclinks.html" . }}</small>{{ end }}
  </li>
  {{ end }}
{{ end }}
</ul>
<p class="more"><a href="{{ "/writing/" | relURL }}">All writing</a></p>
