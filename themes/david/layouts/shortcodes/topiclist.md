<ul class="topic-list">
{{ range site.Data.topics.topics }}
  <li>
    <a href="{{ printf "/topics/%s/" .slug | relURL }}">{{ .name }}</a>
    <span>{{ .description }}</span>
  </li>
{{ end }}
</ul>
