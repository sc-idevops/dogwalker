write-host "W: You should already have created and edited an ENV file before proceeding! Waiting 10 seconds in case you need to abort."
# Start-Sleep -Seconds 10
docker compose build
docker compose up -d