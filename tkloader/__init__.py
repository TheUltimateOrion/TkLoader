import sys

from tkloader._version import __version__
from tkloader.constants import SUCCESS, UNSUPPORTED_VERSION
from tkloader.logging.Logger import Logger

Logger.info("Initializing TkLoader")

__all__ = ['jsonloader', 'constants']

__SIF = lambda _f: _f()

def version() -> str:
    return f"The current version of tkloader is {__version__}"

def __parse_py_version(version_info) -> dict[str, int]:
    i = 0
    ret: str = ""
    for info in version_info:
        i += 1
        if i == 4:
            break
        ret += f"{str(info)}."
    return ret[:-1]
    
__py_version__: str = __parse_py_version(sys.version_info)

@__SIF
def __check_version() -> int:
    Logger.info("Checking python version")
    if sys.version_info[0] < 3 or sys.version_info[1] < 10:
        Logger.warn("Invalid Python version found")
        if sys.version_info[0] == 3 and sys.version_info[1] < 10:
            Logger.critical(f"Python version {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} does not meet the minimum Python version required by TkLoader")
            exit(UNSUPPORTED_VERSION)
        elif sys.version_info[0] < 3:
            Logger.critical(f"Python 2.x.x is deprecated please use a newer version of python")
            Logger.warning("Download the newest version of python from https://www.python.org/downloads.")
            exit(UNSUPPORTED_VERSION)
    Logger.info("Python version validation succeeded")
    return SUCCESS


