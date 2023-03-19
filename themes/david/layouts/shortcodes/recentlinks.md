{{$links := site.Data.links.links}}
{{ $matchpattern := "([]])[^](]|]$"}}

<ul class="recent">
{{ range first 8 $links }}
{{ $markdownLink := printf "%s%s%s" "](" .link ") " }}
{{ $replaced := replaceRE $matchpattern $markdownLink  .text }}
  <li><p>{{ $replaced | markdownify}}</p></li>
  {{end }}
</ul>
{{ $more := printf "%s" "[More links](/links/)"}}
<span class="more">{{ $more | markdownify }}</span>