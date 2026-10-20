# Writes new TC ids + Round 1 results (Result M, Test person N, Test date O, Bug_ID P, Remark Q) into sheet Customers and
# updates the "TC liên quan" column (E) of the questions sheet. usage: apply-writeback.ps1 <workbook.xlsx> <writeback.json>
param([string]$Book, [string]$PlanPath)
$ErrorActionPreference = 'Stop'
$p = Get-Content -Raw -Encoding UTF8 $PlanPath | ConvertFrom-Json
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false
try {
  $wb = $xl.Workbooks.Open($Book); $ws = $wb.Worksheets.Item([string]$p.sheet); $n = 0
  foreach ($r in $p.rows) {
    $row = [int]$r.row
    if ([string]$ws.Cells.Item($row, 7).Value2 -ne [string]$r.old) { throw "row $row holds '$($ws.Cells.Item($row, 7).Value2)', expected $($r.old)" }
    $ws.Cells.Item($row, 7).Value2 = [string]$r.tc
    if ([string]$r.result -ne '') {
      $ws.Cells.Item($row, 13).Value2 = [string]$r.result
      $ws.Cells.Item($row, 14).Value2 = [string]$p.tester
      $ws.Cells.Item($row, 15).NumberFormat = '@'; $ws.Cells.Item($row, 15).Value2 = [string]$p.date
      $ws.Cells.Item($row, 16).Value2 = [string]$r.bug
      $ws.Cells.Item($row, 17).Value2 = [string]$r.remark
      $ws.Cells.Item($row, 17).WrapText = $true
    }
    $n++
  }
  foreach ($e in $p.stepEdits) { if ([string]$ws.Cells.Item([int]$e.row, 7).Value2 -ne [string]$e.tc) { throw "step edit row mismatch $($e.tc)" }; $ws.Cells.Item([int]$e.row, 10).Value2 = [string]$e.steps; $ws.Cells.Item([int]$e.row, 11).Value2 = [string]$e.expected }
  "Customers: {0} rows written, {1} case texts fixed" -f $n, @($p.stepEdits).Count
  $q = $wb.Worksheets.Item([string]$p.questionSheet); $last = $q.Cells.Item($q.Rows.Count, 1).End(-4162).Row; $u = 0
  for ($r = 2; $r -le $last; $r++) {
    $id = [string]$q.Cells.Item($r, 1).Value2
    $ref = $p.questionRefs.PSObject.Properties[$id]
    if ($ref) { $q.Cells.Item($r, 5).Value2 = [string]$ref.Value; $u++ }
  }
  "questions updated: $u"
  $xl.CalculateFull(); $wb.Save(); $wb.Close($true)
} finally { $xl.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null }
