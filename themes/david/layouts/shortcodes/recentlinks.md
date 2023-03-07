{{$links := site.Data.links.links}}
{{ $matchpattern := "([]])[^](]|]$"}}
<ul>
{{ range $links }}
{{ $markdownLink := printf "%s%s%s" "](" .link ") " }}
{{ $replaced := replaceRE $matchpattern $markdownLink  .text }}
  <li><p>{{ $replaced | markdownify}}</p></li>
{{ end }}
</ul>