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