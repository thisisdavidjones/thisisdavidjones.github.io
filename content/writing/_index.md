---
title: "Writing"
---
{{ define "main" }}
  <h1>{{ .Title }}</h1>

  {{/* List immediate children first (subsections and pages) */}}
  {{ range .Pages.ByLastmod.Reverse }}
    <article>
      <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle | default .Title }}</a></h2>
      {{ with .Summary }}<p>{{ . }}</p>{{ end }}
      <p class="meta">
        Updated: {{ .Lastmod.Format "2006-01-02 15:04" }}
      </p>
    </article>
  {{ end }}

  {{/* Optionally include nested content across the whole subtree */}}
  <h3>Everything in this section</h3>
  <ul>
    {{ range .Site.RegularPages }}
      {{ if strings.HasPrefix .File.Dir (print .CurrentSection.File.Dir) }}
        <li><a href="{{ .RelPermalink }}">{{ .Title }}</a></li>
      {{ end }}
    {{ end }}
  </ul>
{{ end }}