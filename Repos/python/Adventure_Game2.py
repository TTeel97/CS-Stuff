import random

#define scenarios for each decision type
scenarios = {
    "direction": {
        "left": [
            "You encounter a strange cat that blocks your path. Weirdly he speaks and offers to guide you through the forest.",
            "A pack of wolves block your path. They dont look happy.",
            #Add more scenarios for left path.
        ],
        "right": [
            "You stumble upon an abandoned cabin. It looks awfully spooky.",
            "A sudden ice storm forces you to take shelter under a large tree.",
            #add more scenarios for the right path.
        ]
    },
    "action": {
        "fight": [
            "You engage in combat with the bandits, and emerge victorious.",
            "The bandits overwhelm you and narrowly escape with your life.",
            #add more scenarios for the fight action
        ],
        "negotiate": [
            "You successfully negotiate with the bandits and reach a peaceful solution.",
            "The bandits reject your offer and you must find another way to proceed.",
            #add more scenarios for the negotiate action
        ]
        #add more decision types as needed
    }
}

# Function to choose and execute a random scenario for the given decision type.
def choose_scenario(decision_type,decision):
    return
random.choice(scenarios.get(decision_type,{}.get(decision, [])))

#ask user to choose a decision based on decision type
if decision_type in scenarios:
    decision = input(f"What {decision_type} do you want to make? ").lower()
    if decision in scenarios[decision_type]:
        print(choose_scenario(decision_type,decision))
    else:
        print(f"No scenarios found for {decision} in {decision_type}.")
