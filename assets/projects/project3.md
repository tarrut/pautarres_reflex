# manim scene with voiceover

## 1 Import libraries

```python
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
```

## 2 Scene

```python
class NameOfTheScene(VoiceoverScene):
    def construct(self):
    
        # self.set_speech_service(GTTSService(lang="ca")) # català
        # self.set_speech_service(GTTSService(lang="en")) # english
        self.set_speech_service(GTTSService(lang="es")) # español
        
        with self.voiceover(text = "Text for voiceover") as tracker:
        # logic of the animation
            t = Text("Hello World!")
            self.play(FadeIn(t), run_time=tracker.duration)
            
```

# References
- https://voiceover.manim.community/en/latest/index.html