param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^COM[0-9]+$')]
    [string]$Port,
    [ValidateRange(1, 600)]
    [int]$Seconds = 30,
    [ValidateRange(0, 20)]
    [int]$ExpectedReleases = 0,
    [string]$OutputPath = (Join-Path $PSScriptRoot ("gesture-{0}.log" -f (Get-Date -Format 'yyyyMMdd-HHmmss')))
)
$ErrorActionPreference = 'Stop'
$serial = [System.IO.Ports.SerialPort]::new($Port, 115200)
$serial.DtrEnable = $true
$serial.ReadTimeout = 200
$serial.ReadBufferSize = 65536
$serial.NewLine = "`n"
$writer = $null
$stream = $null
$lines = 0
$lastFingerCount = 0
$releases = 0
try {
    # CreateNew refuses to overwrite an earlier capture.
    $stream = [System.IO.File]::Open([IO.Path]::GetFullPath($OutputPath),
        [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::Read)
    $writer = [System.IO.StreamWriter]::new($stream, [Text.UTF8Encoding]::new($false))
    $writer.AutoFlush = $true
    $serial.Open()
    Write-Host 'Keep all fingers OFF the pad. Clearing buffered old logs for 2 seconds...'
    $drainTimer = [Diagnostics.Stopwatch]::StartNew()
    while ($drainTimer.Elapsed.TotalSeconds -lt 2) {
        $null = $serial.ReadExisting()
        [Threading.Thread]::Sleep(10)
    }
    $serial.DiscardInBuffer()
    $writer.WriteLine("# Capture started: $([DateTimeOffset]::Now.ToString('o')); port=$Port; seconds=$Seconds")
    Write-Host "Recording $Port for $Seconds seconds. Perform the gesture now."
    $timer = [Diagnostics.Stopwatch]::StartNew()
    while ($timer.Elapsed.TotalSeconds -lt $Seconds) {
        try {
            $line = $serial.ReadLine()
            $writer.WriteLine($line.TrimEnd("`r"))
            if ($line -match '\bGIN seq=(\d+) t=(\d+) fc=(\d+) ') {
                $lines++
                $sequence = $Matches[1]
                $deviceTime = $Matches[2]
                $fingerCount = [int]$Matches[3]
                if ($fingerCount -eq 0 -and $lastFingerCount -gt 0) {
                    $releases++
                    Write-Host "ALL FINGERS RELEASED: $releases (seq=$sequence, t=$deviceTime). Wait 2 seconds before the next trial."
                }
                $lastFingerCount = $fingerCount
            }
        } catch [TimeoutException] {
            # No frame while idle is expected.
        }
    }
    $writer.WriteLine("# Capture ended: $([DateTimeOffset]::Now.ToString('o')); GIN frames=$lines")
} finally {
    $serial.Dispose()
    if ($null -ne $writer) { $writer.Dispose() }
    if ($null -ne $stream) { $stream.Dispose() }
}
Write-Host "Saved $lines gesture frames: $([IO.Path]::GetFullPath($OutputPath))"
Write-Host "Observed full releases: $releases"
if ($ExpectedReleases -gt 0 -and $releases -ne $ExpectedReleases) {
    Write-Warning "Expected $ExpectedReleases releases but observed $releases. Do not treat this as $ExpectedReleases independent trials."
}
if ($lines -eq 0) {
    Write-Warning 'No gesture frames. Check the LEFT USB connection, diagnostic firmware and COM port.'
}
