import logging

__all__ = ['Logger']
Logger: logging.Logger = logging.getLogger('tkloader')
Logger.setLevel(logging.DEBUG)

__console_handler: logging.StreamHandler = logging.StreamHandler()
__file_handler: logging.FileHandler = logging.FileHandler('Error.log')

__console_handler.setLevel(logging.DEBUG)
__file_handler.setLevel(logging.WARNING)
'''
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
'''
#__console_format: logging.Formatter = logging.Formatter('\033[91m[\033[0m\033[1m\033[93m%(levelname)s\033[0m   \033[91m] \033[91m[\033[0m\033[1m\033[93m%(name)s\033[0m   \033[91m]\033[0m \033[93m- %(message)s\033[0m')
__console_format: logging.Formatter = logging.Formatter('\033[91m[\033[0m\033[1m\033[92m%(levelname)s\033[0m   \033[91m] [\033[1m%(name)s\033[0m   \033[91m] - %(message)s\033[0m')
__file_format: logging.Formatter = logging.Formatter('[%(levelname)s   ] [%(name)s   ] - %(message)s')

__console_handler.setFormatter(__console_format)
Logger.addHandler(__console_handler)
__file_handler.setFormatter(__file_format)
Logger.addHandler(__file_handler)