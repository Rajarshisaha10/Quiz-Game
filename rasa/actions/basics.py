from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import time

class ActionGetTime(Action):
    def name(self) -> Text:
        """Unique name of the action"""
        return "get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """The main execution method for the action."""
        
        current_time = time.strftime("%I:%M:%S %p", time.localtime())
        print(current_time)

        message = f"The current time is {current_time}"
        dispatcher.utter_message(text=message)

        return []

class ActionGetDate(Action):
    def name(self) -> Text:
        """Unique name of the action"""
        return "get_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """The main execution method for the action."""

        current_date = time.strftime("%Y-%m-%d", time.localtime())
        message = f"The current date is {current_date}"
        dispatcher.utter_message(text=message)

        return []

class ActionGetDateAndTime(Action):
    def name(self) -> Text:
        """Unique name of the action"""
        return "get_date_and_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """The main execution method for the action."""

        current_date = time.strftime("%Y-%m-%d", time.localtime())
        current_time = time.strftime("%I:%M:%S %p", time.localtime())
        message = f"The current date is {current_date} and the current time is {current_time}"
        dispatcher.utter_message(text=message)