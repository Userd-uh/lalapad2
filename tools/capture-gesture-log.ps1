param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^COM[0-9]+$')]
    [string]$Port,
    [ValidateRange(1, 600)]
    [int]$Seconds = 30,
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
            if ($line -match 'GIN seq=') { $lines++ }
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
if ($lines -eq 0) {
    Write-Warning 'No gesture frames. Check the LEFT USB connection, diagnostic firmware and COM port.'
}
