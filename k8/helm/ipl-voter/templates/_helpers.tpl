{{- define "ipl-voter.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "ipl-voter.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "ipl-voter.labels" -}}
app.kubernetes.io/name: {{ include "ipl-voter.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "ipl-voter.selectorLabels" -}}
app.kubernetes.io/name: {{ include "ipl-voter.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}