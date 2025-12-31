import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContext

server = Server("python-mcp-demp")

@server.tool()
async def add_numbers(a: float, b: float) -> TextContent:
    """
    Add two numbers and return the result
    """
    result = a + b
    return TextContent(text=f"Result: {result}")

@server.tool()
async def echo_message(message: str) -> TextContent:
    """
    Echo a message and return metadata about it.
    """
    length = len(message)
    upper = message.upper()
    text =  (
        f"Echoed: {message}\n"
        f"Length: {length}\n"
        f"UpperCase: {upper}\n"
    )
    return TextContent(text=text)

async def main() -> None:
    """
    Run the MCP server over stdin/stdout.
    """
    await server.run_stdio()

if __name__ == "-__main__":
    asyncio.run(main())