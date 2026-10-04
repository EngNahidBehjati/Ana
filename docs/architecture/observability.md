# Observability Baseline

Sprint 0 baseline:
- structured JSON application logging (structlog)
- explicit `/api/v1/health` endpoint
- environment-driven log level

To add when the first production/staging deployment exists:
- request/correlation IDs
- error tracking provider
- latency/error-rate metrics
- external health monitoring
- alerting thresholds

Tracing is deferred until distributed or latency-diagnosis needs justify it.
