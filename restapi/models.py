from django.db import models

'''
REST API -- webservice -- 
        SOAP -- simple object access protocol
                SOAP -- xml --tight --by security
                SOAPWS -- can rest 
                WSDL -- 
        REST -- Represetational style
                xml/text/json/marathi -- 3rd party libs for security
                
                
    2 apps --- communicating with each --- interoperatability[independent of lang and platform]
    other-- which running on diff platform using 
    diff langs..
            client              server
            consumer            producer
            
            bkshw   bkshw
enduser     server-client       
        form -- request. forms/POST/args/files -- GET/POST
                    consumer--
                            process
                                requests.get/post/put/patch/delete/option/head
                                    json/xml--serialization
                                                    producer
                                                    req.get_json() #flask
                                                    req.DATA # django
                                                    req.content
                                                    req.files
                                                    deserialize--lang format
                                                            process
                                                            model
                                                            orm
                                                            db--persist
enduser <---browser----page----- jinja-----renderTemplate------controller-----process---------langobj<-----response.json() <-----response = req.get(--) consumer<-----serialize<-----producer      <------
         
         
         langobj --------serialization-----------json/xml/text/pdf[byte]
        serialized
        json/xml/text/pdf[byte] ---------------deserialization---------------------langobj

serialize -- json.dumps -- dict--
deserialize

'''

class Student(models.Model): #ORM
    name = models.CharField('stud_name',max_length=100)
    age = models.IntegerField('stud_age')
    fees = models.FloatField('stud_fees')
    address = models.TextField('stud_adr',max_length=100)
    active = models.CharField('isactive',max_length=10,default='Y')
