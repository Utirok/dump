class Knight:
    rank = "Knight"

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.fief_area = 10

    def service(self):
        if self.rank in {"Knight", "Monastic knight", "Sergeant", "Brother", "Man at arms"}:
            self.experience += 20
            print('you have gained some experience, ' + str(self.experience) + ' points')
        else:
            print('it is time to rest now')

    def give_land(self):
        if self.rank in {"Knight", "Monastic knight"}:
            if int(self.experience) in {50, 100}:
                self.fief_area += 10
                print('you have ' + str(self.fief_area) + ' acres of land to protect')
            else:
                print('serve well')
        else:
            print('you cannot get a fief')


    def rise(self):
        ranks = ["Knight", "Monastic knight", "Sergeant", "Brother", "Man at arms"]
        if self.rank in ranks:
            if self.__class__ == Knight:
                print('you are a ' + str(ranks[0]) + ' now')
            else:
                print('come back later')
        else:
            print('you are grand master already')


class Master(Knight):
    rank = "Master"

    def __init__(self, name):
        super().__init__(name)
        self.fief_area = 50
        self.experience = 200

    def service(self):
        if self.rank in {"Knight", "Monastic knight", "Sergeant", "Brother", "Man at arms"}:
            self.experience += 20
            print('you have gained some experience, ' + str(self.experience) + ' points')
        else:
            print('it is time to rest now')

    def give_land(self):
        if self.rank in {"Knight", "Monastic knight"}:
            if int(self.experience) in {50, 1000}:
                self.fief_area += 10
                print('you have ' + str(self.fief_area) + ' acres of land to protect')
            else:
                print('serve well, sir')
        else:
            print('you cannot get a fief, peasant')

    def rise(self):
        ranks = ["Master", "Grand master"]
        if self.rank in ranks:
            if self.rank == "Master":
                if self.__class__ == Master:
                    print('you are a ' + ranks[1] + ' now')
                else:
                    print('come back later')
            else:
                print('you are grand master already')


class Grand_master(Knight):
    rank = "Grand master"

    def __init__(self, name):
        super().__init__(name)
        self.fief_area = 5000
        self.experience = 5000
        self.max_experience = 10000

    def service(self):
        if self.experience in {5000, 9999}:
            self.experience += 1000
            print('your experience is admirable, sir: ' + str(self.experience))
        else:
            print('years of service have finally undermined your health, you die')
            quit()

    def give_land(self):
        self.fief_area += 1000
        print('you have ' + str(self.fief_area) + ' acres of land to protect')

    def give_promotion(self):
        print("you are grand master")


Gregor = Knight("Gregor")
Gregor.give_land()
Gregor.service()
Gregor.service()
Gregor.service()
Gregor.service()
Gregor.give_land()
Gregor.service()
Gregor.give_land()
Gregor.rise()

Archibald = Grand_master("Archibald")
Archibald.service()
Archibald.service()