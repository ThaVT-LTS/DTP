param([string]$Book)
$ErrorActionPreference = "Stop"
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false
try { $wb = $xl.Workbooks.Open($Book); $ws = $wb.Worksheets.Item("Customers")
  function ClearClip() { }
  $lastCase = $ws.Cells.Item($ws.Rows.Count, 7).End(-4162).Row
  $groups = @(); $start = 13; $prev = $null
  for ($r = 13; $r -le $lastCase + 1; $r++) {
    $key = if ($r -le $lastCase) { [string]$ws.Cells.Item($r, 2).MergeArea.Cells.Item(1, 1).Value2 + '|' + [string]$ws.Cells.Item($r, 3).MergeArea.Cells.Item(1, 1).Value2 } else { '#end' }
    if ($null -ne $prev -and $key -ne $prev) { $groups += , @($prev, $start, ($r - 1)); $start = $r }
    $prev = $key
  }
  ClearClip
  $tr = $wb.Worksheets.Item('Test_Report'); $trLast = $tr.UsedRange.Row + $tr.UsedRange.Rows.Count
  # drop the separate "Case bổ sung" row of Customers (now covered by the groups)
  for ($r = $trLast; $r -ge 4; $r--) { if ([string]$tr.Cells.Item($r, 2).MergeArea.Cells.Item(1, 1).Value2 -eq 'Customers' -and [string]$tr.Cells.Item($r, 3).Value2 -like 'Case b*') { $tr.Rows.Item($r).Delete() | Out-Null } }
  $first = 0; $total = 0
  for ($r = 4; $r -le $trLast; $r++) { if ([string]$tr.Cells.Item($r, 2).Value2 -eq 'Customers') { $first = $r; break } }
  for ($r = $first; $r -le $trLast; $r++) { if ([string]$tr.Cells.Item($r, 3).Value2 -eq 'Total') { $total = $r; break } }
  if ($first -eq 0 -or $total -eq 0) { throw "Customers section not found ($first/$total)" }
  $have = $total - $first; $need = $groups.Count
  if ($need -gt $have) { for ($i = 0; $i -lt $need - $have; $i++) { $tr.Rows.Item($total).Insert(-4121) | Out-Null; $total++ } }
  if ($need -lt $have) { for ($i = 0; $i -lt $have - $need; $i++) { $tr.Rows.Item($total - 1).Delete() | Out-Null; $total-- } }
  for ($i = 0; $i -lt $need; $i++) {
    $r = $first + $i; $g = $groups[$i]; $lab = $g[0].Split('|'); $a = $g[1]; $b = $g[2]
    $tr.Cells.Item($r, 3).Value2 = $lab[0]; $tr.Cells.Item($r, 4).Value2 = $lab[1]
    $tr.Cells.Item($r, 5).Formula = "=F$r/G$r"; $tr.Cells.Item($r, 6).Formula = "=SUM(H$($r):L$($r))"; $tr.Cells.Item($r, 7).Formula = "=SUM(H$($r):M$($r))"
    $cols = 'H', 'I', 'J', 'K', 'L'; for ($j = 0; $j -lt 5; $j++) { $tr.Cells.Item($r, 8 + $j).Formula = "=COUNTIF(Customers!`$M`$$($a):`$M`$$($b),$($cols[$j])`$3)" }
    $tr.Cells.Item($r, 13).Formula = "=COUNTA(Customers!`$G`$$($a):`$G`$$($b))-SUM(H$($r):L$($r))"
    $tr.Cells.Item($r, 14).Formula = "=O$r/P$r"; $tr.Cells.Item($r, 15).Formula = "=SUM(Q$($r):U$($r))"; $tr.Cells.Item($r, 16).Formula = "=SUM(Q$($r):V$($r))"
    $cols = 'Q', 'R', 'S', 'T', 'U'; for ($j = 0; $j -lt 5; $j++) { $tr.Cells.Item($r, 17 + $j).Formula = "=COUNTIF(Customers!`$R`$$($a):`$R`$$($b),$($cols[$j])`$3)" }
    $tr.Cells.Item($r, 22).Formula = "=COUNTA(Customers!`$G`$$($a):`$G`$$($b))-SUM(Q$($r):U$($r))"
  }
  foreach ($c in 8..13 + 17..22) { $L = [char](64 + $c); $tr.Cells.Item($total, $c).Formula = "=SUM($L$($first):$L$($total - 1))" }
  "Test_Report Customers: {0} group rows ({1}-{2}), total row {3}" -f $need, $first, ($total - 1), $total

  "C252=" + $tr.Cells.Item(252,3).Value2 + " D252=" + $tr.Cells.Item(252,4).Value2 + " C260=" + $tr.Cells.Item(260,3).Value2
  $wb.Save(); $wb.Close($true) } finally { $xl.Quit() }
