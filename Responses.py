from datetime import datetime
import pandas as pd
import numpy as np



def sample_responses(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hello","hi", "sup"):
		return "Hey!"

	elif user_message in ("who are you", "who are you?"):
		return "I am Chembl Bot!"

	elif user_message in ("How are you?", "how are you?", "how are you"):
		return "I am good. What about you?"

	elif user_message in ("good", "i am good", "I am good"):
		return "That's great to hear"

	elif user_message in ("not too well", "not good", "bad"):
		return "That's bad. Don't worry you'll feel better soon"
		
	elif user_message in ("time","time?"):
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")

		return str(date_time)

	else:

		return "I don't understand you"