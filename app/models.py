from mongoengine import Document, StringField

class Property(Document):
    property_name = StringField()
    property_cost = StringField()
    property_type = StringField()
    property_area = StringField()
    property_locality = StringField()
    property_city = StringField()
    
    meta = {
        'collection': 'Properties', 
    }
