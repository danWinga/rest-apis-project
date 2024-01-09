from db import db 


class StoreModel(db.Model):
    _tablename =  "stores"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    

    tags = db.relationship("tagModel", back_populates="store", lazy="dynamic")
    items = db.relationship("itemModel", back_populates="store", lazy="dynamic")
    
