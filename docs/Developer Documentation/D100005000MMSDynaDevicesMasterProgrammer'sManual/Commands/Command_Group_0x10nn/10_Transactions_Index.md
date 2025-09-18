---
title: Command Group 0x10nn
layout: home
parent: Developer Documentation
nav_order: 
---
<style>
.pill{display:inline-block;padding:.18rem .5rem;border-radius:999px;font-size:.78rem;
  font-weight:600;line-height:1;vertical-align:middle;border:1px solid rgba(0,0,0,.06)}
.pill-blue{background:#f5f9ff;border-color:#dbeafe;color:#1d4ed8}
.pill-red{background:#fff7f7;border-color:#fecaca;color:#b91c1c}
.pill-slate{background:#f8fafc;border-color:#e2e8f0;color:#334155}
.callout{border:1px solid #e5e7eb;border-left-width:4px;border-radius:8px;background:#fafafa;
  padding:.75rem 1rem;margin:1rem 0}
.callout small{display:block;color:#475569;margin-bottom:.25rem;font-weight:600;letter-spacing:.02em;text-transform:uppercase}
.callout p{margin:.25rem 0}
.is-info{border-left-color:#3b82f6;background:#f5f9ff}
.is-success{border-left-color:#10b981;background:#f0fdf4}
.is-warn{border-left-color:#f59e0b;background:#fffbeb}
.code-box{position:relative;margin:1rem 0}
.code-box[data-label]::before{
  content:attr(data-label);
  position:absolute;top:-10px;left:10px;
  background:#fff;padding:0 .4rem;font-size:.75rem;font-weight:600;color:#475569;
  border:1px solid #e5e7eb;border-radius:6px
}
.code-box pre{margin-top:.6rem}
.markdown table{border:1px solid #e5e7eb;border-radius:8px;overflow:hidden}
.markdown table thead th{position:sticky;top:0;background:#f8fafc;z-index:1}
.markdown table tbody tr:hover td{background:#f9fafb}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:1rem 0}
@media (max-width: 860px){.twocol{grid-template-columns:1fr}}
.col{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff}
.mono td,.mono th{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9rem}
table { width: 100%; border-collapse: collapse; margin: 1em 0; }
table th, table td { border: 1px solid #ddd; padding: 6px 10px; }
table th { background: #f8f9fa; font-weight: bold; }
table tr:nth-child(even) { background: #fdfdfd; }
pre code { display: block; background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px;
  padding: 10px; font-size: 0.9rem; line-height: 1.4; overflow-x: auto; }
</style>


# Command Group 0x10nn — Transactions

This section defines the **Transactions** command family. Each command page includes: **Sequence**, **Applicability**, **Syntax**, **Examples** (with payload + full-framed APDUs), **Status/Errors**, and **Notes**.

- 0x1001 — Start Transaction
- 0x1002 — Continue Transaction
- 0x1003 — Finalize Transaction
- 0x1004 — Resume Transaction
- 0x1008 — Cancel Transaction
- 0x1009 — Close / Clear Transaction
- 0x1014 — Get Transaction Status
- 0x1041 — Set Payment Parameters
- 0x1042 — Get Payment Parameters
