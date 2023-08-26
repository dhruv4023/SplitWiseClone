# Set the project directory and virtual environment name
$venvName = "venv"

# Check if the virtual environment folder exists
$venvExists = Test-Path ($venvName)

if (-not $venvExists) {
    # Create virtual environment if it doesn't exist
    Write-Host "Creating virtual environment..."
    python -m venv $venvName
}
Write-Host "Installing dependencies..."
python -m pip install -r "requirements.txt"
try {
    & venv\Scripts\Activate.ps1

    # Run your Django app (replace "myproject" with your actual project name)
    Write-Host "Running Django app..."
    python manage.py runserver

} catch {
    Write-Host "An error occurred: $($_.Exception.Message)"
    # Install dependencies from requirements.txt
}
