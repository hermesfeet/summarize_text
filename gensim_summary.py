from gensim.summarization.summarizer import summarize

"""
This module uses Gensim's summarizer with a word count limit to summarize a text.

Example:
    CLI query to run this tokenizer:

        $ python gensim_summary.py

For more information on this:
https://radimrehurek.com/gensim/summarization/summariser.html
"""

text = """
Preliminary data recovered from the black boxes of last week's Ethiopian Airlines crash has revealed "similarities" to October's fatal Lion Air crash, the Ethiopian Minister of Transport said Sunday.

Dagmawit Moges said that investigators have recovered all relevant data from the black boxes.
Moges did not provide additional details about the purported "similarities" between the two crashes but said they would be "subject to further investigation."
Ethiopian Airlines Flight 302 crashed March 10, six minutes after takeoff, killing all 157 people on board. It was the second disaster involving a new Boeing 737 Max 8 aircraft in less than six months.
In October, all 189 people on board Lion Air Flight 610 were killed when the flight went down over the Java Sea in Indonesia 13 minutes after takeoff.
Similarities between the two incidents -- both of which remain under investigation -- led aviation authorities around the world to ban the use of 737 Max 8s.
Investigators suspect the Lion Air crash may have been caused by an angle of attack sensor on the outside of the plane that transmitted incorrect data, which could have triggered automated flight software called the Maneuvering Characteristics Augmentation System, or MCAS, that forced the plane's nose down.
According to a preliminary report on the crash, the pilots first manually corrected an "automatic aircraft nose down" two minutes after takeoff and performed the same procedure again and again before the plane hurtled nose-first into the Java Sea, the report said.
On Sunday, after Moges' remarks, Boeing Chairman, President and CEO Dennis Muilenburg issued a statement saying the company "continues to support the investigation, and is working with the authorities to evaluate new information as it becomes available."
Muilenburg added the company is "finalizing its development of a previously announced software update that will address the MCAS flight control law's behavior in response to erroneous sensor inputs."
Ethiopian Airlines CEO Tewolde GebreMariam has previously said the pilot of Flight 302 had "flight control problems" shortly before the plane crashed.
"He was having difficulties with the flight control of the airplane, so he asked to return back to base," GebreMariam said. The pilot was granted permission at the same time the flight disappeared from radar.
CNN's Anna Cardovillis reported from Addis Ababa, while Dakin Andone reported and wrote this story from Atlanta. CNN's Thom Patterson contributed to this report.

"""

print(summarize(text, word_count=90))