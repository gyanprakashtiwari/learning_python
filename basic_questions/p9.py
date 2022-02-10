exam_st_date = input("Enter exam date\n")
exam_st_date = exam_st_date[1:]
date  = exam_st_date.strip()

print(exam_st_date)
exam_st_date = exam_st_date[0:len(exam_st_date)-1]




date  = exam_st_date.split(",")

print(" The examination will start from : " + date[0] + "/" + date[1] + "/" + date[2])
