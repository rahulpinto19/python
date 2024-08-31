questions = [
    ["Which lang was used to create fb", "javascript", "html", "php", "none", 4],
    ["What does HTML stand for?", "HyperText Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "none", 1],
    ["Which company created the Java programming language?", "Microsoft", "Apple", "Sun Microsystems", "none", 3],
    ["What is the correct syntax for a 'for' loop in Python?", "for i in range(5)", "for (i=0; i<5; i++)", "for i = 1 to 5", "none", 1],
    ["Which protocol is used to send emails?", "HTTP", "SMTP", "FTP", "none", 2],
    ["Which one is not a programming language?", "Python", "HTML", "JavaScript", "none", 2],
    ["What is the main function of the CPU?", "Store Data", "Process Data", "Move Data", "none", 2],
    ["Which of the following is a database management system?", "HTML", "CSS", "MySQL", "none", 3],
    ["Which company developed the Android operating system?", "Apple", "Microsoft", "Google", "none", 3],
    ["What is the name of the stylesheet language used for describing the presentation of a document written in HTML?", "HTML", "CSS", "JavaScript", "none", 2],
    ["What does SQL stand for?", "Structured Query Language", "Standard Query Language", "Simple Query Language", "none", 1],
    ["Which one is a NoSQL database?", "MySQL", "Oracle", "MongoDB", "none", 3],
    ["What does the acronym HTTP stand for?", "HyperText Transfer Protocol", "HyperTransfer Text Protocol", "HighText Transfer Protocol", "none", 1],
    ["Which language is primarily used for web development?", "Python", "JavaScript", "C++", "none", 2]
]



levels = [1000,2000,3000,5000,10000,20000,40000,80000,16000,32000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter your answer (1-4)"))
    if(reply == question[5]):
        print(f"Correct answer you have won Rs{levels[i]}")
        if i == 4:
            money = 10000
        elif i==9:
            money = 32000
        elif i==14:
            money = 10000000
    else:
        print("Wrong answer")
        break
    
print(f"your take home money is {money}")