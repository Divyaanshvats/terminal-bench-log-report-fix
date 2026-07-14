There is an Apache-style access log located at:

/app/access.log

Analyze the log and generate a JSON report at:

/app/report.json

The report must contain the following fields:

- total_requests: the total number of requests in the log.
- unique_ips: the number of unique client IP addresses.
- top_path: the request path that appears most frequently.

Success criteria:

1. Create /app/report.json.
2. Set total_requests to the total number of log entries.
3. Set unique_ips to the number of unique client IP addresses.
4. Set top_path to the most frequently requested request path.

The output must be valid JSON.