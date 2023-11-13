# CatBeep 猫叫助手
by omltcat 小猫蛋卷

**DCS audio warning for Over-G and Over-AoA**

Find yourself often pulling stick too hard and snapping wings or breaking F-14 INS? Let CatBeep help! 

## How to install
*Auto installer WIP*
1. Find you DCS save folder in:  
`C:\Users\<your_user_name>\Saved Games\DCS or DCS.openbeta`
2. Copy `CatBeepExport` to `Scripts` in the folder above (create if does not exist)
3. Add the following line to `Scripts\Export.lua` (create if does not exist)

```lua
local CatBeeplfs=require('lfs');dofile(CatBeeplfs.writedir()..[[Scripts\CatBeepExport\CatBeep.lua]])
```

## 如何安装
*自动安装程序制作中*
1. 找到 DCS存档文件夹：  
`C:\用户\<你的用户名>\保存的游戏\DCS 或 DCS.Openbeta`
2. 复制 CatBeepExport 至DCS文件夹内的 Scripts 文件夹中（如果没有请新建）
3. 用记事本打开 Scripts 里的 Export.lua（如果没有请新建）在文件末尾加上：
```lua
local CatBeeplfs=require('lfs');dofile(CatBeeplfs.writedir()..[[Scripts\CatBeepExport\CatBeep.lua]])
```