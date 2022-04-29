from models import User,Treepath, Session, engine,exc,desc


class create_users:
    def __init__(self):
        self.local_session = Session(bind=engine)
    def add_user(self):
        
            self.username = input("Enter the username:")
            print("username:",self.username)
            self.email = input("Enter the email id:")
            self.new_user = User(username=self.username,email=self.email)
        # Adding user details into user
            self.local_session.add(self.new_user)
        # Getting the newly inserted user id
            self.new_id = self.local_session.query(User).order_by(desc(User.id)).first()
            print("new id:",self.new_id.id)
        # adding into treepath table
            self.sponser_id = int(input("Enter the Sponser id:"))
            self.add_treepath = Treepath(sponser_id=self.sponser_id,user_id=self.new_id.id)
            self.local_session.add(self.add_treepath)
            self.local_session.commit()
         
      
ob1 = create_users()
ob1.add_user()
