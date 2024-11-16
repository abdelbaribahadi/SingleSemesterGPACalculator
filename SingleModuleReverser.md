# SingleModuleReverser
-->SingleModuleReverser.py os the first block of my future project called SingleSemesterReverser which will do same thing like this script but in larger scale around a single SEMES
-->TD_Possible_Marks and Exam_Possible_Marks are a lists which contain all possible marks of both Exam and TD and the counting will start from 0.00 to 20.00 by 0.25 as an increment
//All Cases Explained:
1-) the first case is when the user input consist of TD and Exam mark then it will calculate GPA in a normal way
2-) the second case is when the user input doesn't contain TD and Exam mark then a request will be made of entering GPA mark then :
*-if the user inserted a GPA mark then the software will calculate all possible marks of TD and Exam from their lists mentioned above and it will choose only correct ones 
to output them in an HTML file and if it didn't find any correct ones it will output an error HTML file
*-if the user didn't inserted a GPA mark then the software will calculate all possible marks of TD and Exam from their lists mentioned above and output all possible results in a HTML file
3-)the third case is when the user input consist of only Exam mark then it will branch into two sub-cases:
*-if the user inserted a GPA mark then the software will calculate all possible marks TD marks that prove the formula of GPA right and it will output them into an html file
*-if the user didn't inserted a GPA mark then the software will calculate all possible TD marks and  their fellow GPA results and also output them into an HTML file
4-)the fourth case is when the user input consist of only TD mark then it will branch into two sub-cases:
*-if the user inserted a GPA mark then the software will calculate all possible marks Exam marks that prove the formula of GPA right and it will output them into an html file
*-if the user didn't inserted a GPA mark then the software will calculate all possible Exam marks and  their fellow GPA results and also output them into an HTML file
