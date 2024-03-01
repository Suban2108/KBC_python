questions = [
    [
        "Which team won the first-ever IPL season in 2008?",
        "Rajasthan Royals",
        "Mumbai Indians",
        "Chennai Super Kings",
        "Kolkata Knight Riders",
        "None of the above",
        1
    ],
    [
        "Who is the highest run-scorer in the history of IPL as of 2022?",
        "Virat Kohli",
        "Rohit Sharma",
        "Suresh Raina",
        "David Warner",
        "None of the above",
        1
    ],
    [
        "Which player has taken the most wickets in IPL history as of 2022?",
        "Lasith Malinga",
        "Sunil Narine",
        "Imran Tahir",
        "Dwayne Bravo",
        "None of the above",
        1
    ],
    [
        "In which year did the IPL introduce the 'Strategic Timeout'?",
        "2019",
        "2018",
        "2017",
        "2016",
        "None of the above",
        2
    ],
    [
        "Which team holds the record for the highest team total in an IPL match?",
        "Royal Challengers Bangalore",
        "Kolkata Knight Riders",
        "Mumbai Indians",
        "Chennai Super Kings",
        "None of the above",
        1
    ],
    [
        "Who was the most expensive player in the IPL 2021 auction?",
        "Chris Morris",
        "Glenn Maxwell",
        "Kyle Jamieson",
        "Jhye Richardson",
        "None of the above",
        1
    ],
    [
        "Which city hosted the final match of IPL 2020?",
        "Dubai",
        "Abu Dhabi",
        "Sharjah",
        "Mumbai",
        "None of the above",
        4
    ],
    [
        "Who holds the record for the fastest century in IPL history?",
        "Chris Gayle",
        "AB de Villiers",
        "David Warner",
        "KL Rahul",
        "None of the above",
        1
    ],
    [
        "Which team has won the most IPL titles as of 2022?",
        "Mumbai Indians",
        "Chennai Super Kings",
        "Kolkata Knight Riders",
        "Rajasthan Royals",
        "None of the above",
        1
    ],
    [
        "Who was the leading wicket-taker in the IPL 2021 season?",
        "Harshal Patel",
        "Amit Mishra",
        "Kagiso Rabada",
        "Rashid Khan",
        "None of the above",
        1
    ],
    [
        "Which player has won the 'Orange Cap' for scoring the most runs in IPL history?",
        "David Warner",
        "Chris Gayle",
        "Virat Kohli",
        "Suresh Raina",
        "None of the above",
        3
    ],
    [
        "Who was the captain of the winning team in IPL 2019?",
        "Rohit Sharma",
        "MS Dhoni",
        "Virat Kohli",
        "Shreyas Iyer",
        "None of the above",
        1
    ],
    [
        "In which season was the IPL expanded to include 10 teams?",
        "2022",
        "2021",
        "2020",
        "2019",
        "None of the above",
        2
    ],
    [
        "Who was the first player to score a century in IPL history?",
        "Brendon McCullum",
        "Sachin Tendulkar",
        "Chris Gayle",
        "Adam Gilchrist",
        "None of the above",
        1
    ],
    [
        "Which team won the IPL 2021 season?",
        "Chennai Super Kings",
        "Kolkata Knight Riders",
        "Delhi Capitals",
        "Mumbai Indians",
        "None of the above",
        1
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{questions[i][0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")