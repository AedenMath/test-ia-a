#!/usr/bin/env python3
"""
Flask Web Server with Embedded HTML, CSS, and JavaScript
A complete web interface served by a Flask application.
"""

from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# HTML, CSS, and JavaScript embedded as strings
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Web Server</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 800px;
            width: 100%;
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
        }

        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .info-section {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .info-title {
            font-size: 1.3em;
            color: #333;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .info-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }

        .info-item:last-child {
            border-bottom: none;
        }

        .info-label {
            font-weight: 600;
            color: #555;
        }

        .info-value {
            color: #667eea;
            font-family: 'Courier New', monospace;
        }

        .button-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 30px;
        }

        button {
            flex: 1;
            min-width: 150px;
            padding: 12px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        }

        button:active {
            transform: translateY(-1px);
        }

        button.secondary {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }

        .card {
            background: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 1.2em;
            color: #333;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .response-box {
            background: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #333;
            max-height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-break: break-word;
        }

        .response-empty {
            color: #999;
            font-style: italic;
        }

        .badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 10px;
        }

        .badge.success {
            background: #10b981;
        }

        .badge.warning {
            background: #f59e0b;
        }

        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #10b981;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }

        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #666;
            font-size: 0.9em;
        }

        .error {
            background: #fee;
            color: #c33;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            display: none;
        }

        .success {
            background: #efe;
            color: #3c3;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            display: none;
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 1.8em;
            }

            .button-group {
                flex-direction: column;
            }

            button {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Flask Web Server</h1>
            <p class="subtitle">Complete Web Interface with Embedded Resources</p>
        </header>

        <div class="info-section">
            <div class="info-title">
                <span class="status-indicator"></span>Server Status
            </div>
            <div class="info-item">
                <span class="info-label">Status:</span>
                <span class="info-value" id="serverStatus">Online</span>
            </div>
            <div class="info-item">
                <span class="info-label">Current Time (UTC):</span>
                <span class="info-value" id="currentTime">Loading...</span>
            </div>
            <div class="info-item">
                <span class="info-label">Server Uptime:</span>
                <span class="info-value" id="uptime">Calculating...</span>
            </div>
            <div class="info-item">
                <span class="info-label">Page Load Time:</span>
                <span class="info-value" id="loadTime">Calculating...</span>
            </div>
        </div>

        <div class="button-group">
            <button onclick="getServerData()">📊 Get Server Data</button>
            <button onclick="getSystemInfo()" class="secondary">💻 System Info</button>
            <button onclick="clearResponse()">🧹 Clear Response</button>
        </div>

        <div class="card">
            <div class="card-title">API Response</div>
            <div class="response-box" id="responseBox">
                <span class="response-empty">Click a button to see the response here...</span>
            </div>
            <div class="error" id="errorBox"></div>
            <div class="success" id="successBox"></div>
        </div>

        <div class="info-section">
            <div class="info-title">Quick Stats</div>
            <div class="info-item">
                <span class="info-label">Requests Made:</span>
                <span class="info-value" id="requestCount">0</span>
            </div>
            <div class="info-item">
                <span class="info-label">Last Request:</span>
                <span class="info-value" id="lastRequest">None</span>
            </div>
        </div>

        <footer>
            <p>Flask Web Server &copy; 2026 | Built with Python Flask</p>
            <p>All resources are embedded in a single Python file</p>
        </footer>
    </div>

    <script>
        let requestCount = 0;
        const pageLoadStart = Date.now();

        // Initialize
        window.addEventListener('load', function() {
            updateTime();
            setInterval(updateTime, 1000);
            updateLoadTime();
        });

        function updateTime() {
            const now = new Date();
            const utcString = now.toISOString().slice(0, 19).replace('T', ' ');
            document.getElementById('currentTime').textContent = utcString + ' UTC';
        }

        function updateLoadTime() {
            const loadTime = Date.now() - pageLoadStart;
            document.getElementById('loadTime').textContent = loadTime + ' ms';
        }

        function getServerData() {
            makeRequest('/api/server-data', 'Server Data');
        }

        function getSystemInfo() {
            makeRequest('/api/system-info', 'System Information');
        }

        function makeRequest(endpoint, title) {
            const responseBox = document.getElementById('responseBox');
            responseBox.innerHTML = '<span class="response-empty">Loading...</span>';

            fetch(endpoint)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    requestCount++;
                    document.getElementById('requestCount').textContent = requestCount;
                    document.getElementById('lastRequest').textContent = new Date().toLocaleTimeString();

                    let output = title + '\\n' + '='.repeat(title.length) + '\\n\\n';
                    output += JSON.stringify(data, null, 2);

                    responseBox.textContent = output;
                    showSuccess('Request successful!');
                })
                .catch(error => {
                    console.error('Error:', error);
                    responseBox.innerHTML = '<span style="color: #c33;">Error: ' + error.message + '</span>';
                    showError('Request failed: ' + error.message);
                });
        }

        function clearResponse() {
            document.getElementById('responseBox').innerHTML = 
                '<span class="response-empty">Response cleared. Click a button to fetch data...</span>';
            document.getElementById('errorBox').style.display = 'none';
            document.getElementById('successBox').style.display = 'none';
        }

        function showError(message) {
            const errorBox = document.getElementById('errorBox');
            errorBox.textContent = message;
            errorBox.style.display = 'block';
            setTimeout(() => errorBox.style.display = 'none', 5000);
        }

        function showSuccess(message) {
            const successBox = document.getElementById('successBox');
            successBox.textContent = message;
            successBox.style.display = 'block';
            setTimeout(() => successBox.style.display = 'none', 3000);
        }

        // Calculate uptime (simulated)
        setInterval(() => {
            const uptime = Math.floor((Date.now() - pageLoadStart) / 1000);
            const hours = Math.floor(uptime / 3600);
            const minutes = Math.floor((uptime % 3600) / 60);
            const seconds = uptime % 60;
            document.getElementById('uptime').textContent = 
                `${hours}h ${minutes}m ${seconds}s`;
        }, 1000);
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Serve the main web interface."""
    return HTML_TEMPLATE, 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route('/api/server-data', methods=['GET'])
def server_data():
    """API endpoint that returns server data."""
    return jsonify({
        'status': 'online',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'server': 'Flask Development Server',
        'python_version': __import__('sys').version.split()[0],
        'message': 'Server is running successfully',
        'endpoints': [
            '/api/server-data',
            '/api/system-info'
        ]
    })


@app.route('/api/system-info', methods=['GET'])
def system_info():
    """API endpoint that returns system information."""
    import platform
    import psutil
    
    try:
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
    except:
        cpu_percent = 'N/A'
        memory = None
        disk = None

    system_data = {
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'architecture': platform.architecture()[0],
        'hostname': os.uname().nodename if hasattr(os, 'uname') else 'Unknown',
        'processor': platform.processor(),
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }

    if memory:
        system_data['memory'] = {
            'total_gb': round(memory.total / (1024**3), 2),
            'used_gb': round(memory.used / (1024**3), 2),
            'available_gb': round(memory.available / (1024**3), 2),
            'percent': memory.percent
        }

    if disk:
        system_data['disk'] = {
            'total_gb': round(disk.total / (1024**3), 2),
            'used_gb': round(disk.used / (1024**3), 2),
            'free_gb': round(disk.free / (1024**3), 2),
            'percent': disk.percent
        }

    if cpu_percent != 'N/A':
        system_data['cpu_percent'] = cpu_percent

    return jsonify(system_data)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource does not exist',
        'status': 404
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred',
        'status': 500
    }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("Flask Web Server Starting")
    print("=" * 60)
    print("Server URL: http://localhost:5000")
    print("Health Check: http://localhost:5000/health")
    print("API Endpoints:")
    print("  - /api/server-data")
    print("  - /api/system-info")
    print("=" * 60)
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
