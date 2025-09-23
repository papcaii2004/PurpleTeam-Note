param (
    [Parameter(Mandatory=$true)] [string] $InputFile,
    [Parameter(Mandatory=$true)] [string] $OutputFile
)

# Đọc nội dung file PS script (UTF8)
$content = Get-Content -Path $InputFile -Raw -Encoding UTF8

# Chuyển nội dung thành bytes UTF-16LE bytes
$bytes = [System.Text.Encoding]::Unicode.GetBytes($content)

# Mã hóa bytes thành base64 string
$base64 = [Convert]::ToBase64String($bytes)

# Ghi base64 ra file output (text)
Set-Content -Path $OutputFile -Value $base64 -Encoding ASCII

Write-Host "Encoded $InputFile to base64 and saved to $OutputFile"
