# AI-video-tutor

Problem: Whenever I'm stuck on a topic, want a clear explanation of something, I turn to YouTubers like The Organic Chemistry Tutor and Khan Academy. However, for specific questions or topics they don't cover, I might not be able to leverage those resources, especially since they typically cover curriculum for high schoolers and content from elementary college courses, and not neccessarily erudite CS courses that I will take in the near future. I could always turn to AI, but it usually outputs verbose messages, which isn't ideal for people who don't feel like reading large text or learn better through engaging visuals. (as copied from the homework assignment).

Solution: I plan to build an AI video tutor which replicates the style of Khan Academy and The Organic Chemistry Tutor. 

Goal: This could eventually extend to an audiovisual AI interface for those who need long requests from an AI but don't prefer to read verbose messages. (as copied from the homework assignment).

MVP (the "Do" cell from my Eisenhower Matrix: 
- User should prompt the tool with their question and the AI responds in the form of a video 
- AI must talk and provide sound output while it draws as if Khan Academy is answering the question live
- The AI needs to make penstrokes, not output text on the fly, else that defeats part of the purpose

Future plans (the "Schedule" part of my Eisenhower Matrix):
- Varied pen colors
- Ability to interrupt the AI and change course
- Download video explanations
- File and voice input, if voice input is incorporated the user should be able to interrupt the AI whenever
- Closed captions
- Users create accounts
- (Later) Give the user ability to draw on the whiteboard and collaborate with the AI, to make the learning feel conversational.
- (Later) Turn this from a specific tutoring-focused app into a full interface where users can interact with AI LLMs in audio-visual format

(Later) means will be implemented in Version 3.0 instead of 2.0, etc., relatively less urgent

Other miscellaneous features (from my "Delete" part of my Eisenhower Matrix):
- Light mode / Dark mode
- Multiple voices
- Practice problems, games
- Other miscellaneous features

Tech stack: Python, HTML, CSS, JS, Flask, HTML Canvas API, LLM, SymPy, JSON (subject to change)

Roadmap:
1. Create the canvas
2. Code the drawing generating engine
3. Code the text generating engine (2 and 3 are interchangeable)
4. Code user input, and other essential user-related functionalities
5. Integrate everything together
6. Fix bugs, ensure everything is running smoothly
7. Implement miscellaneous features, or add features from the "Not urgent/important" bracket.
(Subject to change)

