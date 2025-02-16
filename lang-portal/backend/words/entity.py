from peewee import *

db = SqliteDatabase('portalLang.db')
_WPP_= 2 # number of words per page

def word2Tuple(row, fields):
    w={}
    for idx, field in enumerate(fields):
        w[field]=row[idx]
    return w

class Words(Model):
    id = IntegerField(primary_key=True)
    es = TextField()
    en = TextField()
    gender = TextField()
    context = BlobField()

    class Meta:
        database = db
        table_name = 'Words'

class WordsNQ():
    
    def allwords(page=1):
        words=[]
        db.connect()
        rows = Words.select().paginate(page,_WPP_)
        fields= Words._meta.fields.keys()
        for row in rows.tuples().iterator():
            words.append(word2Tuple(row,fields))
        db.close()
        return words
    
    def getWord(id):
        words=[]
        db.connect()
        fields= Words._meta.fields.keys()
        #row = Words.select().where(Words.id == id)
        row = db.execute(Words.select().where(Words.id == id)).fetchone()
        if row is None:
            return "empty"
        response=word2Tuple(row,fields)
        db.close()
        return response

    
