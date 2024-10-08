from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    uploaded_img_file = db.Column(db.String(255), nullable=True) #20231230
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'), nullable = False)
    user = db.relationship('User',backref = db.backref('question_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True,nullable = True)
    password = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(120),unique = True,nullable = False)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_eng = db.Column(db.String(100), nullable=False)
