# Finishing pass after apply-cc.ps1: writes the classification labels into the top cell of each merged run of the new block
# and sets each case row's height from its text so nothing is cut. usage: fix-cc.ps1 <workbook.xlsx> <apply-cc.json>
param([string]$Book, [string]$PlanPath)
$ErrorActionPreference = 'Stop'
$p = Get-Content -Raw -Encoding UTF8 $PlanPath | ConvertFrom-Json
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false
try {
  $wb = $xl.Workbooks.Open($Book); $ws = $wb.Worksheets.Item('Customers')
  $rows = @{}; foreach ($b in $p.block) { $rows[$b.tc] = $b }; foreach ($b in $p.invite) { $rows[$b.tc] = $b }
  $width = @{}; foreach ($c in 2..11) { $width[$c] = [Math]::Max(4, [double]$ws.Columns.Item($c).ColumnWidth * 1.1) }
  $last = $ws.Cells.Item($ws.Rows.Count, 7).End(-4162).Row; $fixed = 0
  for ($r = 13; $r -le $last; $r++) {
    $tc = [string]$ws.Cells.Item($r, 7).Value2
    if (-not $rows.ContainsKey($tc)) { continue }
    $d = $rows[$tc]
    $labels = @{ 2 = $d.c1; 3 = $d.c2; 4 = $d.c3; 5 = $d.c4 }
    foreach ($c in 2..5) { $m = $ws.Cells.Item($r, $c).MergeArea; if ($m.Row -eq $r) { $m.Cells.Item(1, 1).Value2 = [string]$labels[$c] } }
    # height: the tallest of the unmerged text cells (E..K), ~13.5 pt per wrapped line
    $lines = 1
    foreach ($c in 5..11) {
      $t = [string]$ws.Cells.Item($r, $c).Value2; if ($t -eq '') { continue }
      $n = 0; foreach ($part in $t -split "`n") { $n += [Math]::Max(1, [Math]::Ceiling($part.Length / $width[$c])) }
      if ($n -gt $lines) { $lines = $n }
    }
    $ws.Rows.Item($r).RowHeight = [Math]::Min(409, [Math]::Max(30, $lines * 13.5 + 6)); $fixed++
  }
  "labels and heights set on {0} rows" -f $fixed
  $wb.Save(); $wb.Close($true)
} finally { $xl.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null }
