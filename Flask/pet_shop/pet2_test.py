from pet2_model import db, Pet,Owner,Toy

db.create_all()

sib = Pet('Siberian Cat')
hm = Pet('Himalayan Cat')
rs = Pet('Russian Cat')

db.session.add_all([sib,hm,rs])
db.session.commit()

pb= Toy('ping pong ball',sib.id)
rm = Toy('rubber mouse',hm.id)
ty = Toy('ping pong',hm.id)
rb = Toy('rubber bone',rs.id)
db.session.add_all([pb,rm,rb])
db.session.commit()

rg = Owner('Rahul gandhi',sib.id)
nm = Owner('Narendar Modi',hm.id)
ak = Owner('Arvind Kejriwal',rs.id)
db.session.add_all([rg,nm,ak])
db.session.commit()

print(sib)
print(hm)
print(rs)
print(ty.id)
print(rm.id)
print(rb.id)

