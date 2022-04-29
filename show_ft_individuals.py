from model import Ft_Individual,Treepath,Commision, Session,engine


class Show_Individual:
    def __init__(self):
        self.local_session = Session(bind=engine)
    def show_user(self):
        self.show_user = self.local_session.query(Ft_Individual).join(Treepath).filter(Treepath.descendant==15011).all()
    # count for to identify the number of levels
        self.count = self.local_session.query(Ft_Individual).join(Treepath).filter(Treepath.descendant==15011).count() - 1
        print("Count:",self.count)
        self.level = 0;

        if self.show_user:
            print("Exists")
            # print(self.show_user)
            for user in self.show_user:
                print("Level\tAncestorID\tAncestor_Name\tCommission")
                for des in user.tree:
                    if self.level <= self.count:
                        self.commision = self.local_session.query(Commision).filter(Commision.level==self.level).first()
                    # Calculating Commision 
                        self.amount = round(100 * (self.commision.commission / 100),3)
                
                        self.des_name = self.local_session.query(Ft_Individual).filter(Ft_Individual.id==des.ancestor).first()
                       
                        print(self.level,"\t",des.ancestor,"\t\t",self.des_name.user_name,"\t",self.amount)
                        self.level +=  1
        else:
            print("Not Exists")
ob1 = Show_Individual()
ob1.show_user()
