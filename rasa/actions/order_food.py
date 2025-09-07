from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionOrderFood(Action):
    def name(self) -> Text:
        """Unique name of the action"""
        return "order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """The main execution method for the action."""

        # Retrieve the 'food' slot value from the tracker
        food_item = tracker.get_slot("food")
        
        if food_item == "pizza":
            message = f"Alright opening Domino's"
            dispatcher.utter_message(text=message)
            webbrowser.open_new_tab("https://pizzaonline.dominos.co.in/")
        elif food_item:
            message = f"I don't know the website for {food_item}, but I'll help you search for it."
            webbrowser.open_new_tab(f"https://www.google.com/search?q={food_item}+order+online")
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't understand what you want to order.")

        return []