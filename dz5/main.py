from logexample import ILog
from logging import DEBUG, CRITICAL
try:
    log = ILog("starting log")
    log = ILog("player press: start")
    log = ILog("map loaded (backup)")
    log = ILog("loading ui")
    log = ILog("ui load fail / restart")
    log = ILog("loading ui")
    log = ILog("ui load fail / notify user")
    log = ILog("player press: load with backup (may lose data)")
    log = ILog("Detected critical components miss! notify user")
    log = ILog("Piracy detected! mismatch from server: missing - Account, loader, C:\Sys32\sims\dll_map_31rfsa.dll, C:\Sys32\sims\dll_map_r442.dll, C:\Sys32\sims\classical.map")
    log = ILog("45200b6aeea8ca8cccc37cb508bdb3f4")
    log = ILog("CRITICAL ~ crash, reason: C:\Sys32\sims\dll_map_r442.dll not found! (possible BSOD or game error)")

    log.LogData(level=DEBUG, filename="sims.log")
except Exception as ex:
    print(ex)