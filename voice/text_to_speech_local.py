"""Local text-to-speech using pyttsx3 (completely offline, no API key)."""

import pyttsx3


class LocalTextToSpeech:
    """Handle text-to-speech conversion using local pyttsx3."""
    
    def __init__(self, rate: int = 150, volume: float = 0.9):
        """
        Initialize text-to-speech handler.
        
        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        
        # Configure voice properties
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # List available voices
        voices = self.engine.getProperty('voices')
        
        # Try to set a good default voice
        for voice in voices:
            if 'english' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        print(f"🔊 Text-to-speech initialized")
    
    def speak(self, text: str, play_audio: bool = True) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text: Text to convert to speech
            play_audio: Whether to play the audio immediately
        """
        if not text:
            return
        
        print(f"🔊 Speaking: {text[:50]}...")
        
        try:
            if play_audio:
                self.engine.say(text)
                self.engine.runAndWait()
        except Exception as e:
            print(f"❌ Error during text-to-speech: {e}")
    
    def set_rate(self, rate: int):
        """Set speech rate."""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume: float):
        """Set volume (0.0 to 1.0)."""
        self.engine.setProperty('volume', volume)
    
    def list_voices(self):
        """List all available voices."""
        voices = self.engine.getProperty('voices')
        print("\n📢 Available voices:")
        for i, voice in enumerate(voices):
            print(f"  {i}. {voice.name} ({voice.id})")
    
    def set_voice(self, voice_index: int):
        """Set voice by index."""
        voices = self.engine.getProperty('voices')
        if 0 <= voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)
            print(f"✅ Voice set to: {voices[voice_index].name}")
        else:
            print(f"❌ Invalid voice index. Available: 0-{len(voices)-1}")
    
    def cleanup(self):
        """Cleanup resources."""
        try:
            self.engine.stop()
        except:
            pass
