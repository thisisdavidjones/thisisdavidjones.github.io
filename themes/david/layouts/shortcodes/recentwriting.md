{{$links := site.Data.recentwriting.recentwriting}}
{{ $matchpattern := "([]])[^](]|]$"}}

<ul class="recent">
{{ range first 1 $links }}
{{ $markdownLink := printf "%s%s%s" "](" .link ") " }}
{{ $replaced := replaceRE $matchpattern $markdownLink  .text }}
  <li><p>{{ $replaced | markdownify}}</p></li>
  {{end }}
</ul>