from django.contrib import admin
from django.urls import path 
from home import views 
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.index , name = 'Home'),
    path('corporate/' , views.corporate, name = 'corporate'),
    path('education/' , views.education, name = 'education'),
    path('package/' , views.package, name = 'package') , 
    path('social/' , views.social, name = 'social') ,
    path('cars/cars/' , views.carsform, name = 'carsform') ,
   
    path('specialevents/' , views.specialevents, name = 'specialevents') ,
    path('specialeventform/' , views.specialeventform, name = 'specialeventform') ,
    path('tourpackages/' , views.tourpackages ,  name = 'tourpackages') ,
    path('tourpackageform/' , views.tourpackageform ,  name = 'tourpackageform') ,
    path('packageform/' , views.packageform ,  name = 'packageform') ,
    path('socialform/' , views.socialform ,  name = 'socialform') ,







    path('corporate/index.html' , views.corporateHome, name = 'corporateHome'),
    path('education/index.html' , views.educationHome, name = 'educationHome'),
    path('package/index.html' , views.packageHome, name = 'packageHome'),
    path('social/index.html' , views.socialHome, name = 'socialHome'),
    path('specialevents/index.html' , views.specialeventsHome, name = 'specialeventsHome') , 
    path('corporate/educational.html' , views.corporateeducation, name = 'corporateeducation') ,
    path('corporate/social.html' , views.corporatesocial, name = 'corporatesocial') ,
    path('corporate/special_events.html' , views.corporatespecial, name = 'corporatespecial') ,
    path('education/corporate.html' , views.educationcorporate, name = 'educationcorporate') ,
    path('education/social.html' , views.educationsocial, name = 'educationsocial') ,
    path('education/special_events.html' , views.educationspecial, name = 'educationspecial') ,
    path('social/special_events.html' , views.socialspecial, name = 'socialspecial') ,
    path('social/educational.html' , views.socialeducation, name = 'socialeducation') ,
    path('social/social.html' , views.socialsocial, name = 'socialsocial') ,
    path('specialevents/corporate.html' , views.specialcorporate, name = 'specialcorporate') ,
    path('specialevents/educational.html' , views.specialeducation, name = 'specialeducation') ,
    path('specialevents/social.html' , views.specialsocial, name = 'specialsocial')  , 
    path('specialevents/special_events.html' , views.specialspecial, name = 'specialspecial')  ,
    path('corporate/corporate.html' , views.corporatecorporate, name = 'corporatecorporate')  ,







    path('cars/' , views.select, name = 'cars')  ,
    path('Buses/' , views.Buses, name = 'Buses')  ,
    path('Trains/' , views.Trains, name = 'Trains')  ,
    path('Flights/' , views.Flights, name = 'Flights')  ,
    path('Flights/cars.html' , views.Flightscars, name = 'Flightscars')  ,
    path('Flights/Buses.html' , views.FlightsBuses, name = 'FlightsBuses')  ,
    path('Flights/Trains.html' , views.FlightsTrains, name = 'FlightsTrains')  ,
    path('Flights/Flights.html' , views.FlightsFlights, name = 'FlightsFlights')  ,
    path('cars/Flights.html' , views.carsFlights, name = 'carsFlights')  ,
    path('cars/select.html' , views.carscars, name = 'carscars')  ,
    path('cars/Buses.html' , views.carsBuses, name = 'carsBuses')  ,
    path('cars/Trains.html' , views.carsTrains, name = 'carsTrains') , 
    path('Buses/Buses.html' , views.BusesBuses, name = 'BusesBuses') , 
    path('Buses/cars.html' , views.Busescars, name = 'Busescars') , 
    path('Buses/Trains.html' , views.BusesTrains, name = 'BusesTrains') , 
    path('Buses/Flights.html' , views.BusesFlights, name = 'BusesFlights') , 
    path('Trains/cars.html' , views.Trainscars, name = 'Trainscars') , 
    path('Trains/Buses.html' , views.TrainsBuses, name = 'TrainsBuses') , 
    path('Trains/Trains.html' , views.TrainsTrains, name = 'TrainsTrains') , 
    path('Trains/Flights.html' , views.TrainsFlights, name = 'TrainsFlights') , 
    path('Flights/cars.html' , views.Flightscars, name = 'Flightscars') , 
    path('Flights/Buses.html' , views.FlightsBuses, name = 'FlightsBuses') , 
    path('Flights/Trains.html' , views.FlightsTrains, name = 'FlightsTrains') , 
    path('Flights/Flights.html' , views.FlightsFlights, name = 'FlightsFlights') ,
    



    path('corporate/Inner Pages/Corporate/corporate_board_meeting.html' , views.corporatemeeting , name = 'corporatemeeting' ) ,

    path('corporate/Inner Pages/Corporate/corporate/' , views.corporatemeetingcorporate , name = 'corporatemeetingcorporate' ) ,
    path('corporate/Inner Pages/Corporate/corporate_conference.html' , views.corporateconfrence , name = 'corporateconfrence' ) ,
    path('corporate/Inner Pages/Corporate/corporate_social_networking_event.html' , views.corporatenetwork , name = 'corporatenetwork' ) ,
    path('corporate/Inner Pages/Corporate/corporate_webinar.html' , views.corporatewebinar, name = 'corporatewebinar' ) ,

    path('corporate/Inner Pages/Corporate/corporate_workshop.html' , views.corporateworkshop, name = 'corporateworkshop' )  , 

    path('corporate/package.html' , views.corporatepackage, name = 'corporatepackage' )  ,

    path('education/Inner Pages/Educational/educational_camp.html' , views.educationcamp, name = 'educationcamp' )  ,

    path('education/Inner Pages/Educational/educational_educational_tour_trip.html' , views.educationtrip, name = 'educationtrip' )  ,

    path('education/Inner Pages/Educational/educational_seminar.html' , views.educationseminar, name = 'educationseminar' )   , 


    path('education/Inner Pages/Educational/educational_summit.html' , views.educationsummit, name = 'educationsummit' )   ,

    path('social/Inner Pages/Social/social_anniversary.html' , views.socialanniversary, name = 'socialanniversary' )   ,
    path('social/Inner Pages/Social/social_family_reunion.html' , views.socialfamily, name = 'socialfamily' )   ,

    path('social/Inner Pages/Social/social_pre_wedding_photoshoot.html' , views.socialphoto, name = 'socialphoto' )   ,

    path('social/Inner Pages/Social/social_reception.html' , views.socialreception, name = 'socialreception' )   ,

    path('social/Inner Pages/Social/social_tour_trip.html' , views.socialtrip, name = 'socialtrip' )    , 

    path('social/Inner Pages/Social/social_wedding.html' , views.socialwedding, name = 'socialwedding' )  ,

    path('specialevents/Inner Pages/Special Events/special_events_award_show.html' , views.specialaward, name = 'specialaward' )   ,

    path('specialevents/Inner Pages/Special Events/special_events_dance_event.html' , views.specialdance, name = 'specialdance' )  ,

    path('specialevents/Inner Pages/Special Events/special_events_exhibition.html' , views.specialexhibition, name = 'specialexhibition' )   ,

    path('specialevents/Inner Pages/Special Events/special_events_retreat.html' , views.specialretreat, name = 'specialretreat' )   ,

    path('specialevents/Inner Pages/Special Events/special_events_spiritual_and_religious.html' , views.specialreligious, name = 'specialreligious' )   ,

    path('specialevents/Inner Pages/Special Events/special_events_sports_event_tournament.html' , views.specialtournament , name = 'specialtournament' )   ,
    path('education/package.html' , views.educationpackage , name = 'educationpackage' )   ,


    path('education/educational.html' , views.educationeducational , name = 'educationeducational' )   ,

    path('cars/cars/' , views.carscars , name = 'carscars' )  ,   
    path('Buses/Buses/' , views.Busbus, name = 'Busbus' )    , 
    path('tourpackages.html' , views.tpgs, name = 'tpgs' )     ,
    path('Trains/cars/' , views.tcrs, name = 'tcrs' )   ,  
    path('Flights/cars/' , views.fcrs, name = 'fcrs' )     ,
    path('cars/cars/' , views.crscrs, name = 'crscrs' )     ,
    path('Buses/Buses/' , views.bsbs, name = 'bsbs' )     ,
    path('Trains/Trains/' , views.tsts, name = 'tsts' )     ,
    path('Flights/Flights/' , views.fsfs, name = 'fsfs' )    , 
    path('cars/cars/' , views.carsform, name = 'carsform' )   , 
    path('corporate/Inner%20Pages/Corporate/corporate_board_meeting.html' , views.corporatecomment, name = 'corporatecomment' ) ,  
    path('dubai/' , views.dubai , name = 'dubaitour'),
    path('thailand/' , views.thailand , name = 'thailandtour')
    
       
      





    

    
]