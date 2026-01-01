from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

# Create the FastMCP instance
mcp = FastMCP("python-mcp-demo")

@mcp.tool()
async def add_numbers(a: float, b: float) -> TextContent:
    """
    Add two numbers and return the result.
    """
    result = a + b
    return TextContent(type="text", text=f"Result: {result}")

@mcp.tool()
async def echo_message(message: str) -> TextContent:
    """
    Echo a message and return metadata about it.
    """
    length = len(message)
    upper = message.upper()
    text = (
        f"Echoed: {message}\n"
        f"Length: {length}\n"
        f"UpperCase: {upper}\n"
    )
    return TextContent(type="text", text=text)

if __name__ == "__main__":
    # For Claude Desktop / ChatGPT MCP hosts (stdio transport):
    mcp.run(transport="stdio")

    # For local HTTP testing instead, you could use:
    # mcp.run(transport="streamable-http")