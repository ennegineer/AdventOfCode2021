Attribute VB_Name = "Module1"
Sub Day():

Count = 0
Row = 1

    'find the last row
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    For i = 2 To lastRow
        If Cells(i + 1, 1).Value > Cells(i, 1).Value Then
            Count = Count + 1
        End If
    Next i
    
    Range("C2").Value = Count
End Sub

