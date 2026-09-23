class User:
    def __init__(self,name, followers, password, nickname):
        self.name = name 
        self.followers = followers
        self.__paswword = password
        self.nickname = nickname

    def enroll(self, post):
        self.post = post

    def share(self, name):
        print(f"\nNEW \nHello my name is: {self.name}")

    def create_post(self, title, content):
        self.title = title
        self.content = content
        print(f"from {self.name} public {self.title}: {self.content}")

    def create_message(self, content_message, receiver):
        self.content_message = content_message
        self.receiver = receiver
        print(f"Message from {self.nickname} to {self.receiver.nickname }: {self.content_message}  ")



class Post:
    def __init__(self, publication, id, nickname, receiver):
        self.publication = publication
        self.__id = id
        self.nickname = nickname
        self.receiver = receiver 

    def enroll(self, comment):
        self.comment = comment

    def public(self, nickname, publication):
        print(f"{nickname}: {publication}")

    def create_comment(self, content):
        self.content = content
        print(f"from {self.nickname} to User:{self.receiver} comment:{self.content}")


        

class Comments:
    def __init__(self, comment, likes, retwits):
        self.comment = comment
        self.likes = likes
        self.retwits = retwits

    def commenting(self,comment):
        print(f"{comment}")

class Message:
    def __init__(self, dm, amount_dm, notes):
        self.dm = dm
        self.amount_dm = amount_dm 
        self.notes = notes 

    def text(self, dm,):
        print(f"{dm}")


user1 = User("Diego Toledo", 200, "HOLA1", "perro")
user2 = User("Gael avila", 200, "HOLA2", "gato")
post1 = Post("The new movie of spiderman is amazing", 1, "gato", "Diego toledo")
comments1 = Comments("I'm disagree with your point", 0, 0)
message1 = Message("Bro, you went to the party last night?", 0, 0)

#Create a post
user1.enroll(post1)
user1.create_post("Amazing","it works")

#Comment a post
post1.enroll(comments1)
post1.create_comment( "It is")

#Send a message
user2.create_message("Yes i did", user1)