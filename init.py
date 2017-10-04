'''
Copyright 2017 Dumidu Handakumbura

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import prerequisite.systemprerequisite as syscheck
import db.dbwrapper
import os
import logging.config


# boots the application.
def bootloader():
    os.putenv('K8S2DCKR', os.getcwd())
    setup_logging()
    logger = logging.getLogger('bootloader')
    if syscheck.check():
        db.dbwrapper.moduletest()
        logger.info('running.')
        quit(0)
    else:
        quit(1)


# reads loggin configuration to setup logger.
# 'disable_existing_loggers' should be set to False to allow log messages from other modules.
def setup_logging():
        import yaml
        with open('config/logging_config.yaml', 'rt') as f:
            config = yaml.load(f)
        logging.config.dictConfig(config)



if __name__ == "__main__":
    bootloader()
