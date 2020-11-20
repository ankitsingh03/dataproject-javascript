# dataproject-javascript

##Aim
To convert raw data with the help of python and present it in HTML page, use the HighCharts JavaScript Lib for plotting.

## Project Requirements
Python version should be more then 3.5+

## How To Get Data
- To download the data [click here](https://www.kaggle.com/manasgarg/ipl/version/5). Here you will get two data files.
- Third data file is present in project itself.
- copy and paste all three data files in `py_file`


## How To Run
1. It is deployed on [Heroku](https://data-plot-js.herokuapp.com/)
1. Download the zip file and extract it in your system. Open `index.html` file in your browser.

#### If your graph is not working or .json file have no data in it then follow this.
1. open the `py_file`
1. Run all the `.py` file in you system.
1. It will put the data from `csv` to `assets/*.json file`.
1. Now, you are ready to run `index.html`

#### Graph 1: Foreign umpire analysis
- Obtain a source for country of origin of umpires. Plot a chart between number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.

#### Graph 2: Top batsman for Royal Challengers Bangalore
- Considered only games played by Royal Challengers Bangalore. Plot between total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.

#### Graph 3: Total runs scored by team
- Plot a chart between total runs scored by each teams over the history of IPL. Hint: use the total_runs field.

#### Graph 4: Stacked chart of matches played by team by season

- Plot a stacked bar chart of :
- Number of games played
- By team
- By season
