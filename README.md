# Terminal Report Terminal Bench Fix

A repaired Terminal-Bench style software engineering task that parses an Apache access log and generates a JSON summary report.

This project focuses on improving task reproducibility, verification quality, and instruction clarity rather than changing the underlying programming problem.

---

# Objective

The task reads an Apache-style access log and generates a JSON report containing:

- Total number of requests
- Number of unique client IP addresses
- Most frequently requested path

The generated report is saved as:

```

/app/report.json

```

---

# Project Structure

```

log-report/
│
├── environment/
│   ├── Dockerfile
│   ├── access.log
│
├── solution/
│   ├── solve.py
│   └── solve.sh
│
├── tests/
│   ├── test_outputs.py
│   └── test.sh
│
├── instruction.md
└── task.toml

```

---

# Processing Flow

```text
              Apache Access Log
                      │
                      ▼
              solution/solve.py
                      │
         Parse every log entry
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Count Requests   Count Unique IPs   Count Paths
      │               │                │
      └───────────────┼────────────────┘
                      │
                      ▼
        Determine Most Requested Path
                      │
                      ▼
          Generate report.json
                      │
                      ▼
        tests/test_outputs.py
                      │
        Validate expected values
                      │
                      ▼
             Reward 1 / Reward 0
```

---

# Output Format

The generated report follows the format below.

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

---

# Improvements Made

## 1. Task Format

- Corrected the Harbor task configuration.
- Updated the artifact declaration.
- Completed required metadata.
- Ensured the declared artifact matches the generated output.

---

## 2. Environment

- Replaced the floating Docker image with a pinned image digest.
- Removed the leaked reference solution from the build context.
- Installed verifier dependencies during image build.
- Disabled unnecessary internet access.

---

## 3. Verifier

The original verifier only checked whether `report.json` existed and was non-empty.

The updated verifier validates:

- report creation
- total request count
- unique IP count
- most frequently requested path

This prevents incorrect implementations from passing.

---

## 4. Instructions

The instructions were rewritten to:

- clearly define the input file
- specify the output location
- document the required JSON schema
- define explicit success criteria

The instructions now match the verifier exactly.

---

# Verification

Two verification scenarios were executed.

### Oracle

Expected Result

```

Reward = 1

```

All verifier tests pass.

---

### No-op Agent

Expected Result

```

Reward = 0

```

No report is generated and all verifier checks fail.

---

### Incorrect Solution Test

An intentional bug was introduced by writing incorrect values for:

- total_requests
- unique_ips

The verifier correctly returned:

```

Reward = 0

```

confirming that it validates output correctness rather than simply checking whether a file exists.

---

# Technologies

- Python
- Docker
- Pytest
- JSON
- Regular Expressions

---

# Running

Build

```bash
docker build -t log-report .
```

Run

```bash
harbor run -p . --agent oracle
```

No-op Agent

```bash
harbor run -p . --agent nop
```

---

# License

This repository is intended for educational and software engineering evaluation purposes.
