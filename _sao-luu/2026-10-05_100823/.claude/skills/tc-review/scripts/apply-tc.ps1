# Applies apply-plan.json to a COPY of the test case workbook with Excel itself, so formulas (Test_Report COUNTIF ranges)
# and merged classification cells are adjusted by Excel. usage: apply-tc.ps1 <src.xlsx> <dst.xlsx> <plan.json>
param([string]$Src, [string]$Dst, [string]$PlanPath)
$ErrorActionPreference = 'Stop'
$plan = Get-Content -Raw -Encoding UTF8 $PlanPath | ConvertFrom-Json
Copy-Item $Src $Dst -Force
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false; $xl.ScreenUpdating = $false

try {
  $wb = $xl.Workbooks.Open($Dst); $xl.Calculation = -4135  # manual while editing
  function Remove-RowKeepMerges($ws, [int]$r) {
    # if this row is the top of a vertical merge in the classification columns, move the value down first
    $keep = @{}
    for ($c = 1; $c -le 6; $c++) {
      $cell = $ws.Cells.Item($r, $c)
      if ($cell.MergeCells) { $area = $cell.MergeArea; if ($area.Row -eq $r -and $area.Rows.Count -gt 1) { $keep[$c] = $cell.Value2 } }
    }
    $ws.Rows.Item($r).Delete() | Out-Null
    foreach ($c in $keep.Keys) { $ws.Cells.Item($r, $c).Value2 = $keep[$c] }
  }
  foreach ($s in $plan.sheets) {
    $ws = $wb.Worksheets.Item($s.name)
    foreach ($e in $s.cells) {
      $cell = $ws.Cells.Item([int]$e.row, [int]$e.col)
      if ([int]$e.col -le 5 -and $cell.MergeCells) { "  SKIP merged classification {0}!R{1}C{2} -> '{3}'" -f $s.name, $e.row, $e.col, $e.value; continue }
      $cell.Value2 = [string]$e.value
    }
    foreach ($r in $s.deletes) { Remove-RowKeepMerges $ws ([int]$r) }
    # renumber column A (No.) for every case row
    $last = $ws.Cells.Item($ws.Rows.Count, 7).End(-4162).Row; $n = 0
    for ($r = 13; $r -le $last; $r++) { if ([string]$ws.Cells.Item($r, 7).Value2 -ne '') { $n++; $ws.Cells.Item($r, 1).Value2 = [double]$n } }
    "{0}: {1} edits cells, {2} rows deleted, {3} cases now" -f $s.name, $s.cells.Count, $s.deletes.Count, $n
  }
  $q = $wb.Worksheets.Item([string]$plan.questionSheet)
  foreach ($r in $plan.questionDeletes) { $q.Rows.Item([int]$r).Delete() | Out-Null }
  "Questions sheet: {0} closed questions deleted" -f $plan.questionDeletes.Count
  # Test_Report rows whose whole group was deleted now show #REF! — remove them
  $xl.Calculation = -4105; $xl.CalculateFull()
  $tr = $wb.Worksheets.Item('Test_Report'); $lastTr = $tr.UsedRange.Rows.Count + $tr.UsedRange.Row; $removed = 0
  for ($r = $lastTr; $r -ge 4; $r--) {
    $f = [string]$tr.Cells.Item($r, 8).Formula
    if ($f -match '#REF!') { $tr.Rows.Item($r).Delete() | Out-Null; $removed++ }
  }
  "Test_Report: {0} group rows with #REF! removed" -f $removed
  $xl.CalculateFull()
  $wb.Save(); $wb.Close($true)
} finally { $xl.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null }
