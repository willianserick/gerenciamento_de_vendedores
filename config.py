class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads/'