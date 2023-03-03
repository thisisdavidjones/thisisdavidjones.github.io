{{ $src := .Get "src" }}
{{ $cite := .Get "cite" }}
{{ $extra := .Get "extra" }}
<div class="epigraph" >
<blockquote>
{{ .Inner}}
{{if or ($src) ($cite) ($extra)}}
<footer>{{if $src}}{{$src}}{{end}} {{if $cite}}<cite>{{$cite}}</cite>{{end}} {{if $cite}}{{$extra}}{{end}}</footer>
{{end}}
</blockquote>

</div>

