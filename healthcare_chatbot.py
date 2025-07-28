import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[,.!]", "", text)
    return text.strip()

def get_greeting_response():
    return "Hello, I am your healthcare assistant! Ask me about symptoms, emergency help, diet, hygiene, vaccines, or advice for children, elderly, and pregnant women."

def get_fallback_response():
    return "Sorry, I didn't understand that. Please rephrase or ask another healthcare question."

def rule_based_response(user_input):
    user_input = preprocess(user_input)
    # EMERGENCY CASES
    if any(word in user_input for word in ["unconscious", "not breathing", "chest pain", "heart attack", "severe bleeding", "fits", "seizure"]):
        return "⚠️ This might be a medical emergency. Please call emergency services or go to your nearest hospital immediately!"

    # COMMON SYMPTOMS
    elif any(word in user_input for word in ["fever", "temperature", "hot body"]):
        return "Fever can be due to many reasons. Drink fluids, rest, and see a doctor if it stays more than 2 days."
    elif any(word in user_input for word in ["cough", "cold", "sneeze", "runny nose"]):
        return "Cough or cold? Drink warm fluids. If it lasts beyond a week or causes trouble breathing, consult a doctor."
    elif any(word in user_input for word in ["sore throat", "throat pain", "difficulty swallowing"]):
        return "Sore throat is usually viral. Gargle with warm salt water. For severe pain or fever, see a doctor."
    elif any(word in user_input for word in ["fatigue", "tired", "weak"]):
        return "Fatigue could be due to stress or lack of rest, but if it lasts long, consult your doctor for a checkup."
    elif any(word in user_input for word in ["headache", "migraine"]):
        return "Headache can be caused by stress, dehydration, or vision issues. Take rest and drink water."
    elif any(word in user_input for word in ["stomach pain", "abdominal pain", "belly pain"]):
        return "Stomach pain has many causes. If it is severe, with vomiting or fever, consult a doctor."
    elif any(word in user_input for word in ["vomit", "vomiting", "nausea"]):
        return "Vomiting can lead to dehydration. Drink fluids. If persistent or with blood, see a doctor."
    elif any(word in user_input for word in ["diarrhea", "loose motion"]):
        return "Diarrhea can be due to infection. Stay hydrated. If persists >2 days or you feel weak, visit a doctor."
    elif any(word in user_input for word in ["rash", "skin allergy", "itching", "red spots", "hives"]):
        return "Skin rash could be allergy or infection. For severe/spreading rashes, seek medical care."
    elif any(word in user_input for word in ["allergy", "allergic", "sneezing"]):
        return "Allergies cause sneezing/itching. Avoid known triggers, use prescribed meds if needed."
    elif any(word in user_input for word in ["eye pain", "conjunctivitis", "red eye"]):
        return "Eye redness could be conjunctivitis. Avoid touching eyes, see a doctor if there is pain or discharge."
    elif any(word in user_input for word in ["back pain", "joint pain", "knee pain"]):
        return "Back/joint pain: rest, gentle movement, and see a doctor if it persists."

    # COVID/LATEST
    elif "covid" in user_input or "corona" in user_input:
        return "COVID-19 symptoms include fever, cough, and breathlessness. Isolate and consult a doctor if you suspect infection."

    # DIET/NUTRITION
    elif any(word in user_input for word in ["diet", "food", "nutrition", "what to eat"]):
        return "Eat fruits, green veggies, whole grains, proteins, healthy fats. Avoid junk food, drink enough water!"

    # HYGIENE/VACCINATIONS
    elif any(word in user_input for word in ["vaccine", "vaccination", "immunization"]):
        return "Stay up to date on all recommended vaccines. Consult your doctor for the schedule."
    elif any(word in user_input for word in ["hygiene", "wash", "sanitize", "clean", "handwashing"]):
        return "Wash hands often, use sanitizer, and bathe daily to reduce infection risk."

    # SPECIAL GROUP: Pregnancy, Children & Elderly
    elif any(word in user_input for word in ["pregnant", "pregnancy", "pregnancy care"]):
        return "Pregnancy: Eat nutritious food, vitamins, avoid stress, regular prenatal checkups are essential."
    elif any(word in user_input for word in ["child", "baby", "children", "toddler", "kid"]):
        return "Children: ensure vaccination, healthy diet, hydration, and regular checkups. Monitor for fever, rashes, unusual tiredness."
    elif any(word in user_input for word in ["elderly", "senior", "aged", "old age"]):
        return "Elderly: Focus on well-balanced meals, monitor chronic conditions, and get regular checkups."

    # GENERAL RULES
    elif any(word in user_input for word in ["appointment", "doctor", "consult", "book", "visit"]):
        return "To book an appointment, tell your preferred date and time. We'll confirm it soon."
    elif any(word in user_input for word in ["thank", "thanks"]):
        return "You're welcome! Stay healthy 🩺"
    elif user_input in ["exit", "quit", "bye"]:
        return "Take care! Goodbye 😊"
    elif any(word in user_input for word in ["tips", "health tips", "advice"]):
        return "General Health Tips: Eat well, exercise, drink water, wash hands, sleep well, and avoid stress!"

    # GREETING
    elif re.search(r"\b(hi|hello|hey|good morning|good evening|good afternoon)\b", user_input):
        return get_greeting_response()

    else:
        return get_fallback_response()
