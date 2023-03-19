{{$changes := site.Data.changelog.changes}}
{{ $matchpattern := "([]])[^](]|]$"}}

<ul class="recent">
{{ range first 20 $changes }}
  <li><p>{{.date}} - {{ .title | markdownify}} - {{ .details  | markdownify}} </p></li>
  {{end }}
</ul>