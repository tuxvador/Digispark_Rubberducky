$i=1
$files = (Get-ChildItem -Path .\scripts\ -File).Name
$basename = (Get-ChildItem -Path .\scripts\ -File).BaseName
$name = $files | % {"$i) $_$($i++)"}
$name
do{
    $choice=Read-Host 'Chosse file to convert to arduino digispark compatible script '
    $value=$choice -as [Int]
    $ok=$value -ne $nul
    if ($(-not($value -gt $files.Length)) -and $(-not($value -lt 1))) {
        $choice=$files[$value-1]
        Write-Host $choice
        Write-Host $value
        iex("java -jar .\exes\duckencoder.jar -i .\scripts\$choice -o .\bin\$($basename[$value-1]).bin -l fr")
        if( -not $(Test-Path .\ino\$($basename[$value-1]))) {
            iex("mkdir .\ino\$($basename[$value-1])") | Out-Null
        }
        iex("python .\exes\duck2spark.py -i .\bin\$($basename[$value-1]).bin -l 1 -o .\ino\$($basename[$value-1])\$($basename[$value-1]).ino")
    }
    else{
    $ok = $nul
    Write-Host "You Must enter a number between 1 and $($list.Length)"
    }
}until($ok)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force