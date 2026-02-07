from groq import Groq
import os

class CaricaCareAdvisor:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"  # Faster, uses fewer tokens

    def get_organic_advice(self, disease_name):
        try:
            prompt = f"""
            Diagnosis: {disease_name} in Papaya.
            Expert Persona: CaricaCare AI Organic Expert for Farmers.
            
            Please provide a SIMPLE, CONCISE guide for farmers with these 4 protocols:
            1. About the Disease
            2. Causes
            3. Prevention
            4. Organic Treatment

            Requirements:
            - Keep it SIMPLE and FARMER-FRIENDLY
            - Use 3-4 SHORT bullet points per protocol (maximum 1-2 lines each)
            - Use simple language that farmers can easily understand
            - Focus on PRACTICAL, ACTIONABLE information
            - ENGLISH_TEXT: Simple 4-protocol guide in English
            - TAMIL_TEXT: Simple Tamil translation (same 3-4 points per protocol)
            - HINDI_TEXT: Simple Hindi translation (same 3-4 points per protocol)

            Rules:
            - NO asterisks (*). NO bolding (**). Use plain text only.
            - Keep each point SHORT and CLEAR (1-2 lines maximum)
            - Use these markers exactly to separate language sections:
            ###ENGLISH_SECTION###
            ###TAMIL_SECTION###
            ###HINDI_SECTION###

            Within EACH language section, use these exact markers before each specific protocol:
            [PROTOCOL_1] - for About the Disease
            [PROTOCOL_2] - for Causes
            [PROTOCOL_3] - for Prevention
            [PROTOCOL_4] - for Organic Treatment
            
            Example format for each protocol:
            - Point 1 (short, clear)
            - Point 2 (short, clear)
            - Point 3 (short, clear)
            """

            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a professional agricultural scientist."},
                          {"role": "user", "content": prompt}],
                temperature=0.2
            )

            res = completion.choices[0].message.content
            
            # Parsing the three sections
            en = res.split("###ENGLISH_SECTION###")[-1].split("###TAMIL_SECTION###")[0].strip()
            ta = res.split("###TAMIL_SECTION###")[-1].split("###HINDI_SECTION###")[0].strip()
            hi = res.split("###HINDI_SECTION###")[-1].strip()
            
            return en, ta, hi
        except Exception as e:
            return f"Error: {str(e)}", "தகவல் பிழை.", "सूचना त्रुटि"

    def transcribe_audio(self, audio_file_path):
        """Transcribes audio using Groq's Whisper-large-v3 model."""
        try:
            with open(audio_file_path, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(os.path.basename(audio_file_path), file.read()),
                    model="whisper-large-v3",
                    response_format="json",
                    language="ta", # Primarily targeting Tamil as per current UI
                    temperature=0.0
                )
                return transcription.text
        except Exception as e:
            print(f"Transcription Error: {e}")
            return None