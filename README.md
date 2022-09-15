# deploy-to-cms

## Usage
```
python3 main.py sample.sh --port 5000
```

Add webhook in `https://github.com/your-name/your-repo/settings/hooks/new`
- Payload URL: `https://example.com:5000` or your url
- Content type: application/json
- Which events would you like to trigger this webhook?: Just the push event.
