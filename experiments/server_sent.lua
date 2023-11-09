-- Load the LuaSocket library
package.path = ";.\\experiments\\LuaSocket\\?.lua"..package.path
local socket = require("socket")

print(socket.version())

-- Create a new TCP server socket
local server = socket.tcp()

-- Bind the server socket to a port
server:bind("127.0.0.1", 8080)

-- Listen for incoming connections
server:listen()

-- Define the function that will handle each incoming connection
local function handle_connection(client)
    -- Send the HTTP headers to the client
    client:send("HTTP/1.1 200 OK\r\n")
    client:send("Content-Type: text/event-stream\r\n")
    client:send("Cache-Control: no-cache\r\n")
    client:send("Access-Control-Allow-Origin: *\r\n")
    client:send("\r\n")

    -- Continuously send the current time to the client
    local i = 1
    while true do
        if i < 10 then
            i = i + 1
        else
            i = 1
        end
        local time = os.date("!%Y-%m-%dT%H:%M:%SZ")
        local message = time.." - "..i
        local status, err = pcall(function() client:send("data: " .. message .. "\r\n\r\n") end)
        if not status then
            print("Client disconnected: ", err)
            return
        end
        print("message: ", message)
        socket.sleep(0.1)
    end
end

-- Accept incoming connections and handle them
while true do
    local client = server:accept()
    handle_connection(client)
    client:close()
end

