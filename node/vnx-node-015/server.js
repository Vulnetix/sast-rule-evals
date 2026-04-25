// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-NODE-015: WebSocket server without origin verification (CSWSH)

const WebSocket = require('ws');
const { Server } = require('socket.io');
const http = require('http');

// VULNERABLE: WebSocket.Server without verifyClient - no origin validation
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
        console.log('received: %s', message);
    });
    ws.send('connected');
});

// VULNERABLE: Socket.IO with wildcard CORS origin - allows CSWSH from any domain
const httpServer = http.createServer();
const io = new Server(httpServer, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

io.on('connection', (socket) => {
    console.log('user connected');
});
