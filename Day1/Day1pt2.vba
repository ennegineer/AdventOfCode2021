Attribute VB_Name = "Module1"
Sub nxt():

Count = 0
StartRow = 2

    'find the last row
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    For i = 2 To lastRow
        NextSet = StartRow + 1
        LastSet = StartRow + 2
        For x = StartRow To LastSet
            Total = Total + Cells(x, 1).Value
            Range("B" & LastSet).Value = Total
        Next x
        StartRow = StartRow + 1
        Total = 0
    Next i
    
    For j = 4 To lastRow
        If Cells(j + 1, 2).Value > Cells(j, 2).Value Then
        Cells(j + 1, 3).Value = "increased"
        Count = Count + 1
        End If
    Next j
    
    Range("D2").Value = Count
End Sub

