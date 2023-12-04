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
		local airframe = LoGetSelfData().Name
		local gearDown = false
		local gearMute = 0
		if CatBeep.GearIndicator[airframe] then
			local gear = 0
		elseif CatBeep.FC3[airframe] then
			gearDown = LoGetMechInfo().gear.value <= 1
		end
		
		if gearDown then
			gearMute = 1
		end

		local message = string.format("%.2f,%.4f,%d",LoGetAccelerationUnits().y,LoGetAngleOfAttack(), gearMute)
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

CatBeep.GearIndicator = {
	['F-14B'] = 8301
}

CatBeep.FC3 = {
	'A-10A',
	'F-15C',
	'J-11A',
	'MiG-29A',
	'MiG-29S',
	'Su-25',
	'Su-25T',
	'Su-27',
	'Su-33'
}