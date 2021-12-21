from enum import Enum


class ProtocolVersion(Enum):
    UNKNOWN = ""
    RFB003003 = "RFB 003.003\n"
    RFB003007 = "RFB 003.007\n"
    RFB003008 = "RFB 003.008\n"
