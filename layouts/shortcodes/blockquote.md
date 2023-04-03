{{ $src := .Get "src" }}
{{ $cite := .Get "cite" }}
{{ $extra := .Get "extra" }}
<blockquote>{{ .Inner}}{{if or ($src) ($cite) ($extra)}}
<footer>{{if $src}}{{ $src | markdownify }}{{end}} {{if $cite}}<cite>{{$cite | markdownify }}</cite>{{end}} {{if $cite}}{{$extra | markdownify }}{{end}}</footer>
{{end}}
</blockquote> 

