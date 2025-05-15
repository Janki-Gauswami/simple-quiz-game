quiz = {
    "What is the capital of India?": {
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Hyderabad"],
        "answer": "B",
        "explanation": "New Delhi has been the capital of India since 1931 and houses all major government offices."
    },
    "Who was the first President of India?": {
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. Rajendra Prasad", "D. Sardar Patel"],
        "answer": "C",
        "explanation": "Dr. Rajendra Prasad served as the first President of independent India from 1950 to 1962."
    },
    "Which Indian river is considered the holiest?": {
        "options": ["A. Yamuna", "B. Ganga", "C. Brahmaputra", "D. Godavari"],
        "answer": "B",
        "explanation": "The Ganga (Ganges) River is regarded as sacred and worshipped by millions in India."
    },
    "Who wrote the Indian National Anthem?": {
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Subhash Chandra Bose", "D. Mahatma Gandhi"],
        "answer": "A",
        "explanation": "Rabindranath Tagore composed 'Jana Gana Mana' in 1911 in Bengali, later adopted as the national anthem."
    },
    "What is the national animal of India?": {
        "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
        "answer": "B",
        "explanation": "The Bengal Tiger represents strength, power, and grace, making it India's national animal."
    },
    "Which Indian state has the highest population?": {
        "options": ["A. Maharashtra", "B. Bihar", "C. West Bengal", "D. Uttar Pradesh"],
        "answer": "D",
        "explanation": "Uttar Pradesh is the most populous Indian state, with over 200 million residents."
    },
    "Who is known as the Father of the Indian Constitution?": {
        "options": ["A. B. R. Ambedkar", "B. Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Rajendra Prasad"],
        "answer": "A",
        "explanation": "Dr. B. R. Ambedkar was the chief architect of the Indian Constitution adopted in 1950."
    },
    "Which is the largest state in India by area?": {
        "options": ["A. Rajasthan", "B. Madhya Pradesh", "C. Maharashtra", "D. Uttar Pradesh"],
        "answer": "A",
        "explanation": "Rajasthan is the largest Indian state by area, covering over 10% of the country."
    },
    "In which year did India become a republic?": {
        "options": ["A. 1947", "B. 1950", "C. 1952", "D. 1949"],
        "answer": "B",
        "explanation": "India became a republic on January 26, 1950, when the Constitution came into force."
    },
    "Which is the national flower of India?": {
        "options": ["A. Rose", "B. Marigold", "C. Lotus", "D. Jasmine"],
        "answer": "C",
        "explanation": "The lotus symbolizes purity and divinity in Indian culture and is the national flower."
    },
    "Who was the first woman Prime Minister of India?": {
        "options": ["A. Indira Gandhi", "B. Sarojini Naidu", "C. Pratibha Patil", "D. Sushma Swaraj"],
        "answer": "A",
        "explanation": "Indira Gandhi became India’s first female Prime Minister in 1966."
    },
    "Which Indian monument is known as a symbol of love?": {
        "options": ["A. Qutub Minar", "B. India Gate", "C. Taj Mahal", "D. Charminar"],
        "answer": "C",
        "explanation": "The Taj Mahal was built by Shah Jahan in memory of his wife Mumtaz Mahal."
    },
    "Which festival is called the Festival of Lights?": {
        "options": ["A. Holi", "B. Diwali", "C. Navratri", "D. Eid"],
        "answer": "B",
        "explanation": "Diwali is celebrated with lamps and fireworks to mark the victory of light over darkness."
    },
    "Who discovered the sea route to India?": {
        "options": ["A. Christopher Columbus", "B. Vasco da Gama", "C. Ferdinand Magellan", "D. Marco Polo"],
        "answer": "B",
        "explanation": "Vasco da Gama reached Calicut in 1498, establishing a sea route from Europe to India."
    },
    "What is the currency of India?": {
        "options": ["A. Dollar", "B. Rupee", "C. Dinar", "D. Taka"],
        "answer": "B",
        "explanation": "The official currency of India is the Indian Rupee (₹)."
    },
    "What does the Ashoka Chakra represent?": {
        "options": ["A. Peace", "B. War", "C. Law and dharma", "D. Unity"],
        "answer": "C",
        "explanation": "The 24 spokes in the Ashoka Chakra stand for righteousness (dharma) and the eternal wheel of law."
    },
    "Which Indian city is known as the Silicon Valley of India?": {
        "options": ["A. Pune", "B. Hyderabad", "C. Bengaluru", "D. Chennai"],
        "answer": "C",
        "explanation": "Bengaluru (Bangalore) is home to major tech companies and is India's startup hub."
    },
    "What is the term of a President in India?": {
        "options": ["A. 4 years", "B. 5 years", "C. 6 years", "D. 7 years"],
        "answer": "B",
        "explanation": "The President of India serves a term of five years after being elected by an electoral college."
    },
    "Who is known as the Iron Man of India?": {
        "options": ["A. Bhagat Singh", "B. Jawaharlal Nehru", "C. Sardar Vallabhbhai Patel", "D. Subhash Chandra Bose"],
        "answer": "C",
        "explanation": "Sardar Patel united the princely states and earned the title 'Iron Man' for his determination."
    },
    "Which Indian satellite was the first to reach Mars?": {
        "options": ["A. INSAT-3D", "B. Chandrayaan-1", "C. Mangalyaan", "D. RISAT-1"],
        "answer": "C",
        "explanation": "Mangalyaan, or Mars Orbiter Mission, made India the first Asian country to reach Mars in 2014."
    }
}
print("****QUIZ GAME****")
print("GAME RULES:\n"
      "If you answer the question correct,\n"
      "score = +1\n,and will head on to the next question.\n"
      "Else if you answer the question correct,\n"
      "you will get the explanation of the question.\n and then head on to the next question.\n"
      "IF YOU WANT TO EXIT THE GAME ENTER (NO)")
name = input("What is your name? ")
name = input("What is your name? ")
while True:
    score = 0
    for question in quiz:
        print("\n" + question)  # Show the question
        for option in quiz[question]['options']:
            print(option)  # Show each option

        user_ans = input("CORRECT OPTION IS: ").strip().upper()  # Take answer once
        if user_ans == quiz[question]['answer']:
            print("✅ Correct!")
            print("+1 mark\n")
            score += 1
        else:
            print("❌ Incorrect!")
            print("Explanation:", quiz[question]['explanation'])

        user_input = input("Do we head on to the next question? yes/no: ").strip().lower()
        if user_input == "yes":
            continue
        elif user_input == "no":
            print("\nGame exited by user.")
            break
        else:
            print("Invalid input, continuing to next question by default.")
            user_input = input("Do we head on to the next question? y/n: ")
            if user_input == "y":
                pass
            else:
                break
        print(f"\n{name}, your final score is: {score}/{len(quiz)}")





