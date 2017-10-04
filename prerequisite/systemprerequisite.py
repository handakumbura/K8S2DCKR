import logging, os

#get the values from configuration file
modulelist = ['yaml','jinja2','docker']
containerbuildspace = '/home/dumiduh/KT_DEMO1_BUILDSPACE/'
logger = logging.getLogger(__name__)



def check():
    checksentinal=False
    if modulecheck():
        logger.info('Module validations completed successfully.')
        if systemcheck():
            logger.info('System validations completed successfully.')
            if dockercheck():
                logger.info('Docker runtime validations completed successfully.')
                checksentinal=True

    return checksentinal




def modulecheck():
    modulesavailable = False
    for module in modulelist:
        try:
            __import__(module)
            modulesavailable = True
        except ImportError:
            logger.error(str(module) + 'module was not found.')
            modulesavailable = False

    return modulesavailable


def systemcheck():
    syetemchecksentinal=False

    i=3/2
    if  i == 1:
        syetemchecksentinal = True
    elif i == 1.5:
        logger.error('Python v. 2.X was not found.')
        syetemchecksentinal = False


    try:
        os.stat(containerbuildspace)
        syetemchecksentinal = True
    except:
        logger.error('Buildspace is not accessible.')
        syetemchecksentinal = False

    return syetemchecksentinal

def dockercheck():
    import docker
    dockerchecksentinal=False
    try:
        dclient=docker.from_env()
        dockerversioninfo = dclient.version()
        for key in dockerversioninfo.keys():
            if 'linux' in dockerversioninfo[key].lower():
                dockerchecksentinal=True
                logger.debug(dockerversioninfo[key])
    except:
        logger.error('Docker run-time checks failed.', exc_info=True)

    return dockerchecksentinal








