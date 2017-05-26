from pymongo import MongoClient
import gridfs
import urllib2

#connect to mongo
connection = MongoClient("127.0.0.1")
db = connection['STUYCS_CODE_REVIEW']
fs = gridfs.GridFS(db)
students = db['students']
teachers = db['teachers']
classes = db['classes']

#how a user uploads a file
#takes name of uploader, assignment, and file OBJECT
#type = upload
def uploadFile(upload, uploaderName, assignmentName):
    fileID = fs.put(upload, uploader = uploader, assignment = assignmentName, fileType = "upload")
    return fileID

#upload file from github link
#type = github
def uploadFileFromGithub(uploaderName, assignmentName, githubUsername, repository, fileName):
    response = urllib2.urlopen('https://raw.githubusercontent.com/{0}/{1}/master/{2}'.format(githubUsername, repository, fileName))
    responseString = response.read()
    
    fileID = fs.put(responseString, filename = fileName, uploader = uploaderName, assignment = assignmentName, fileType = "github")
    return fileID

#get a file
#returns dictionary of
#{ 'assignment', 'uploader', 'file' }
#or (github files)
#{'assignment', 'uploader', 'link', 'file'}
#NOTE: the file is a string
def getFile(fileID):
    data = fs.get(fileID)
    if data.fileType == "github":
        return {
            'uploader': data.uploader,
            'link': data.link,
            'assignment': data.assignment,
            'file': data
        }
    else:
        return {
            'uploader': data.uploader,
            'assignment': data.assignment,
            'file': data.read()
        }
