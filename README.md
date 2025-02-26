# Security Scan GitHub Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Furkhanhash/github-action-security-scan)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Furkhanhash/github-action-security-scan/test.yml)

## 🚀 Description
This GitHub Action fetches **security vulnerabilities** from GitHub's **Code Scanning API** and returns counts by severity (`critical`, `high`, `medium`, `low`). It also generates a **JSON report** for high and critical severity issues.

## 🛠️ Usage

### **Basic Example**
```yaml
jobs:
  security_scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Run Security Scan
        id: security_scan
        uses: Furkhanhash/github-action-security-scan@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Output Results
        run: |
          echo "Critical Alerts: ${{ steps.security_scan.outputs.critical_count }}"
          echo "High Alerts: ${{ steps.security_scan.outputs.high_count }}"
          echo "Medium Alerts: ${{ steps.security_scan.outputs.medium_count }}"
          echo "Low Alerts: ${{ steps.security_scan.outputs.low_count }}"

      - name: Upload JSON Report
        uses: actions/upload-artifact@v4
        with:
          name: security_scan_report
          path: ${{ steps.security_scan.outputs.high_critical_alerts_json }}
