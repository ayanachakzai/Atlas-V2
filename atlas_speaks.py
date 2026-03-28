import json
import re
from chatbot_base import ChatbotBase
import os
from openai import OpenAI


class AtlasSpeaks(ChatbotBase):
    # Week 2-3 parent class and variables
    def __init__(self, name="Chatbot"):
        ChatbotBase.__init__(self, name)
    # Week 3 data structure loading
        self.data = self.load_data('data/atlas_myths_facts_comparisons.json')
        self.music_data = self.load_data('data/pakistani_music_database.json')

    # week 3 booleans
        self.conversation_is_active = True

        self.in_music_mode = False
        self.music_step=0
        self.music_preferences = {}

        self.llm_client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.getenv("GROQ_API_KEY"),
        )


    def load_data(self, filepath):
        # Week 3 Functions
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Loaded {len(data)} entries from {filepath.split('/')[-1]}.")
        return data
    
    def greeting(self):
        # Week 2 Greeting
        print(f"\n{'='*60}")
        print(f"Salam & Welcome to {self.name} Speaks")
        print(f"{'='*60}\n")
        print("\nI was created by a student from Balochistan, Pakistan and my purpose is to share.")
        print("\nAlong the way, I can also tell you a little about a few other places –")
        print("the United Kingdom, United States, India, China, and Turkey.")
        print("\nI can also suggest you some good Pakistani music based on your mood and taste!\n")
        print("\nThink of me as a friendly companion who loves exploring traditions,")
        print("debunking myths, and finding connections across cultures.\n")
        print("Would you like to see a MENU of what I can do, or some EXAMPLE prompts")         # Learned from LLM to generate a Menu
        print("to get started?")
        print("\nType: 'menu' or 'examples'")
        print("\nType 'music' to get Pakistani music recommendations.")
        print("Type 'exit' anytime to leave.\n")
        print(f"{'='*60}\n")

    def show_menu(self):
        return (
            "📋 MENU - What I Can Help You With\n\n"
            "🗺️  CULTURAL EXPLORATION\n"
            "  • Ask me about Pakistani culture, traditions, or regions\n"
            "  • Debunk common myths and stereotypes\n"
            "  • Learn about food, festivals, history, and more\n\n"
            "🎵 MUSIC RECOMMENDATIONS\n"
            "  • Get personalized Pakistani music suggestions\n"
            "  • Discover artists from different eras and genres\n"
            "  • Type 'music' to start the questionnaire\n\n"
            "🌍 COMPARATIVE INSIGHTS\n"
            "  • Learn about other countries I know (UK, US, India, China, Turkey)\n"
            "  • Compare cultural practices and traditions\n\n"
            "💬 EXAMPLE COMMANDS\n"
            "  • Type 'examples' to see sample questions\n"
            "  • Type 'music' to get music recommendations\n"
            "  • Type 'exit' to end our conversation\n"
        )

    def show_examples(self):
        return (
            "💡 EXAMPLE QUESTIONS - Try asking me:\n\n"
            "📍 ABOUT PAKISTAN:\n"
            "  • Is Pakistan safe to visit?\n"
            "  • Tell me about Pakistani food\n"
            "  • What is Balochi culture like?\n"
            "  • Are all Pakistanis Muslim?\n\n"
            "🎵 MUSIC:\n"
            "  • music (Start personalized recommendations)\n"
            "  • Recommend me some Pakistani songs\n\n"
            "🌍 COMPARISONS:\n"
            "  • How is Pakistan different from India?\n"
            "  • Tell me about Turkish and Pakistani food\n\n"
            "💭 MYTHS:\n"
            "  • Pakistan is all desert, right?\n"
            "  • Do women have rights in Pakistan?\n"
        )

    def process_input(self, user_input):
        #week 3-4 process user input
        processed = user_input.strip().lower()
        return processed
    
    def start_music_questionnaire(self):
        # Week 4 multi-turn conversation flow
        self.in_music_mode = True
        self.music_step = 1
        self.music_preferences = {}
        
        return (
                "\n🎵 Let me help you discover Pakistani music!\n"
            "I'll ask 3 quick questions.\n\n"
            "Question 1/3: What mood are you in?\n\n"
            "  A) 🎉 Energetic - dance/party vibes\n"
            "  B) 🧘 Calm - relax/meditate\n"
            "  C) 💕 Romantic - in my feelings\n"
            "  D) 🎭 Emotional - deep and powerful\n"
            "  E) 🌍 Curious - explore something new\n\n"
            "Type: A, B, C, D, or E"
        )
    
    def handle_music_questionnaire(self, user_input):
        
        # Q1 Mood
        if self.music_step == 1:
            mood_map = {
                'a': 'energetic',
                'b': 'calm',
                'c': 'romantic',
                'd': 'emotional',
                'e': 'curious'
            }
        
            if user_input in mood_map:
                self.music_preferences['mood'] = mood_map[user_input]
                self.music_step = 2
                return (
                f"\n✅ Mood: {mood_map[user_input].upper()}\n\n"
                        "Question 2/3: Which style sounds interesting?\n\n"
                        "  A) 🎸 Modern (pop, rock, indie)\n"
                        "  B) 🎻 Traditional (folk, classical)\n"
                        "  C) 🙏 Spiritual (Sufi, qawwali)\n"
                        "  D) 🎺 Fusion (traditional + modern)\n\n"
                        "Type: A, B, C, or D"
                )
            else:
                return "Please Choose A, B, C, D, or E"
        
        # Q2 Style
        elif self.music_step == 2:
            style_map = {
                'a': 'modern',
                'b': 'traditional',
                'c': 'spiritual',
                'd': 'fusion'
            }
        
            if user_input in style_map:
                self.music_preferences['style'] = style_map[user_input]
                self.music_step = 3
                return (
                f"\n✅ Style: {style_map[user_input].upper()}\n\n"
                    "Question 3/3: Vocal preference?\n\n"
                    "  A) 🎤 Powerful vocals\n"
                    "  B) 🎹 Soft/gentle vocals\n"
                    "  C) 🎵 Either is fine\n\n"
                    "Type: A, B, or C"
                )
            else:
                return "Please Choose A, B, C, or D"
        
        # Q3 Vocals
        elif self.music_step == 3:
            vocal_map = {
                'a': 'powerful',
                'b': 'soft',
                'c': 'any'
            }
        
            if user_input in vocal_map:
                self.music_preferences['vocals'] = vocal_map[user_input]
                self.music_step = 0
                self.in_music_mode = False
                return self.generate_music_recommendations()
            else:
                return "Please Choose A, B, or C"
            
    def generate_music_recommendations(self):
        mood = self.music_preferences.get('mood')
        style = self.music_preferences.get('style')
        vocals = self.music_preferences.get('vocals')

        matches = []

        for song in self.music_data:
            score = 0

            if song.get('mood', '').lower() == mood:
                score += 1

            if song.get('style', '').lower() == style:
                score += 1

            if vocals == 'any':
                score += 1
            elif song.get('vocal_intensity', '').lower() == vocals:
                score += 1

            # keep songs that match at least 2 out of 3 preferences
            if score >= 2:
                matches.append((score, song))

        if len(matches) == 0:
            return "No good matches found. Try another combination."

        # sort best matches first
        matches.sort(key=lambda x: x[0], reverse=True)
        matches = [song for score, song in matches[:5]]

        response = f"\n🎵 Found {len(matches)} songs for you!\n\n"

        count = 1
        for song in matches:
            response += f"\n🎵 {count}. {song.get('song')} - {song.get('artist')}\n"
            response += f"Year: {song.get('year')} | Language: {song.get('language')}\n"
            response += f"💡 Why you'll love it: {song.get('why_youll_love')}\n"
            response += f"🎶 Comparison to Western Music: {song.get('comparison')}\n"
            count += 1

        return response

# MYTHS
    def check_for_myths(self, user_input):
    # week 4 regex to find myths
        for entry in self.data:
            triggers = entry.get('triggers', [])
            

            for trigger in triggers:
                pattern = re.compile(trigger, re.IGNORECASE)
                
                if pattern.search(user_input):
                    region = entry.get('region', 'Unknown')
                    fact = entry.get('fact', '')
                    reflect = entry.get('reflect', '')

                    response = f"\n🗺️  {region.upper()}\n"
                    response += "="*60 + "\n"
                    response += f"✅ FACT: {fact}\n\n"
                    response += f"💭 REFLECTION: {reflect}\n"
                    response += "="*60 + "\n"
                    response += "\nType: 'menu' or 'examples'"
                    response += "\nType 'music' to get Pakistani music recommendations."
                    return response
        
        # Only return None AFTER checking ALL entries
        return None


# FACTS
    def find_relevant_fact(self, user_input):
        try:
            if not os.getenv("GROQ_API_KEY"):
                return ("\n⚠️ Missing GROQ_API_KEY.\n"
                        "Set it as an environment variable and try again.\n")

            prompt = f"""You are Atlas, a cultural chatbot about Pakistan.

    Answer this question in 2-3 friendly sentences. Give your result in Two Parts:
    1) ✅ 
    2) 💭 (poetic but clear)

    User question: {user_input}

    Focus on Pakistani culture and regions (Balochistan, Punjab, Sindh, KPK, Gilgit-Baltistan, Azad Kashmir, Islamabad),
    or comparisons involving (UK, USA, India, China, Turkey).
    """

            completion = self.llm_client.chat.completions.create(
                # Keep it simple: use a good, cheap model.
                # You can change this model string later without changing other code.
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are Atlas Speaks. You are culturally respectful, concise, and helpful."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=220,
                temperature=0.7
            )

            answer = completion.choices[0].message.content.strip()
            return f"\n🌍 {answer}\n" + "="*60 + "\n"

        except Exception as e:
            print(f"🐛 DEBUG ERROR: {e}")
            return ("\n⚠️ Connection issue. Try asking about:\n"
                    "  • Pakistani food, culture, music\n"
                    "  • Type 'menu' for options\n")

        # COMPARISONS
    def normalize_country(self, s: str) -> str:
        s = s.strip().lower()
        s = re.sub(r'[^a-z\s]', '', s)     # remove punctuation
        s = re.sub(r'^\s*the\s+', '', s)   # remove leading "the"
        s = re.sub(r'\s+', ' ', s)         # collapse spaces
        return s

    def detect_topic(self, text: str):
        text = text.lower()

        if any(w in text for w in ["rain", "weather", "climate", "snow", "temperature", "monsoon"]):
            return "weather"
        if any(w in text for w in ["food", "cuisine", "dish", "eat", "spicy", "tea"]):
            return "food"
        if any(w in text for w in ["safe", "safety", "crime", "danger", "visit", "travel"]):
            return "safety"
        if any(w in text for w in ["culture", "tradition", "festival", "wedding", "dress", "clothes"]):
            return "culture"

        return None
    
    def pick_fact_by_topic(self, facts, topic):
        import random

        # If user didn’t mention a topic, just pick random (your old behavior)
        if topic is None:
            return random.choice(facts)

        # Topic keywords (simple)
        topic_words = {
            "weather": ["rain", "weather", "climate", "snow", "monsoon", "temperature"],
            "food": ["food", "cuisine", "dish", "eat", "spicy", "tea", "bread", "rice"],
            "safety": ["safe", "safety", "crime", "danger", "travel", "visit"],
            "culture": ["culture", "tradition", "festival", "wedding", "dress", "clothes"],
        }

        words = topic_words.get(topic, [])
        filtered = []

        for entry in facts:
            text = (entry.get("fact", "") + " " + entry.get("reflect", "")).lower()
            if any(w in text for w in words):
                filtered.append(entry)

        # If we found topic-matching facts, pick from them. Otherwise fall back to random.
        if filtered:
            return random.choice(filtered)

        return random.choice(facts)

    def choose_shared_topic(self, facts1, facts2):
        topic_words = {
            "weather": ["rain", "weather", "climate", "snow", "monsoon", "temperature"],
            "food": ["food", "cuisine", "dish", "eat", "spicy", "tea", "bread", "rice"],
            "culture": ["culture", "tradition", "festival", "wedding", "dress", "clothes"],
            "history": ["history", "colonial", "empire", "independence", "partition"],
            "language": ["language", "english", "urdu", "punjabi", "sindhi"],
        }

        def has_topic(facts, words):
            for entry in facts:
                blob = (entry.get("fact", "") + " " + entry.get("reflect", "")).lower()
                if any(w in blob for w in words):
                    return True
            return False

        for topic, words in topic_words.items():
            if has_topic(facts1, words) and has_topic(facts2, words):
                return topic

        return None
    
    def handle_comparison(self, user_input):
            # Week 4 - regex pattern matching for comparisons
            # took guidance from LLM to create patterns
            comparison_patterns = [
                r'compare\s+(.+?)\s+(?:with|and|to|versus|vs)\s+(.+)',
                r'difference\s+between\s+(.+?)\s+and\s+(.+)',
                r'(.+?)\s+versus\s+(.+)',
                r'(.+?)\s+vs\s+(.+)'
            ]
        
        # Country name mappings
            country_map = {
                'pakistan': 'Pakistan',
                'uk': 'United Kingdom',
                'britain': 'United Kingdom',
                'england': 'United Kingdom',
                'united kingdom': 'United Kingdom',
                'usa': 'United States',
                'america': 'United States',
                'united states': 'United States',
                'india': 'India',
                'china': 'China',
                'turkey': 'Turkey',
                'great britain': 'United Kingdom',
                'british': 'United Kingdom'
                
        }
        
            for pattern in comparison_patterns:
                match = re.search(pattern, user_input, re.IGNORECASE)
                if match:
                    topic = self.detect_topic(user_input)
                    country1 = self.normalize_country(match.group(1))
                    country2 = self.normalize_country(match.group(2))

                    region1 = country_map.get(country1, country1.title())
                    region2 = country_map.get(country2, country2.title())
                    
                    facts1 = []
                    facts2 = []
                    
                    for entry in self.data:
                        entry_region = entry.get('region', '')
                        if region1.lower() == entry_region.lower():
                            facts1.append(entry)
                        if region2.lower() == entry_region.lower():
                            facts2.append(entry)
                    
                    if facts1 and facts2:
                        if topic is None:
                            topic = self.choose_shared_topic(facts1, facts2)
                        fact1 = self.pick_fact_by_topic(facts1, topic)
                        fact2 = self.pick_fact_by_topic(facts2, topic)
                        

                        response = f"\n🌍 {region1.upper()} and {region2.upper()} - Cultural Overview\n"
                        response += "="*60 + "\n\n"
                        response += f"📍 {region1.upper()}:\n"
                        response += f"{fact1.get('fact', '')}\n\n"
                        response += f"💭 {fact1.get('reflect', '')}\n\n"
                        response += f"📍 {region2.upper()}:\n"
                        response += f"{fact2.get('fact', '')}\n\n"
                        response += f"💭 {fact2.get('reflect', '')}\n\n"
                        response += "="*60 + "\n"
                        response += f"💡 I have {len(facts1)-1} more facts about {region1} and {len(facts2)-1} more about {region2}.\n"
                        response += "Ask me specific questions to learn more!\n"
                        response += "\nType: 'menu' or 'examples'"
                        response += "\nType 'music' to get Pakistani music recommendations."
                        return response
                    elif facts1:
                        fact1 = facts1[0]
                        response = f"\n🌍 About {region1.upper()}\n"
                        response += "="*60 + "\n"
                        response += f"📖 {fact1.get('fact', '')}\n\n"
                        response += f"💭 {fact1.get('reflect', '')}\n"
                        response += "="*60 + "\n"
                        response += f"\n(I don't have information about {region2} to compare)\n"
                        response += "\nType: 'menu' or 'examples'"
                        response += "\nType 'music' to get Pakistani music recommendations."
                        return response
            
            return None   
     
    def get_random_reflection(self):
    # random selection from list in case answer is not found
        import random
        
        reflections = [
            "Every question is a bridge between cultures, even if I don't have all the answers yet.",
            "Some stories are still being written. Ask me about Pakistan, and I'll share what I know!",
            "Like a traveler in new lands, I'm still learning. Try asking about culture, food, or music!",
            "Not all paths are mapped, but I can guide you through Pakistani heritage and traditions.",
            "The best conversations start with curiosity. Let me share what I do know!",
            "Sometimes the melody escapes me, but I have many songs about Pakistan to share.",
            "Every culture has untold stories. Mine are about Pakistan—ask me about them!",
            "Like petals in the wind, some answers drift beyond my reach. But I have many tales of Pakistan!"
        ]
        
        return random.choice(reflections)

    def generate_response(self, processed_input):
        if processed_input in ['menu', 'help', 'options']:
            return self.show_menu()

        if processed_input in ['example', 'examples', 'example prompts', 'samples', 'sample', 'prompts']:
            return self.show_examples()

        if processed_input in ['hi', 'hello', 'hey', 'how are you', 'whats up', 'howdy']:
            return ("\nHello! I'm doing great, thank you for asking! 😊\n"
                    "I'm here to share stories about Pakistan and other cultures.\n"
                    "Type 'menu' to see what I can help you with!\n")

        if processed_input in ['music', 'recommend music', 'music recommendations']:
            return self.start_music_questionnaire()
        
        if processed_input in ['menu', 'help', 'options']:
            print("DEBUG: menu triggered")
            return self.show_menu()

        if self.in_music_mode:
            return self.handle_music_questionnaire(processed_input)

        myth_response = self.check_for_myths(processed_input)
        if myth_response:
            return myth_response
        
        comparison_response = self.handle_comparison(processed_input)
        if comparison_response:
            return comparison_response

        fact_response = self.find_relevant_fact(processed_input)
        if fact_response:
            return fact_response

        return (f"\n{self.get_random_reflection()}\n\n"
        "🤔 I work best with questions about:\n"
        "  • Pakistani culture, traditions, and regions\n"
        "  • Common myths to debunk\n"
        "  • Food, music, history, and festivals\n"
        "  • Comparisons with UK, USA, India, China, Turkey\n\n"
        "💡 Try:\n"
        "  • 'Tell me about Pakistani food'\n"
        "  • 'Is Pakistan safe to visit?'\n"
        "  • Type 'examples' for more ideas\n"
        "  • Type 'menu' to see all options\n")