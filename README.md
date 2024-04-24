# 4022-Project

<div align="center">
    <img src="./assets/plt1.png" alt="plts"/>
</div>

Digit classification with K-Means clustering

Main code file is ```research/main.ipynb```

### Environment Setup 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

###  Write-Up
Google Doc: https://docs.google.com/document/d/1jfs_Y3a3PV33UePfLRl7O0zu-oGrzLDcF12To9LohM0/edit

The project write-up is a 5-7 page paper (single spaced, 12 pt font). This includes any smaller graphics used, but don’t just fill a document with 7 full page images. You may use your own discretion on how to write and format the paper, but your goal is to both clearly and eloquently describe your problem solving process and results.

A possible outline may follow a standard hard sciences academic paper.  Consider sections such as:

* Introduction: the why of the question: what’s the real-world impact? Why do you yourself care? (maybe half a page)
* Data: what is the source of your data. Describe any and all columns/features in the data set, and where the read could find the data if possible.
* Real-world impact: a miniature literature review or context for the problem. Is this a problem solved by real world companies? Are there any easily accessible academic papers. 
* Exploratory results: you may include any work you did for the preliminary check-in here, but make sure you’ve adjusted the write-up to fit into the overall content of the paper.
* Methods: what data science technique are you using? Why should this model give you results that are useful to the why of the question? * If there are any ad hoc choices in the algorithms, what are you choosing for them?  If there is a probability model (like in BigCLAM or GMMs), write it out.  This is the place to include any equations that define your model.
* Results: what came out of your methods? This is where you can show off your pretty pictures.  As in the presentation, if you have a lot of days/times/locations/people/etc., pick one or two to show plots or a table of. 
* Conclusion: The conclusion could be an explanation of “work still to do” or “unanswered questions” or even “why the 4022 technique was worse than doing a neural net or linear model”. Make sure you circle back to the why of the data science problem.  Did you successfully answer anything with interesting results?
* Submit your final paper as a .pdf.

### Presentation

Slides: https://docs.google.com/presentation/d/1LgfTgp0mLIOAv0NgphH1Dabi6m-mlunv26zONNy2kFc/edit#slide=id.p

The project presentation is a 5-minute talk with a quick 60-second questioning period. For your talk, make sure that you:

* Introduce who you are and the why of the question: what’s the real-world impact? Why do you yourself care?  (about 30s)
* Introduce the data. How big is it?  Where did it come from?  Maybe show a plot or a picture of a row/data point (about 30s)
* Describe your model. If it’s one we did in class, just use words or a quick bullet point.  This isn’t the right type of talk for lots of formalism: if you can make a picture of the model that’s much more valuable than a pile of equations (about 30s)
* Show some results. You might not have final results or it might be hard to show all of the results, so pick something that’s smaller and easier to show.  If you have a lot of days/times/locations/people/etc., pick one or two to show plots or a table of. 
* EX: What are the biggest 2-3 item associations?
* EX: If we’re clustering, what are 2-3 items in cluster A and 2-3 items in cluster B? Do they pass the sanity check?
(about 2 minutes)
* And you’re done!  The conclusion could be a quick list of “work still to do” or “unanswered questions” or even “why the 4022 technique was worse than doing a neural net or linear model”.