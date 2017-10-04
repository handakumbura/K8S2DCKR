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
    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.error('k8s2dckr logging setup failed.')


if __name__ == "__main__":
    bootloader()
