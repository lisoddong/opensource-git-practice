param([switch]$IncludeJava)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$py = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
if (!(Test-Path $py)) { throw 'Create .venv and install Python requirements first.' }
foreach ($lab in @('01-unit','02-integration')) {
    & $py -m pytest -v "python/$lab"
    if ($LASTEXITCODE -ne 0) { throw "Python $lab failed" }
}
if ($IncludeJava) {
    $jdk = Get-ChildItem '.tools/jdk' -Directory -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($jdk) { $env:JAVA_HOME = $jdk.FullName }
    $env:GRADLE_USER_HOME = Join-Path $PSScriptRoot '.tools/gradle-home'
    foreach ($lab in @('01-unit','02-integration')) {
        & '.tools/gradle-9.7.1/bin/gradle.bat' -p "java/$lab" clean test --no-daemon --console=plain
        if ($LASTEXITCODE -ne 0) { throw "Java $lab failed" }
    }
}
