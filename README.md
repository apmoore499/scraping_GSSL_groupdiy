---------

# IF YOU HAVE COME HERE FOR COMPILED BUILD THREAD FOR GYRAF SSL COMP

google sheets link:

offline copy:

------


# IF YOU WANT TO FORK / CONTRIBUTE TO PROJECT

Many thanks go to Jakob Gyraf & the community at GroupDIY for this wonderful GSSL compressor!

Motivation: like many threads on GroupDIY, the help thread is many pages long and very hard to search effectively. So, this code will collate all the comments from the forum and put them into .csv file. you can use microsoft excel or google sheets to filter the message column and search for keywords if you want, like for example:

- ``` "Resistor R2 Measured volts " ```
- ``` "Distortion at low volume" ```
- ``` "Oscillation" ```

or whatever. Then you can sift through the relevant comments. The goal is to simplify and facilitate the process of troubleshooting, so that we can spend more time recording.

The script is a python creation which uses beautiful soup to scrape the entire thread, and then dumps it into a csv file

**build/run instructions:**

```sh
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python compile_GSSL.py
```

Improvements:
- Incorporate comment upvote score so we can prioritise helpful comments
- Maybe NLP algo to summarise and simplify text
- Images would be useful
- Hyperlinks would be useful
- Expand to other threads



