from mcp.server.fastmcp import FastMCP
from app import getliveTemp
import requests

# Initialize MCP server
mcp = FastMCP("weather-forecast-mcp")



@mcp.tool()
async def get_word_definition(word: str) -> dict:
    """
    Get the definition of a word using dictionaryapi.dev.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Word not found or API error (status {response.status_code})"}

if __name__ == "__main__":
    mcp.run(transport="stdio")