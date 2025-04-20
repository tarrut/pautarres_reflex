# Current Weather MCP Tool

This short project was developed to deepen the understanding of how the **Model Context Protocol (MCP)** works, focusing specifically on the concept of **MCP servers**. The project consists of creating a **local MCP server** in Python using the `mcp[cli]` library.

The server implements a single tool that makes an HTTP request to a weather API, providing real-time weather context to an AI assistant (in this case, Claude). The code can be found [in this repository](https://github.com/tarrut/weather_api_ai_tool).

## What is Model Context Protocol?

The **Model Context Protocol (MCP)** is an open standard developed by Anthropic to standardize the integration of AI models with external tools and services. MCP allows AI assistants to interact with various resources without requiring bespoke connectors. It operates on a **modular client-server architecture**, where AI applications (hosts) communicate with MCP servers that expose resources, tools, and prompts.  

This design facilitates seamless context exchange, enabling AI models to perform tasks such as reading files, querying databases, or invoking APIs in an efficient and secure manner.

## MCP with Claude Desktop

**Claude Desktop** leverages MCP to enhance its capabilities by connecting with both local and remote services. Through MCP, Claude can perform actions such as reading from the file system, writing new files, moving files, and searching documents (with user consent).  

MCP ensures that interactions with external tools are permissioned, transparent, and controlled by the user, preserving a high standard of privacy and security. This integration empowers users to extend Claude's functionality, making it a versatile and powerful assistant for a wide range of tasks.

## Weather API

To fetch current weather data, the tool integrates with a **Weather API**, which provides real-time weather information for any location worldwide. The API returns data such as temperature, humidity, wind speed, and weather conditions in JSON format.  

Developers access this data by making HTTP requests to the API endpoints, specifying parameters such as the city name or geographic coordinates.