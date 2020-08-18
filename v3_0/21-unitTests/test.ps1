$Application = New-Object -ComObject powerpoint.application
$Application.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$ThemePath = "C:\Users\Theme.potx"
$PPTXPath = "C:\Users\acbart\Projects\cisc108\cisc108-python-f19-bart\pages\slides\21-unitTests\Unit Tests.pptx"
$SavePath = "C:\Users\acbart\Projects\cisc108\cisc108-python-f19-bart\pages\slides\21-unitTests\2 - Unit Tests.mp4"

$Presentation = $Application.Presentations.Open($PPTXPath)
#--Applies a theme for the slides
#--$Presentation.ApplyTemplate($ThemePath)
#--Saves as a Video
$Presentation.SaveAs($SavePath, 39)
#$Presentation.Close()