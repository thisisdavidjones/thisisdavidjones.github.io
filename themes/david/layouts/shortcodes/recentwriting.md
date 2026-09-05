{{ $pages := where site.RegularPages "Section" "writing" }}
<ul class="recent writing-recent">
{{ range first 6 $pages.ByLastmod.Reverse }}
  <li>
    <p><a href="{{ .RelPermalink }}">{{ .Title }}</a>
    <small>revised {{ .Lastmod.Format "02 Jan 2006" }}</small></p>
  </li>
{{ end }}
</ul>
<p class="more"><a href="{{ "/writing/" | relURL }}">All writing</a></p>
