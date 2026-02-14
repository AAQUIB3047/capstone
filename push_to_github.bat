@echo off
echo This script will help you push your project to GitHub
echo.
echo First, you need to create a Personal Access Token on GitHub:
echo 1. Go to https://github.com/settings/tokens
echo 2. Click "Generate new token (classic)"
echo 3. Select scopes: repo (full control)
echo 4. Generate token and copy it
echo.
set /p TOKEN="Enter your GitHub Personal Access Token: "

echo.
echo Creating repository...
curl -X POST -H "Authorization: token %TOKEN%" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d "{\"name\":\"capstone\",\"description\":\"Capstone Project\",\"private\":false}"

echo.
echo Uploading README.md...
powershell -Command "$content = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes('capstone-main\README.md')); $body = @{message='Initial commit - Add README'; content=$content} | ConvertTo-Json; curl -X PUT -H 'Authorization: token %TOKEN%' -H 'Accept: application/vnd.github.v3+json' https://api.github.com/repos/AAQUIB3047/capstone/contents/README.md -d $body"

echo.
echo Done! Your project has been pushed to https://github.com/AAQUIB3047/capstone
pause
