from pymongo import MongoClient

connection = MongoClient("127.0.0.1")
db = connection['STUYCS_CODE_REVIEW']
teachers = db['teachers']
students = db['students']

def addAdminTeacher():
    db.teachers.insert_one(
        {
            'email':'admin@admin.edu',
            'password':'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
            'verified':True,
            'classes':[],
            'profile': {
                'firstName':'Admin',
                'lastName':'Admin'
            }
        })

def addAdminStudent():
    db.students.insert_one(
        {
            'email':'student@admin.edu',
            'password':'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
            'verified':True,
            'classes':[],
            'groups':[],
            'files':[],
            'profile':{
                'firstName':'Admin',
                'lastName':'Admin'
            }
        })

addAdminTeacher()
addAdminStudent()
