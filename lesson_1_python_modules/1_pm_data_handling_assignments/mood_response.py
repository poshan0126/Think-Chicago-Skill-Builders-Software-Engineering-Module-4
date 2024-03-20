def mood_response(mood):
    if mood.lower() == "happy":
        return "Great to hear that you're feeling happy today! Keep smiling!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that you're feeling sad.Take care!"
    elif mood.lower() == "excited":
        return "Wow! Sounds like you're having an exciting day."
    elif mood.lower() == "angry":
        return "Hey yo! Cool down!"
    elif mood.lower() == "scared":
        return "hou hou hou"
    else:
        return "Unknown Mood"
