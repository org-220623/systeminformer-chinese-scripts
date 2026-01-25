from Config.static_data_type import TranslationDataType
from . import (
    DotNetTools,
    ExtendedTools,
    ExtendedServices,
    ExtendedNotifications,
    WindowsExplorer,
    NetworkTools,
    Updater,
    UserNotes,
    OnlineChecks,
    HardwareDevices,
    ToolStatus,
)

DATA: TranslationDataType = (
    ExtendedTools.DATA +
    ToolStatus.DATA +
    HardwareDevices.DATA +
    NetworkTools.DATA +
    DotNetTools.DATA +
    WindowsExplorer.DATA +
    ExtendedNotifications.DATA +
    ExtendedServices.DATA +
    Updater.DATA +
    OnlineChecks.DATA
)