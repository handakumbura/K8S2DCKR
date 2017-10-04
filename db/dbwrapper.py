'''
Copyright 2017 Dumidu Handakumbura

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sqlite3,logging
db=None
cursor=None
cwd=None
logger = logging.getLogger(__name__)

def moduletest():
    initDB()
    getjob()
    getjobs()
    putjob()
    getEnv()
    putEnv()
    getComposeMeta()
    putComposeMeta()
    closeDB()

def getjobs():
    logger.info('get jobs')

def getjob():
    logger.info('get job')

def putjob():
    logger.info('put job')

def getEnv():
    logger.info( 'get env')

def putEnv():
    logger.info( 'put env')

def getComposeMeta():
    logger.info( 'get compose meta')

def putComposeMeta():
    logger.info( 'put compose meta')


def initDB(filename= None):
    global db, cursor, cwd
    if not filename:
        filename='/home/dumiduh/KT_DEMO1/db/k8s2dckr.db'

    try:
        db=sqlite3.connect(filename)
        cursor=db.cursor()
        t=cursor.execute('SELECT * FROM Jobs').fetchall()
        logger.info(t)
    except:
        logger.error('Database connection error.', exc_info=True)
        cursor=None


def closeDB():
    try:
        cursor.close()
        db.close()
        logger.debug('Successfully closed the database connection.s')
    except:
        logger.error('An error occured while closing the database connection.', exc_info=True)



#wrapper test temp
if __name__ == '__main__':
    moduletest()