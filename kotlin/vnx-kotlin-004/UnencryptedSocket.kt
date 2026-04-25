// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-KOTLIN-004: Unencrypted plain socket (cleartext transmission)

import java.net.ServerSocket
import java.net.Socket

class UnencryptedSocket {

    fun connectToServer(host: String, port: Int): Socket {
        // TRIGGERS: plain Socket without SSL — data sent in cleartext
        val socket = Socket(host, port)
        return socket
    }

    fun startServer(port: Int): ServerSocket {
        // TRIGGERS: plain ServerSocket accepts unencrypted connections
        val serverSocket = ServerSocket(port)
        return serverSocket
    }

    fun fetchData(host: String, port: Int): String {
        // TRIGGERS: plain socket for data transfer
        val conn = Socket(host, port)
        val reader = conn.getInputStream().bufferedReader()
        return reader.readLine() ?: ""
    }
}
