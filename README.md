# summarize_text
Some different NLP implementation of summarizing text

## What It Does
Tests 2 tools to summarize text (TextTeaser and Gensim) versus a home-grown NLTK-based summarizer.

## Examples
![Source article to summarize, from CNN on plane crashes] (https://www.cnn.com/2019/03/17/africa/ethiopian-lion-air-crash-data-similarities-intl/index.html)

### 1) Gensim Summary Implemented:
How it Works: Uses the TextRank algorithm to create sentences as nodes, and edges as similarity, to then rank top sentences.  The algorithm applies a variation of PageRank [20] over a graph constructed
specifically for the task of summarization. This produces a ranking of the elements in the graph: the most important elements are the ones that better
describe the text. This approach allows TextRank to build summaries without the need of a training corpus or labeling and allows the use of the algorithm
with different languages.  See:  [Variations of TextRank] (https://arxiv.org/pdf/1602.03606.pdf)
Summary:  Preliminary data recovered from the black boxes of last week's Ethiopian Airlines crash has revealed "similarities" to October's fatal Lion Air crash, the Ethiopian Minister of Transport said Sunday.
According to a preliminary report on the crash, the pilots first manually corrected an "automatic aircraft nose down" two minutes after takeoff and performed the same procedure again and again before the plane hurtled nose-first into the Java Sea, the report said.
Ethiopian Airlines CEO Tewolde GebreMariam has previously said the pilot of Flight 302 had "flight control problems" shortly before the plane crashed.

### 2) TextTeaser Summary Implemented:
How it Works: Cleans up text by removing stop words and spaces.  Gets top key words after tokenization and gives it a score - then orders the sentences by the total score.
Summary:  Moges did not provide additional details about the purported "similarities" between the two crashes but said they would be "subject to further investigation."
Ethiopian Airlines Flight 302 crashed March 10, six minutes after takeoff, killing all 157 people on board.
It was the second disaster involving a new Boeing 737 Max 8 aircraft in less than six months.
Ethiopian Airlines CEO Tewolde GebreMariam has previously said the pilot of Flight 302 had "flight control problems" shortly before the plane crashed.
"He was having difficulties with the flight control of the airplane, so he asked to return back to base," GebreMariam said.

### 3) Home-grown NLTK Summary:
How it Works:  Cleans up the text to removes spaces, tabs, stop words, etc, then word and sentence tokenizes it.  Does a word frequency count and then ranks sentences by highest word frequencies, and then outputs top sentences.
Summary:  Preliminary data recovered from the black boxes of last week's Ethiopian Airlines crash has revealed "similarities" to October's fatal Lion Air crash, the Ethiopian Minister of Transport said Sunday. Ethiopian Airlines CEO Tewolde GebreMariam has previously said the pilot of Flight 302 had "flight control problems" shortly before the plane crashed.

## Running the different tools
$ python gensim_summary.py
$ python textteaser_summary.py
cd to nltk_summar, then $ python nltk_summary.py airline.txt

## Built With / Dependencies
Built in Python 3.6. See the Requirements.txt file.
Mostly Gensim, TextTeaser, Numpy, Scipy, NLTK.

## Versioning
Version 1.1.

## Dev Timeline - Next To Do
- Test on on other data
- Add Neural network

## License
This project is licensed under the MIT License.

Copyright 2019 - HermesFeet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Appendix - Corpora to Check Out
![Word-level neural net Keras/LSTM overview] (https://machinelearningmastery.com/how-to-develop-a-word-level-neural-language-model-in-keras/)
![A Survey of Available Corpora for Building Data-Driven Dialogue Systems - UM Paper] (https://arxiv.org/pdf/1512.05742.pdf)
![Dialogue Datasets] (https://breakend.github.io/DialogDatasets/)
