# Election_Analysis

## Overview of Election Audit 
In this project we were given a csv file which contained the election results. We then used python to write code in order to read the csv file and get the information required by the Colorado Board of Elections and display it in a text file. For the challange part of the project we had to modify/add code to our orginial code in order to get some additional data to complete the election audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Election-Audit Results

When we run the code we get the following text file as an ouput:

<img width="296" alt="Screen Shot 2022-10-25 at 5 47 11 PM" src="https://user-images.githubusercontent.com/44278585/197888572-a3f92116-4f16-4a04-9b34-c2e71a9d402a.png">


**We can use the above output to answer the following questions:**
- How many votes were cast in this congressional election?
  
    369,711 Votes were cast

- Which county had the largest number of votes?

    Denver with 82.8% of the total votes or 306,055 people who voted were from Denver County
 
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    Diana DeGettee was the winner of the election with a vote count of 272,892 which equivalets to 73.8% of the total votes.

## Election-Audit Summary

The benefit of using python is that the code we wrote can be used to get the same data for any election that has its ballots stored in a csv file. The only code that would need to be changed is the variable that we use to load a file from the path and the varibale used to save the file to a path.

<img width="517" alt="Screen Shot 2022-10-26 at 8 42 05 PM" src="https://user-images.githubusercontent.com/44278585/198164751-51c6b349-a196-41b9-bd23-4882d1bbf378.png">


