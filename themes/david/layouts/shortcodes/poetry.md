{{ $attr := .Get "attr" }}
{{ $title := .Get "title" }}
<blockquote class="poetry">
{{if $title}}<p class="poemtitle">{{$title}}</p>{{end}}<pre>{{ .Inner }}</pre>{{ if $attr }}<footer>&mdash; {{$attr}}</footer>
{{end}}
</blockquote>
