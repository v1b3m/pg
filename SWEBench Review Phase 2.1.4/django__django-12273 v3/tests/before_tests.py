
from .models import (
    ArticleWithAuthor, BachelorParty, BirthdayParty, BusStation, Child,
    DerivedM, InternalCertificationAudit, ItalianRestaurant, M2MChild,
    MessyBachelorParty, ParkingLot, ParkingLot3, ParkingLot4A, ParkingLot4B,
    Person, Place, Profile, QualityControl, Restaurant, SelfRefChild,
    SelfRefParent, Senator, Supplier, TrainStation, User, Wholesaler,
)


        italian_restaurant.restaurant_ptr = None
        self.assertIsNone(italian_restaurant.pk)
        self.assertIsNone(italian_restaurant.id)