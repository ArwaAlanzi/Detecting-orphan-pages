# Detecting orphan pages and scanning them using Python

This Python script allows you to search for historical mementos (archived copies) of a URL, in this case, a university site. It will download only the HTML pages that are still active (status code 200) and save them as text files.

**The process:**

1. Start by searching for the KSU website (https://ksu.edu.sa) to find its historical mementos.

2. Make sure you have a file named "ksu.txt" that contains all the URLs related to the KSU website.

3. Run the Python script provided to check the status of each URL in the "ksu.txt" file.

4. The script will filter out the active (alive) URLs with a status code of 200 and save them in a new text file.

5. The new text file will contain the details of the active URLs, allowing you to easily access and analyze the archived copies of the KSU website.

By following these steps and utilizing this Python script, you can efficiently detect orphan pages and scan them for historical mementos of the KSU website. This can be valuable for retrieving and studying past content, preserving the university's online history, and conducting research or analysis on the evolution of the website.

