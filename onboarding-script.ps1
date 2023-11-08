# Enable automatic screen lock
$lockTimeout = 120
$RegPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$RegName = "InactivityTimeoutSec"
$lockTimeoutValue = New-Object -TypeName PSObject -Property @{
    Property = $RegName
    Value = $lockTimeout
}

if (Test-Path $RegPath) {
    Set-ItemProperty -Path $RegPath -Name $RegName -Value $lockTimeout
} else {
    New-ItemProperty -Path $RegPath -Name $RegName -Value $lockTimeout
}

# Check if antivirus software is installed and running
$antivirusSoftware = Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct

if ($antivirusSoftware) {
    Write-Host "Antivirus software is installed and running:"
    $antivirusSoftware | ForEach-Object {
        Write-Host " - $_.displayName"
    }
} else {
    Write-Host "No antivirus software detected."
}

# Check if automatic updates are enabled, and enable if not
$automaticUpdates = Get-WmiObject -Class Win32_ComputerSystem
if ($automaticUpdates.AutomaticUpdateNotificationsSetting -ne 4) {
    Write-Host "Enabling automatic OS updates..."
    $automaticUpdates.AutomaticUpdateNotificationsSetting = 4
    $automaticUpdates.Put()
    Write-Host "Automatic OS updates are now enabled."
} else {
    Write-Host "Automatic OS updates are already enabled."
}