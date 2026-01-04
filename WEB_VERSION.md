# Web Server Launch Instructions for Safari

## Prerequisites
- macOS with Safari browser installed
- Node.js and npm installed (or your project's runtime requirements)
- The project repository cloned locally

## Steps to Launch Web Server

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the Web Server
```bash
npm start
# or if using a different command:
# npm run dev
# node server.js
```

The server will typically start on `http://localhost:3000` or display the URL in the console.

### 3. Open in Safari
- Open Safari browser
- Press `Cmd + T` to open a new tab
- In the address bar, enter the server URL (e.g., `http://localhost:3000`)
- Press `Enter`

## Troubleshooting

### Port Already in Use
If the default port is already in use, you may need to:
- Stop other processes using that port
- Configure the server to use a different port (check your project's configuration)

### Server Not Responding
- Verify the server process is running in your terminal
- Check that the correct URL is entered in Safari
- Look for error messages in the terminal for debugging

### Safari Security Warning
- If Safari shows a security warning, it's typically safe to proceed for local development
- Click "Show Details" then "Visit Website" if needed

## Additional Notes
- Keep the terminal window open while the server is running
- To stop the server, press `Ctrl + C` in the terminal
- Use Safari's Developer Tools (`Cmd + Option + I`) for debugging and inspecting network requests

## More Information
For project-specific setup instructions, refer to the main README.md file.
