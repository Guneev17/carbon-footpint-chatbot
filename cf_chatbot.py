import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "18e63320-59f2-11ec-bf74-790db530cef4b646d0e4-8c5a-4bf6-b1d4-22721a87ed38"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def flight_cf():
    flight_emission=0.0
    print("Welcome to air travel(planes) carbon calculator. Please provide the following details");
    taken = int(input("How many times did you use a plane this year(one way): "))
    total_miles= float(input("how many miles did you travel in total using a plane: "))
    flight_carbon= (total_miles *0.2) * taken
    print("Your carbon footprint",flight_carbon,"in kilograms CO2 emissons per mile")

def person_cf():
    print("Welcome to house carbon calculator. Please provide the following details");
    emissions=0.0
    people=float(input("Enter family members"))
    food=float(input(("If you are a u are a Non-vegetarian then input 1 or if vegetarian/vegan input 2")))
    calories=float(input("Enter avg calories"))
    if food==1:
        emissions += (calories*0.01)*people
    elif food==2:
        emissions += (calories*0.005)*people
    else:
        print("not a valid option")
    miles=float(input("Enter avg kms driven in a year"))
    if(miles>0):
        emissions += miles*0.01
    else:
        print("enter valid kms driven")
    household_utilities=float(input("Enter number of household utilities \nThey include 1)Electricity \n2)Natural Gas \n3)Fuel \n4)oil"))
    total_expenditures=float(input("Enter total expenditures spent after the utilities"))
    if(people>0&household_utilities>0&total_expenditures>0):
        emissions += (0.12*total_expenditures)*household_utilities
    else:
        print("enter valid details")
    emissions += ((0.12*total_expenditures)*household_utilities)*people
    print("your carbon emissions are"+emissions+"metric tonnes")

def train_cf():
    train_emission=0.0
    print("Welcome to railway travel (trains) carbon calculator. Please provide the following details");
    taken = int(input("How many times did you use a train this year: "))
    total_miles= float(input("how many miles did you travel in total using trains: "))
    train_carbon= (total_miles *0.114) * taken
    print("Your carbon footprint",train_carbon,"in kilograms CO2 emissons per mile")

def watts_cf():
    carbon_emission=0.0
    print("Welcome to electicity carbon calculator. Please provide the following details");
    total_kwh= float(input("how many kilowatt-hour(kWh) did you use in total: "))
    train_carbon= (total_kwh *0.429)
    print("Your carbon footprint",train_carbon,"in kilograms CO2 emissons per kWh")

def road_cf():
    road_carbon=0.0
    print("Welcome to road transportation (cars,motorcycles,trucks,etc) carbon calculator. Please provide the following details");

    type=int(input("Are you using gasoline, enter 1 or if you are using diesel enter 2:\n"))

    if type==1:
        taken = int(input("How many gallons did this year: "))
        road_carbon= (taken*8.78)
    elif type==2:
        taken = int(input("How many gallons did this year: "))
        road_carbon= (taken*10.21)
    else:
        print("Not a valid choice")

    print("Your carbon footprint",road_carbon,"in kilograms CO2 emissons per gallon")


def answer_question():
    question = input(r"> ")
    answer = classify(question)
    answerclass = answer['class_name']
    if answerclass == 'flight___cf':
        print("approximately 915 million tonnes of CO2 in 2019")
    elif answerclass == 'largest_cf___flights':
        print("China Southern")
    elif answerclass == 'reduce_cf___flights':
        print("Fly more efficient aircraft. Use new technologies to set more efficient flightpaths and reduce delays. Use sustainable lower-carbon alternative fuels. Invest in emissions offsets within or outside of the aviation sector.")
    elif answerclass == 'lowest_cf___flights':
        print("EasyJet")
    elif answerclass == 'calculate_cf_flights':
        flight_cf()

    elif answerclass == 'person_cf':
        print ('39.767 kg in US')
    elif answerclass == 'reduce_person___cf':
        print ('Insulate your home. Switch to renewables. Buy energy efficient. Use less water. Change your diet')
    elif answerclass == 'calculate_cf___person':
        person_cf()

    elif answerclass == 'train_cf_total':
        print ('14 grams of CO2 emissions per passenger mile')
    elif answerclass == 'reduce_cf___train':
        print ('A single freight train can remove several hundred trucks from the highways, reducing congestion and limiting the number of emissions to the atmosphere of greenhouse gasses. In fact, by moving just five percent of freight from trucks to rail, the result would be nine million fewer tons of greenhouse gas emissions.')
    elif answerclass == 'calculate_cf_train':
        train_cf()

    elif answerclass == 'watts_used_cf__total':
        print ('7 tonnes CO2e per year per person')
    elif answerclass == 'largest_cf___electricity':
        print ('China')
    elif answerclass == 'lowest_cf___electricity':
        print ('Tuvalu')
    elif answerclass == 'calculate_watts_cf':
        watts_cf()

    elif answerclass == 'road_total_cf':
        print ('A typical passenger vehicle emits about 4.6 metric tons of carbon dioxide per year.')
    elif answerclass == 'reduce_cf_road':
        print ("Drive less. Choose fuel efficient vehicles. Don't idle. Optimize home deliveries. Use efficient equipment")
    elif answerclass == 'calculate_road_cf':
        road_cf()
        
while True:
    userInput = input("What emission would you like to calculate? (flight, train, family, electricity, road)\n")
    if userInput == 'flight':
        print ('You can calculate carbon footprint of flights or learn about: total carbon footprint by flights, largest and lowest flight company emitters of carbon footprint and how to reduce carbon footprint in flights')   
        answer_question()

    elif userInput == 'train':
        print ('You can calculate carbon footprint of trains or learn about: total carbon footprint by trains and how to reduce carbon footprint in trains')   
        answer_question()

    elif userInput == 'family':
        print ('You can calculate carbon footprint of a person or learn about: total carbon footprint by people and how to reduce carbon footprint by a person')   
        answer_question()

    elif userInput == 'electricity':
        print ('You can calculate carbon footprint of a country or learn about: average carbon footprint by a country and largest and lowest countries to emit a high carbon footprint')   
        answer_question()

    elif userInput == 'road':
        print ('You can calculate carbon footprint of a road vehicle or learn about: total carbon footprint by a vehicle and how to reduce carbon footprint by a vehicle')   
        answer_question()
