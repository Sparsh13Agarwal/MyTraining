from pet_model import Pet,db

db.create_all()

sib = Pet('Siberian Cat','Dolly','Kapil',5)
hm = Pet('Himalayan Cat','Molly','Rahul',3)
rs = Pet('Russian Cat','Jelly','Puber',4)
db.session.add_all([sib,hm,rs])
db.session.commit()
print(sib)
print(hm)
print(rs)
print(sib.pet_id)
print(hm.pet_id)
print(rs.pet_id)


