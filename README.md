# Bot Collection

This repository contains various bots created using Streamlit and Langchain. Each bot is designed to assist with different tasks such as generating blogs, summarizing news, providing mental health advice, suggesting recipes, and creating study plans. Below is a brief description of each bot and its functionality.

## Bots

### 1. BlogGen
- **Description**: This bot generates blog content based on user input. The user provides a topic, desired word count, and blog style, and the bot generates a well-structured blog post.
- **Usage**: Input the topic, word count, and select the blog style to generate a blog.

### 2. HowTos
- **Description**: This bot provides step-by-step guides and tutorials on various topics. Users can request guides on specific subjects.
- **Usage**: Enter the topic for which you need a guide to receive detailed instructions.

### 3. MentalHealthCompanion
- **Description**: This bot offers mental health advice and resources based on the user's current mood, recent activities, and specific concerns. It provides practical tips and strategies to help improve mental well-being.
- **Usage**: Input your current mood, describe your recent activities, and specify any concerns to receive tailored advice and resources.

### 4. NewsSummarizer
- **Description**: This bot summarizes news articles based on user-provided content. Users can paste a news article and specify keywords to focus on, and the bot will generate a concise summary.
- **Usage**: Paste the news article, enter focus keywords, and specify the desired summary length to receive a summary.

### 5. RecipeBot
- **Description**: This bot suggests recipes based on the ingredients available to the user. Users can input the ingredients they have, select a cuisine type, and specify any dietary restrictions.
- **Usage**: Enter the available ingredients, select the cuisine type, and list any dietary restrictions to receive recipe suggestions.

### 6. StudyPlanner
- **Description**: This bot generates a comprehensive study plan based on the subject, duration, study intensity, and preferred resources provided by the user. It helps users organize their study schedule effectively.
- **Usage**: Input the subject, duration in weeks, study hours per week, and preferred study resources to receive a detailed study plan.

## Installation

To run these bots, you need to have Python installed along with the required packages. You can install the necessary packages using the following command:

```bash
pip install streamlit langchain transformers
```

## Running the Bots

Navigate to the directory of the desired bot and run the Streamlit application using the following command:

```bash
streamlit run <bot_script>.py
```

Replace <bot_script>.py with the name of the Python script for the bot you want to run (e.g., BlogGen.py).

Feel free to contribute to this repository by submitting pull requests or opening issues for any bugs or feature requests.
