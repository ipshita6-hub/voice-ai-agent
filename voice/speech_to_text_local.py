"""Local speech-to-text using Google Speech Recognition (free, no API key)."""

import speech_recognition as sr


class LocalSpeechToText:
    """Handle speech-to-text conversion using local/free services."""
    
    def __init__(self):
        """Initialize speech-to-text handler."""
        self.recognizer = sr.Recognizer()
        
        # Adjust for ambient noise
        print("🎤 Calibrating microphone for ambient noise...")
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        print("✅ Microphone ready!")
    
    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> str:
        """
        Record and transcribe audio in one step.
        
        Args:
            timeout: Seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for the phrase
        
        Returns:
            Transcribed text
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (speak now)")
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                
                print("🔄 Transcribing...")
                
                # Try Google Speech Recognition (free, no API key)
                try:
                    text = self.recognizer.recognize_google(audio)
                    print(f"📝 Transcribed: {text}")
                    return text
                except sr.UnknownValueError:
                    print("❌ Could not understand audio")
                    return ""
                except sr.RequestError as e:
                    print(f"❌ Could not request results; {e}")
                    return ""
        
        except sr.WaitTimeoutError:
            print("❌ No speech detected (timeout)")
            return ""
        except Exception as e:
            print(f"❌ Error during speech-to-text: {e}")
            return ""
    
    def listen_continuous(self) -> str:
        """
        Listen continuously until user stops speaking.
        
        Returns:
            Transcribed text
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (speak now, will auto-detect when you stop)")
                
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen
                audio = self.recognizer.listen(source)
                
                print("🔄 Transcribing...")
                
                # Transcribe
                text = self.recognizer.recognize_google(audio)
                print(f"📝 Transcribed: {text}")
                return text
        
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""
