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
    DotNetTools.DATA +
    ExtendedTools.DATA +
    ExtendedServices.DATA +
    ExtendedNotifications.DATA +
    WindowsExplorer.DATA +
    NetworkTools.DATA +
    Updater.DATA +
    UserNotes.DATA +
    OnlineChecks.DATA +
    HardwareDevices.DATA +
    ToolStatus.DATA
)