from models import User,Treepath, Session, engine,exc,desc

localsession = Session(bind=engine)

def get_user(id):
    result = localsession.query(User).join(Treepath).filter(Treepath.user_id==id).first()
    if(result):
        if id == 1:
            return 1
        else:
            print("Exists")
            print(result.id,result.username)
            return get_user(result.id)
        # for user in result:
        #    for tree in user.treepath:
        #        print(user.id,user.username,tree.user_id)
    else:
        print("not Exists")
id = int(input("Enter the user id:"))
get_user(id)