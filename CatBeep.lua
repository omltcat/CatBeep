CatBeep = {}
CatBeep.PrevExport.LuaExportStart = LuaExportStart
CatBeep.PrevExport.LuaExportAfterNextFrame = LuaExportAfterNextFrame
CatBeep.PrevExport.LuaExportStop = LuaExportStop
function LuaExportStart()
	CatBeep.socket = require("socket")
	CatBeep.host = "127.0.0.1"
	CatBeep.port = 8014
	CatBeep.connection = CatBeep.socket.try(CatBeep.socket.connect(CatBeep.host, CatBeep.port))
	CatBeep.connection:setoption("tcp-nodelay",true)

	if CatBeep.PrevExport.LuaExportStart then
		CatBeep.PrevExport.LuaExportStart()
	end
end

function LuaExportAfterNextFrame()
	CatBeep.socket.try(CatBeep.connection:send(string.format("%+.3f",LoGetAccelerationUnits().y)))

	if CatBeep.PrevExport.LuaExportAfterNextFrame then
		CatBeep.PrevExport.LuaExportAfterNextFrame()
	end
end

function LuaExportStop()
	CatBeep.connection:close()
	
	if CatBeep.PrevExport.LuaExportStop then
		CatBeep.PrevExport.LuaExportStop()
	end
end