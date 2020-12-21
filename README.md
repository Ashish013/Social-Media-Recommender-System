# Social-Media-Recommender-System
## A simple Social Media Recommender System based on **Interests of the person**

One way to go about, for a simple Social Media Recommendation System is to recommend people who are a mutual friend to the given person in context.

But the drawback of this method is it recommends all the mutual friends of a given person irrespective of whether the interests, age of the two people match or not.
To overcome this drawback, we sort the mutual connections based on the interests of the two people to provide better recommendations.

Therefore the overview of the entire algorithm can be summarized as:

* First we extract the list of mutual connections of the person in context using the BFS algorithm.

* For the filtering/sorting of the mutual friends to function, each person must provide his/her age and also select preferable interests from a collection of given pre-defined interests.
For example, say the given pool of interest list is [music, reading, gardening, movies, sports]. And each person chooses his/her favourite interests from the given pool.

* Now each person has a corresponding interest_Boolean array based on what particular interest he/she has chosen and not, and also each person has an age attribute. For example interest list of Ashish is [1,0,1,1,0,0,0,1]

* Now using these attributes, we can filter the mutual connection according to the formula:
    ```
    Score = abs(Preson1_Interest0 - Person2_Interest0) + abs(Preson1_Interest1 -  Person2_Interest1) + ... + abs(Preson1_InterestK - Person2_InterestK) + abs(Preson1_Age - Person2_Age)

    where:

    • Personm_Interestn signifies a 1 (or) 0 indicating whether the particular Intereset n is choosen by Person m. 

    • Personm_Age signifies the age of Personm. 

    (For all m = {1,2} and 0 <= n <= K)
    
    ```

### Justification of the above filtering/sorting algorithm used for calculating *score*:

If we ensure the score in the formula is as low as possible then what we are indeed doing is making sure that the 2 given persons are in the similar age group and have similar interests. Now we sort the mutual connections in ascending order to recommend the final filtered connections amongst the mutual connections list. Thereby filtering the mutual connections list and at the same time making up for a simple and effective filtering algorithm. 


