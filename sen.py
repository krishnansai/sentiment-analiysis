from sentiment_analysis_spanish import sentiment_analysis


print("English:Press(1) ")
print("spanish:Press(2) ")
opction=int(input("Choose The opction : "))
if(opction==2):
    sentiment1=sentiment_analysis.SentimentAnalysisSpanish()

    span=input("say something in spanish : ")
    print("")
    print("")
    span_ans=(sentiment1.sentiment(span))
    #"me gusta la tombola es genial"
    if(span_ans >= 0.60):
        print("It is an positive words")
    elif(span_ans >=0.10 ):
        print("It is a negative words")

    

elif(opction==1):
    sentence = input("Say Something : ")
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()

    score=sid.polarity_scores(sentence)
    #print(score)

    values=score.values()

    values_list=list(values)
    #print(values_list)
    print("")
    print("")


    if(values_list[0]>0):
        print("it is a negative words ")
    elif(values_list[1]>0):
        print("it is a neutral words ")
    elif(values_list[1]>0 and values_list[2]>0):
        print("it is a common words")
    elif(values_list[2]>0):
        print("This is a  positive words ")
        
