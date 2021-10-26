# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:58:23 2021

@author: HP Envy
"""
with open("sporsmaalsfilen.txt", "r", encoding="UTF8") as file:
    questions = list()
    correct = list()
    options = list()
    for line in file:
        elements = line.split(":")
        elements = [element.strip() for element in elements]
        questions.append(elements[0])
        correct.append(elements[1])
        options.append(elements[2])
    options = [i.strip('][').split(', ') for i in options]
    # data = [questions, correct, options]
    
class Quiz:
    def __init__(self, correct_answer, correct_answer_index, options):
        self.correct_answer = correct_answer
        self.correct_answer_index = correct_answer_index
        self.options = options
    
    def korrekt_svar_tekst(self):
        return print("\nKorrekt svar: ", self.correct_answer)
    
    def check1(self, answer1, answer2):
        if answer1 == self.correct_answer_index:
            print("\nSpelare 1: Korrekt")

        if answer1 != self.correct_answer_index:
            print("\nSpelare 1: Fel")

        if answer2 == self.correct_answer_index: 
            print("\nSpelare 2: Korrekt")

        if answer2 != self.correct_answer_index:
            print("\nSpelare 2: Fel")
   
            
    def __str__(self):
        options = list()
        for index, option in enumerate(self.options):
            if index == 0:
                option = "1. " + option
                options.append(option)
            else:
                option = f"\n{1+index}. " + option
                options.append(option)
        options = "".join(options)
        return f"{options}"
    
if __name__ == "__main__":
    score1 = 0
    score2 = 0
    for index, question in enumerate(questions):
        print("-------------------------------------------------------\n" + question)
        correct_index = int(correct[index])
        start = Quiz(options[index][correct_index], correct_index + 1, options[index])
        print(start)
        answer1 = int(input("Välj ett svarsalternativ för spelare 1: "))
        answer2 = int(input("Välj ett svarsalternativ för spelare 2: "))
        start.korrekt_svar_tekst()
        start.check1(answer1, answer2)
        
        if answer1 == correct_index + 1:
            score1 += 1
            
        if answer2 == correct_index + 1:
            score2 += 1
            
        if index == len(questions) - 1:
            print("Spelare 1 fick", score1, "rätt utav /" + str(len(questions)))
            print("Spelare 2 fick", score2, "rätt utav /" + str(len(questions)))
        
    