# # logging : writting flow o execution of an application inside file is called logging 
# # logging level :   

# DEBUG: Detailed info for debugging. (logging.DEBUG)

# INFO: General program info. (logging.INFO)

# WARNING: Non-critical issues. (logging.WARNING)

# ERROR: Problems stopping part of the program. (logging.ERROR)

# CRITICAL: Severe issues that might crash the program. (logging.CRITICAL)


import logging
logging.basicConfig(filename='mylog.log',level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
