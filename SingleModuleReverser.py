#!/usr/bin/env python3
################################By Abdelbari Bahadi###########################################
print("==========Welcome To SingleModuleReverse==========")
print("==========Please fill given marks as available==========")
#################################################################################################
UEF_1_TD = input("Please Enter Systèmes à Microprocesseurs TD : ")#Variable which holds UEF_1_TD value
UEF_1_Exam = input("Please Enter Systèmes à Microprocesseurs Exam(Cours) : ")#Variable which holds UEF_1_Exam value
UEF_1_Moy = None #an empty variable which will used later in holding the UEF_1_Moy value
TD_Possible_Marks = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.25, 16.5, 16.75, 17.0, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5, 18.75, 19.0, 19.25, 19.5, 19.75, 20.0]
Exam_Possible_Marks = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.25, 16.5, 16.75, 17.0, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5, 18.75, 19.0, 19.25, 19.5, 19.75, 20.0]
#################################################################################################
#1.if both TD and Exam marks get inputted then it will calculate the GPA Based on previously given formula "formula =( TD * 0.4 ) + (Exam * 0.6)"(1) 
if(UEF_1_TD != "" ) and ( UEF_1_Exam != "" ): 
    UEF_1_TD = round(float(UEF_1_TD),2)
    UEF_1_Exam = round(float(UEF_1_Exam),2)
    UEF_1_Moy = round(( UEF_1_TD * 0.4 ) + (UEF_1_Exam * 0.6),2)
    UEF_1_Crdt = 0
    if UEF_1_Moy >= 10.00:
        UEF_1_Crdt = 6 
    elif UEF_1_Moy < 10.00:
        UEF_1_Crdt = 0
    FILE = """<!DOCTYPE html>
    <html>
    <head>
    <title>SingleModuleReverser</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="background-color:rgb(42,42,46);">
        <div style="width:1251px;height:213px;margin:auto;background:white;">
            <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
            <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
            <div class = "Wrapper">
                <table border = "1" width="100%";">
                    <tr>
                        <th colspan = "1">Module d'enseignement (U.E)</th>
                        <th colspan = "7">Ses détails</th>
                    </tr>
                    <tr>
                        <th rowspan="2">Systèmes à Microprocesseurs</th>
                        <th>Crédits</th>
                        <th>Coef</th>
                        <th>TD</th>
                        <th>TP</th>
                        <th>Exam(Cours)</th>
                        <th>Moy</th>
                        <th>Crédits Accumulé</th>
                    </tr>
                    <tr>
                        <th>6</th>
                        <th>3</th>
                        <th>{}</th>
                        <th bgcolor="black">N/A</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        </tr>
                </table>
                    <br>
                <table border="0" style="border-collapse:collapse;margin-left:5px;">
                    <tr>
                        <td bgcolor="black">N/A</td>
                        <td>Ce façon de évalutaion n'est exite pas.</td>
                     </tr>
                </table>
            </div>
       </div>
    </body>
    </html> 
     """.format(UEF_1_TD,
                UEF_1_Exam,
                UEF_1_Moy,
                UEF_1_Crdt,
                )
    OutputFile = open('SingleModuleReverser_TD_and_Exam_given.html','w')
    OutputFile.write(FILE)
    OutputFile.close()
#################################################################################################
#2.if both TD and Exam marks are not present and Moy is then the function will calculate all possible TD and Exam marks based on a given formula " Moy = ( TD * 0.4 ) + ( Exam * 0.6 ) " and it will output results in HTMML file
elif ( UEF_1_TD == "" ) and ( UEF_1_Exam == "" ):
    UEF_1_Moy=input("Please Enter GPA of this Module : ")
    if ( UEF_1_Moy != "" ):
        UEF_1_Moy = float(UEF_1_Moy)
        uef_1_decision_2_1_body = []
        for TD_Mark in TD_Possible_Marks:
            for Exam_Mark in Exam_Possible_Marks:
                if((TD_Mark * 0.4 )+(Exam_Mark * 0.6) == UEF_1_Moy):
                    uef_1_decision_2_1_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(TD_Mark,Exam_Mark,UEF_1_Moy,6 if UEF_1_Moy >= 10.00 else 0)
                                              )
        def output_file_content_f(list):
            output_file_content = ''.join(list)
            output_file_content_error = """<div style="width:1251px;height:213px;margin:auto;background:white;">
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
                <h1 style="text-align:center;font-family:"Times New Roman",Times,serif;">impossible de générer <br>des notes TD et d'examen <br> pour votre moyenne donnée {}</h1>	
            </div>
        <br>""".format(UEF_1_Moy,)
            if ( output_file_content != "" ):
                return output_file_content
            elif ( output_file_content == "" ):
                return output_file_content_error
                                         
        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content_f(uef_1_decision_2_1_body))
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
    elif ( UEF_1_Moy == "" ):
        uef_1_decision_2_1_body = []
        for TD_Mark in TD_Possible_Marks:
            for Exam_Mark in Exam_Possible_Marks:
                Moy = round((TD_Mark * 0.4 )+(Exam_Mark * 0.6),2)
                uef_1_decision_2_1_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(TD_Mark,Exam_Mark,Moy,6 if Moy >= 10.00 else 0)
                                              )
            
        output_file_content = ''.join(uef_1_decision_2_1_body)

        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content,)
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
#################################################################################################               
elif ( UEF_1_TD == "" ) and ( UEF_1_Exam != "" ):#If TD == "" and Exam != "" : (if Exam mark get inputted and TD mark not)
    UEF_1_Moy=input("Please Enter GPA of this Module : ")
    if ( UEF_1_Moy != "" ):
        UEF_1_Moy = float(UEF_1_Moy)
        UEF_1_Exam = float(UEF_1_Exam)
        uef_1_decision_3_1_body = []
        for TD_Mark in TD_Possible_Marks:
            if ( TD_Mark == ( UEF_1_Moy - (UEF_1_Exam * 0.6)) / 0.4  ):
                uef_1_decision_3_1_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(TD_Mark,UEF_1_Exam,UEF_1_Moy,6 if UEF_1_Moy >= 10.00 else 0))
        def output_file_content_f_2(list):
            output_file_content = ''.join(list)
            output_file_content_error = """<div style="width:1251px;height:213px;margin:auto;background:white;">
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
                <h1 style="text-align:center;font-family:"Times New Roman",Times,serif;">impossible de générer <br>la note TD pour votre examen : {} <br> et votre moyenne {} donnée </h1>	
            </div>
        <br>""".format(UEF_1_Exam,UEF_1_Moy,)
            if ( output_file_content != "" ):
                return output_file_content
            elif ( output_file_content == "" ):
                return output_file_content_error
                                         
        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content_f_2(uef_1_decision_3_1_body))
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
        
    elif ( UEF_1_Moy == "" ):
        UEF_1_Exam = float(UEF_1_Exam)
        uef_1_decision_3_2_body = []
        for TD_Mark in TD_Possible_Marks:
            UEF_1_Moy = ( TD_Mark * 0.4 )+(UEF_1_Exam * 0.6) 
            uef_1_decision_3_2_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(TD_Mark,UEF_1_Exam,UEF_1_Moy,6 if UEF_1_Moy >= 10.00 else 0))
        output_file_content = ''.join(uef_1_decision_3_2_body)
        
        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content,)
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
#################################################################################################
elif ( UEF_1_TD != "" ) and ( UEF_1_Exam == "" ):
    UEF_1_Moy=input("Please Enter GPA of this Module : ")
    if ( UEF_1_Moy != "" ):
        UEF_1_Moy = float(UEF_1_Moy)
        UEF_1_TD = float(UEF_1_TD)
        uef_1_decision_4_1_body = []
        for Exam_Mark in Exam_Possible_Marks:
            if ( Exam_Mark == ( UEF_1_Moy - (UEF_1_TD * 0.4)) / 0.6  ):
                uef_1_decision_4_1_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(UEF_1_TD,Exam_Mark,UEF_1_Moy,6 if UEF_1_Moy >= 10.00 else 0))
        def output_file_content_f_3(list):
            output_file_content = ''.join(list)
            output_file_content_error = """<div style="width:1251px;height:213px;margin:auto;background:white;">
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
                <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
                <h1 style="text-align:center;font-family:"Times New Roman",Times,serif;">impossible de générer <br>la note Exam pour votre TD : {} <br> et votre moyenne {} donnée </h1>	
            </div>
        <br>""".format(UEF_1_TD,UEF_1_Moy,)
            if ( output_file_content != "" ):
                return output_file_content
            elif ( output_file_content == "" ):
                return output_file_content_error
                                         
        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content_f_3(uef_1_decision_4_1_body))
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
    elif ( UEF_1_Moy == "" ):
        UEF_1_TD = float(UEF_1_TD)
        uef_1_decision_4_2_body = []
        for Exam_Mark in Exam_Possible_Marks:
            UEF_1_Moy = ( Exam_Mark * 0.4 )+(UEF_1_TD * 0.6) 
            uef_1_decision_4_2_body.append("""<div style="width:1251px;height:213px;margin:auto;background:white;">
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de un Etudiant</h2>
        <h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Module : Systèmes à Microprocesseurs</h2>
        <table border = "1" width="100%";">
            <tr>
                <th colspan = "1">Module d'enseignement (U.E)</th>
                <th colspan = "7">Ses détails</th>
            </tr>
            <tr>
                <th rowspan="2">Systèmes à Microprocesseurs</th>
                <th>Crédits</th>
                <th>Coef</th>
                <th>TD</th>
                <th>TP</th>
                <th>Exam(Cours)</th>
                <th>Moy</th>
                <th>Crédits Accumulé</th>
            </tr>
            <tr>
                <th>6</th>
                <th>3</th>
                <th>{}</th>
                <th bgcolor="black">N/A</th>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        </table>
        <br>
        <table border="0" style="border-collapse:collapse;margin-left:5px;">
            <tr>
                <td bgcolor="black">N/A</td><td>Ce façon de évalutaion n'est exite pas.</td>
            </tr>   
        </table>
    </div>
    <br>""".format(UEF_1_TD,Exam_Mark,round(UEF_1_Moy,2),6 if UEF_1_Moy >= 10.00 else 0))
        output_file_content = ''.join(uef_1_decision_4_2_body)
        
        OutputFileWrapper = """<!DOCTYPE html>
    <html>
        <head>
            <title>SingleModuleReverser</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color:rgb(42,42,46);">
        {}
        </body>
    </html>""".format(output_file_content,)
        OutputFile = open('SingleModuleReverser.html','w')
        OutputFile.write(OutputFileWrapper)
        OutputFile.close()
