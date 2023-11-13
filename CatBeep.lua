CatBeep = {}

-- Config
CatBeep.Host = "localhost"
CatBeep.Port = 14009
CatBeep.ExportInterval = 0.05
CatBeep.OutputFile = io.open(lfs.writedir().."/Logs/CatBeep_lua.log", "w")

-- Work with other export scripts
CatBeep.PrevExport = {}
CatBeep.PrevExport.LuaExportStart = LuaExportStart
CatBeep.PrevExport.LuaExportAfterNextFrame = LuaExportAfterNextFrame
CatBeep.PrevExport.LuaExportStop = LuaExportStop
CatBeep.OutputFile:write("CatBeep.lua loaded.\n")

function LuaExportStart()
	CatBeep.socket = require("socket")
	CatBeep.UDPsender = CatBeep.socket.udp()
	CatBeep.UDPsender:setpeername(CatBeep.Host, CatBeep.Port)
	CatBeep.OutputFile:write("UDPsender created\n")
	CatBeep.LastExportTime = 0

	if CatBeep.PrevExport.LuaExportStart then
		CatBeep.PrevExport.LuaExportStart()
	end
end

function LuaExportAfterNextFrame()
	local currentTime = LoGetModelTime()
	if currentTime >= CatBeep.LastExportTime + 0.05 then
		local message = string.format("%.2f,%.4f",LoGetAccelerationUnits().y,LoGetAngleOfAttack())
		CatBeep.UDPsender:send(message)
		CatBeep.LastExportTime = currentTime
	end

	if CatBeep.PrevExport.LuaExportAfterNextFrame then
		CatBeep.PrevExport.LuaExportAfterNextFrame()
	end
end

function LuaExportStop()
	if CatBeep.UDPsender then
		CatBeep.UDPsender:close()
		CatBeep.UDPsender = nil
		CatBeep.OutputFile:write("UDPsender closed\n")
	end

	if CatBeep.PrevExport.LuaExportStop then
		CatBeep.PrevExport.LuaExportStop()
	end
end