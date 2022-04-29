from model import Ft_Individual,Treepath,Commision, Session,engine


class Show_Individual:
    def __init__(self):
        self.local_session = Session(bind=engine)
    def show_user(self):
        self.show_user = self.local_session.query(Ft_Individual).join(Treepath).filter(Treepath.descendant==15011).all()
        self.count = self.local_session.query(Ft_Individual).join(Treepath).filter(Treepath.descendant==15011).count() - 1
        print("Count:",self.count)
        # for user in self.show_user:
        #     print("id:",user.id," username:",user.user_name)
        if self.show_user:
            print("Exists")
            print(self.show_user)
            for user in self.show_user:
                for des in user.tree:
                    self.commision = self.local_session.query(Commision).filter(Commision.level==self.count).first()
                    print(self.commision.commission)
                    self.amount = round(100 * (self.commision.commission / 100),3)
                    print("level",self.count,"id:",user.id,"name:",user.user_name,"ancestor:",des.ancestor,"commission:",self.amount)
                    self.count -=  1
        else:
            print("Not Exists")
ob1 = Show_Individual()
ob1.show_user()