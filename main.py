import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load data
resume = docx2txt.process("./resume-sample.docx")
job_description = docx2txt.process("job-sample.docx")

#A list of text
text = [resume, job_description]

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

#print similarity matrix
print("\nSimilarity Score: ")
print(cosine_similarity(count_matrix))


#get the match percentage
matchPercentage = cosine_similarity(count_matrix)[0][1]*100
matchPercentage = round(matchPercentage,2) # round to two decimal places

print("your resume matches about "+ str(matchPercentage) + "% of the job description")


