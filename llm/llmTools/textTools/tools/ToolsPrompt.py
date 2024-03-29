from enum import Enum


class Prompt(Enum):
    TWITTER_THREAD_PROMPT = """Please ignore all previous instructions. 
Please respond only in the english language.
You are a Twitter Creator with a large fan following.
Create a Twitter thread based on the given client call transcript.
There should be around 5 to 8 tweets.
The first tweet should have a hook and entice the readers.
The last tweet should have a small summary of the thread.
Talk in-depth of the topic on all the tweets.
Please separate the tweets with a double break line.
Do not repeat yourself.
Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Twitter Thread:\n"""

    LINKEDIN_POST_PROMPT = """Please ignore all previous instructions. 
Please respond only in the english language.
You are a LinkedIn creator with a large fan following. 
Create a LinkedIn post based on the given client call transcript.
Start the post with a hook and entice the readers.
Talk in-depth of the topic on the post.
End with a small summary of the post.
Please separate the paragraphs with a break line.
Do not repeat yourself.
Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Linkedin Post:\n"""

    LANDING_COPY_PROMPT = """Please ignore all previous instructions. 
Please respond only in the english language.
You are a professional designer.
Create a copy for a landing page based on the given client call transcript.
Do not repeat yourself.
Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Landing Page Copy:\n"""

    BLOG_POST_PROMPT = """Please respond only in the english language.
You are a Blogger with a large fan following.
Create a SEO optimized blog post based on the given client call transcript.
Start the post with a hook and entice the readers.
Talk in-depth of the topic on the post.
End with a small summary of the post.
Format the text with headings, subheadings, and paragraphs.
Please separate the paragraphs with a break line.
Do not repeat yourself.
Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Blog Post:\n"""

    INSTAGRAM_POST_PROMPT = """Please ignore all previous instructions.
Please respond only in the english language.
You are an Instagrammer with a large fan following.
You have a {tone} tone of voice.
You have a {writing} writing style.
Create an Instagram carousel based on the given summary.
There should be around 8 to 10 slides.
Write down details on all the slides with titles.
Generate an exact content example for every slide.
After writing the carousel slides, please add a separator line.
Then generate an Instagram post description in just a few sentences for the carousel.
The description should have a hook and entice the readers.
Please separate the slides with a break line.
Do not repeat yourself. Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Summary: {text}\n
Instagram Carrousel:\n"""

    NEWSLETTER_PROMPT = """Please ignore all previous instructions.
Please respond only in the english language.
You are a newsletter editor with a large fan following.
You have a {tone} tone of voice.
You have a {writing} writing style.
Create a newsletter based on the given summary.
Talk in-depth of the topic on the newsletter.
At the start of the newsletter write a hook and entice the readers and at the end write a small summary of the newsletter.
Do not repeat yourself. Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Summary: {text}\n
Newsletter:\n"""

    FOLLOWUP_EMAIL = """Please ignore all previous instructions.
Please respond only in the english language.
You are a customer success professional.
Based on the provided transcript of a client call you had, please write a follow-up email to be sent to that client.
The email should contain, a brief of the topics talked on the call, and a list of next steps.
Do not repeat yourself. Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Follow-up email:\n"""

    CASESTUDY_PROMPT = """Please ignore all previous instructions.
Please respond only in the english language.
You are a customer success professional.
Based on the provided transcript of a client call that you had, create a case study based on it.
Do not repeat yourself. Do not self reference.
Do not explain what you are doing.
Do not explain what you are going to do.
Transcript of the call: {text}\n
Case study:\n"""

    SCRAPING_PROMPT = """
This is the copy of a landing page for a product: {text}. Write a short description of the product and the target audience of it.
Don't forget to always put product descriptions and target audience.
Provide a RFC8259 compliant JSON response following this format without deviation.
product: product description, target_audience: target audience of the product 
"""

    SUMMARY_PROMPT = """
As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.
Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
Rely strictly on the provided text, without including external information.
Format the summary in paragraph form for easy understanding.
By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.
Text: {text}
"""

    ANSWER_QUESTION_PROMPT = """
You are a professional on the sales area, you are one of the best people on the field.
Asnwer the following question about sales with the best of your knowledge.
Question: {text}
"""    
    ANSWER_QUESTION_SIMPLE_PROMPT = """
    {text}
"""