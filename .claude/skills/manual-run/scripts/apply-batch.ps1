# Batch update of sheet Customers: new remarks for Failed cases, TC_011 -> Passed, TC_060 expected, new case TC_100 at the end.
# usage: apply-batch.ps1 <workbook.xlsx> <remarks-v2.json> <update-batch.json>
param([string]$Book, [string]$RemarksPath, [string]$BatchPath)
$ErrorActionPreference = 'Stop'
$rm = Get-Content -Raw -Encoding UTF8 $RemarksPath | ConvertFrom-Json
$b = Get-Content -Raw -Encoding UTF8 $BatchPath | ConvertFrom-Json
$tester = 'Auto (Claude) · localhost main b5cb690'; $date = '19/10/2026'
$xl = New-Object -ComObject Excel.Application; $xl.Visible = $false; $xl.DisplayAlerts = $false
try {
  $wb = $xl.Workbooks.Open($Book); $ws = $wb.Worksheets.Item('Customers')
  function RowOf([string]$tc) { $f = $ws.Range('G13:G2000').Find($tc, [Type]::Missing, -4163, 1); if ($f) { $f.Row } else { throw "not found $tc" } }
  $n = 0
  foreach ($p in $rm.PSObject.Properties) { $r = RowOf $p.Name; $ws.Cells.Item($r, 17).Value2 = [string]$p.Value; $ws.Cells.Item($r, 17).WrapText = $true; $n++ }
  "remarks rewritten: $n"
  $r = RowOf $b.tc011.tc; $ws.Cells.Item($r, 13).Value2 = 'Passed'; $ws.Cells.Item($r, 16).Value2 = ''; $ws.Cells.Item($r, 17).Value2 = [string]$b.tc011.remark
  "TC_011 -> Passed (row $r)"
  $r = RowOf 'TC_060'; $ws.Cells.Item($r, 11).Value2 = [string]$b.tc060Expected; "TC_060 expected updated (row $r)"
  # TC_100 appended after the last case, formats copied from the row above
  $last = $ws.Cells.Item($ws.Rows.Count, 7).End(-4162).Row
  if ([string]$ws.Range('G13:G2000').Find('TC_100', [Type]::Missing, -4163, 1) -ne '') { throw 'TC_100 already exists' }
  $new = $last + 1
  $ws.Rows.Item($last).Copy() | Out-Null; $ws.Rows.Item($new).PasteSpecial(-4122) | Out-Null
  [void][System.__ComObject].InvokeMember('CutCopyMode', [System.Reflection.BindingFlags]::SetProperty, $null, $xl, @($false))
  $c = $b.tc100
  $vals = @{ 1 = 100; 2 = $c.c1; 3 = $c.c2; 4 = $c.c3; 5 = $c.c4; 6 = $c.priority; 7 = $c.tc; 8 = $c.name; 9 = $c.pre; 10 = $c.steps; 11 = $c.expected; 13 = $c.result; 14 = $tester; 16 = $c.bug; 17 = $c.remark; 24 = $c.uc }
  foreach ($k in $vals.Keys) { if ($k -eq 1) { $ws.Cells.Item($new, 1).Value2 = [double]100 } else { $ws.Cells.Item($new, [int]$k).Value2 = [string]$vals[$k] } }
  $ws.Cells.Item($new, 15).NumberFormat = '@'; $ws.Cells.Item($new, 15).Value2 = $date
  $ws.Rows.Item($new).RowHeight = 80
  "TC_100 appended at row $new"
  $xl.CalculateFull(); $wb.Save(); $wb.Close($true)
} finally { $xl.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null }
