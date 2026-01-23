
#Need to add mcp configuration here
~/Library/Application Support/Claude/claude_desktop_config.json

#This is what needs to be added
{
  "mcpServers": {
    "python-mcp-demo": {
      "command": "python3",
      "args": ["server.py"],
      "env": {
        "PYTHONUNBUFFERED": "1"
      },
      "workingDirectory": "/Users/troymcgahey/Projects/Python/python-mcp-server"
    }
  }
}

#activate python
source .venv/bin/activate

#to kill and exit the python virtual environment
deactivate

#to run App
python3 server.py