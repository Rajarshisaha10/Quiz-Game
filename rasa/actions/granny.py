from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import time

import subprocess



class Actionstart_granny(Action):
    def name(self) -> Text:
        """Unique name of the action"""
        return "start_granny"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """The main execution method for the action."""

        message = f"Starting Granny ..."
        dispatcher.utter_message(text=message)
        subprocess.Popen(r"C:\\Users\\Public\\Desktop\\Grand Theft Auto V.lnk")

        return []