# Rebuilds the "Create customer" block of sheet Customers (Bước 1 · Account / Bước 2 · Invite initial Customer Admin / Sau khi tạo),
# moves TC_038/TC_043 to the invite group, appends new questions, and rebuilds the Customers part of Test_Report.
# usage: apply-cc.ps1 <workbook.xlsx> <apply-cc.json>   (edits the workbook in place; make a backup first)
param([string]$Book, [string]$PlanPath)
$ErrorActionPreference = 'Stop'
$p = Get-Content -Raw -Encoding UTF8 $PlanPath | ConvertFrom-Json
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false; $xl.ScreenUpdating = $false
try {
  $wb = $xl.Workbooks.Open($Book); $xl.Calculation = -4135
  $ws = $wb.Worksheets.Item('Customers')
  function ClearClip() { [void][System.__ComObject].InvokeMember("CutCopyMode", [System.Reflection.BindingFlags]::SetProperty, $null, $xl, @($false)) }
  function RowOf($sheet, [string]$tc) { $f = $sheet.Range('G1:G2000').Find($tc, [Type]::Missing, -4163, 1); if ($f) { $f.Row } else { 0 } }
  function LastCaseRow($sheet) { $sheet.Cells.Item($sheet.Rows.Count, 7).End(-4162).Row }
  function SetRow($sheet, [int]$r, $c) {
    $vals = @{ 2 = $c.c1; 3 = $c.c2; 4 = $c.c3; 5 = $c.c4; 6 = $c.priority; 7 = $c.tc; 8 = $c.name; 9 = $c.pre; 10 = $c.steps; 11 = $c.expected; 23 = $c.oq; 24 = $c.uc }
    foreach ($k in $vals.Keys) { $sheet.Cells.Item($r, [int]$k).Value2 = [string]$vals[$k] }
  }
  function MergeRuns($sheet, [int]$top, [int]$bottom, [int]$col, [int[]]$keyCols) {
    $start = $top
    for ($r = $top + 1; $r -le $bottom + 1; $r++) {
      $same = $r -le $bottom
      if ($same) { foreach ($kc in $keyCols) { if ([string]$sheet.Cells.Item($r, $kc).Value2 -ne [string]$sheet.Cells.Item($start, $kc).Value2) { $same = $false } } }
      if (-not $same) {
        if ($r - 1 -gt $start) {
          $v = $sheet.Cells.Item($start, $col).Value2
          for ($q = $start + 1; $q -le $r - 1; $q++) { $sheet.Cells.Item($q, $col).Value2 = $null }
          $rg = $sheet.Range($sheet.Cells.Item($start, $col), $sheet.Cells.Item($r - 1, $col)); $rg.Merge() | Out-Null
          $rg.Value2 = $v; $rg.VerticalAlignment = -4108; $rg.WrapText = $true
        }
        $start = $r
      }
    }
  }

  # 1. template row for formats (a plain, unmerged case row)
  $tplTc = 'TC_055'
  # 2. delete the old rows of every case that is rebuilt or moved (bottom-up, keeping merged labels)
  $rows = @(); foreach ($tc in $p.removeTcs) { $r = RowOf $ws $tc; if ($r -gt 0) { $rows += $r } }
  foreach ($r in ($rows | Sort-Object -Descending)) {
    $keep = @{}
    for ($c = 1; $c -le 6; $c++) { $cell = $ws.Cells.Item($r, $c); if ($cell.MergeCells) { $a = $cell.MergeArea; if ($a.Row -eq $r -and $a.Rows.Count -gt 1) { $keep[$c] = $cell.Value2 } } }
    $ws.Rows.Item($r).Delete() | Out-Null
    foreach ($c in $keep.Keys) { $ws.Cells.Item($r, $c).Value2 = $keep[$c] }
  }
  "deleted {0} old rows" -f $rows.Count

  # 3. insert the new block above the first "Chi tiết khách hàng" case (TC_024)
  $at = RowOf $ws 'TC_024'; $n = $p.block.Count
  $ws.Range("A$($at):A$($at + $n - 1)").EntireRow.Insert(-4121) | Out-Null
  $blk = $ws.Range("A$($at):X$($at + $n - 1)")
  $blk.UnMerge()
  $tpl = RowOf $ws $tplTc
  $ws.Range("A$($tpl):X$($tpl)").Copy() | Out-Null; $blk.PasteSpecial(-4122) | Out-Null; ClearClip
  for ($i = 0; $i -lt $n; $i++) { SetRow $ws ($at + $i) $p.block[$i] }
  $last = $at + $n - 1
  MergeRuns $ws $at $last 2 @(2)
  MergeRuns $ws $at $last 3 @(2, 3)
  MergeRuns $ws $at $last 4 @(2, 3, 4)
  $ws.Range("H$($at):K$($last)").Rows.AutoFit() | Out-Null
  "inserted block rows {0}-{1}" -f $at, $last

  # 4. TC_038 / TC_043 into the invite group, above TC_067
  $at2 = RowOf $ws $p.inviteBeforeTc; $m = $p.invite.Count
  $ws.Range("A$($at2):A$($at2 + $m - 1)").EntireRow.Insert(-4121) | Out-Null
  $tpl = RowOf $ws $tplTc
  $ws.Range("A$($tpl):X$($tpl)").Copy() | Out-Null; $ws.Range("A$($at2):X$($at2 + $m - 1)").PasteSpecial(-4122) | Out-Null; ClearClip
  for ($i = 0; $i -lt $m; $i++) { SetRow $ws ($at2 + $i) $p.invite[$i] }
  $ws.Range("H$($at2):K$($at2 + $m - 1)").Rows.AutoFit() | Out-Null
  "moved {0} invite rows to {1}" -f $m, $at2

  # 5. renumber No.
  $lastCase = LastCaseRow $ws; $k = 0
  for ($r = 13; $r -le $lastCase; $r++) { if ([string]$ws.Cells.Item($r, 7).Value2 -ne '') { $k++; $ws.Cells.Item($r, 1).Value2 = [double]$k } }
  "Customers now {0} cases" -f $k

  # 6. new questions at the end of the questions sheet
  $q = $wb.Worksheets.Item([string]$p.questionSheet)
  $ql = $q.Cells.Item($q.Rows.Count, 1).End(-4162).Row
  foreach ($x in $p.questions) {
    $ql++
    $q.Rows.Item($ql - 1).Copy() | Out-Null; $q.Rows.Item($ql).PasteSpecial(-4122) | Out-Null; ClearClip; ClearClip
    $vals = @($x.id, 'Customers', $x.question, $x.basis, $x.tcs, $x.proposal, $x.level, $x.status)
    for ($c = 0; $c -lt $vals.Count; $c++) { $q.Cells.Item($ql, $c + 1).Value2 = [string]$vals[$c] }
  }
  $q.Range("A$($ql - $p.questions.Count + 1):H$($ql)").Rows.AutoFit() | Out-Null
  "added {0} questions" -f $p.questions.Count

  # 7. Test_Report: one row per run of (Classification I, II) over the whole Customers sheet
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

  $xl.Calculation = -4105; $xl.CalculateFull()
  $wb.Save(); $wb.Close($true)
} finally { $xl.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null }
