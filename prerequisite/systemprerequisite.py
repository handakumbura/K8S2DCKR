'''
Copyright 2017 Dumidu Handakumbura

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

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








