#paragraph = int(input("Enter the number of paragraphs: Iam Harsh Chauhan from CSE(AIML). I am currently pursuing my B.Tech in Computer Science and Engineering with a specialization in Artificial Intelligence and Machine Learning. I have a strong passion for technology and programming, and I enjoy working on projects that involve data analysis, machine learning, and software development. In my free time, I like to explore new technologies, participate in coding competitions, and contribute to open-source projects. My goal is to become a proficient AI/ML engineer and make significant contributions to the field of artificial intelligence."))

paragraph = input("Enter the paragraph: ")
paragraph_text = paragraph
paragraph = paragraph.count(".")
paragraph = paragraph + 1
print("The number of paragraphs in the given text is:", paragraph)
#i want to select the number of characters in the paragraph
characters = len(paragraph_text)

word_count = len(paragraph_text.split())
print("The number of words in the given text is:", word_count)

