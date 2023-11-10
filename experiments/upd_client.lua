-- Load the socket library
local socket = require("socket")

-- Set the IP address and port of the server to send data to
local ip = "127.0.0.1"
local port = 14009

-- Create a UDP socket
local udp = socket.udp()

-- Set the socket to broadcast mode
udp:setoption("broadcast", true)

-- Send a random number between 0 to 10 every second to the UDP socket
local g = 0
local aoa = 0
while true do
    -- Generate a random number between 0 to 10
    local diff = math.random(-5, 5)/10
    g = g + diff
    g = math.min(math.max(0, g), 12)

    diff = math.random(-5, 5)/10
    aoa = aoa + diff
    aoa = math.min(math.max(0, aoa), 30)

    local message = g .. "," .. aoa

    -- Send the number to the server
    udp:sendto(message, ip, port)
    print("Sent: " .. message)
    
    -- Wait for 1 second before sending the next number
    socket.sleep(0.05)
end
