# Running

## Purpose

I created this pipeline to easily visualise how much running I was doing. This allows me to keep track of my progress.

## Logging

I keep a log of my runs in the raw data file. This can be taken and filled in so pipeline can work for anyone. Schema/description below.

|      date      |                    activity                    |             distance             |               time              |       cumulative_distance      |       cumulative_time      |     cumulative_hours    |               %_of_10000               |            Notes            |
|:--------------:|:----------------------------------------------:|:--------------------------------:|:-------------------------------:|:------------------------------:|:--------------------------:|:-----------------------:|:--------------------------------------:|:---------------------------:|
| date type      | string type                                    | float                            | float                           | float                          | float                      | float                   | float                                  | string                      |
| Date of my run | What type of activity it was e.g run/intervals | Distance in metres e.g 5k = 5000 | time taken in minutes e.g 54.32 | sum of all cumulative distance | sum of all cumulative time | sum of cumulative hours | % of my hours compared to 10,000 hours | any notes that are relevant |
|                |                                                |                                  |                                 |                                |                            |                         |                                        |                             |

## Pipeline steps

The pipeline is broken down into three smaller scripts. All the input/output data paths can be changed in the config.properties file.

### Reading and Merging 
This reads in the raw dataset and merged with a datecolumn of all dates from the 12th October 2019 to the current day. A new dataset is outputted into the merged directory.

### Derived Variables
This reads in the merged file and creates derived variables to conduct analysis with. AN example is adding a day of the week marker. A new dataset is outputted into the processed directory.

### Analysis
This reads in the processed data and creates all the charts automatically saving them into the anlysis folder.

## Running the Pipeline
This can either be run directly by running each python script for each step mentioned previously. If you are a windows user there are .bat files which can be executed to trigger the scripts. 
