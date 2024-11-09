#!/usr/bin/env python3
################# By Abdelbari Bahadi ###########################################################
##################################################################################################
print("==========Welcome To UnivMoyenneCalculator==========")
print("==========Please fill all given marks==========")
##################################################################################################
ETUD_FirstName=str(input("Please Enter Your First Name : "))
ETUD_LastName=str(input("Please Enter Your Last Name  : "))
##################################################################################################
UEF_1_TD=float(input("Please Enter Systèmes à Microprocesseurs TD : "))
UEF_1_Exam=float(input("Please Enter Systèmes à Microprocesseurs Exam(Cours) : "))

UEF_2_TD=float(input("Please Enter Fonctions de l’Ézzzzzlectronique TD : "))
UEF_2_Exam=float(input("Please Enter Fonctions de l’Électronique Exam(Cours) : "))

UEF_3_TD=float(input("Please Enter Traitement du signal TD : "))
UEF_3_Exam=float(input("Please Enter Traitement du signal Exam(Cours) : "))

UEF_4_TD=float(input("Please Enter Réseaux informatiques locaux TD : "))
UEF_4_Exam=float(input("Please Enter Réseaux informatiques locaux Exam(Cours) : "))
##################################################################################################
UEM_1_TP=float(input("Please Enter TP Systèmes à Microprocesseurs TP : "))

UEM_2_TP=float(input("Please Enter TP Fonctions de l’Électronique TP : "))

UEM_3_TP=float(input("Please Enter TP Signal et Réseaux locaux TP : "))

UEM_4_TP=float(input("Please Enter Travaux avant-Projet TP : "))
UEM_4_Exam=float(input("Please Enter Travaux avant-Projet Exam(Cours) : "))
##################################################################################################
UED_1_Exam=float(input("Please Enter Technologie des composants électroniques 2 Exam(Cours) : "))
UED_2_Exam=float(input("Please Enter Propagation d’ondes et Antennes Exam(Cours) : "))
##################################################################################################
UET_1_Exam=float(input("Please Enter Technologie et fabrication des circuits intégrés(Cours) : "))
##################################################################################################
print("==========Please wait while generating your Relevé de Notes==========")
##################################################################################################
UEF_1_Moy = ( UEF_1_TD * 0.4 ) + ( UEF_1_Exam * 0.6 )                                            #                                                                                                
UEF_2_Moy = ( UEF_2_TD * 0.4 ) + ( UEF_2_Exam * 0.6 )                                            #                                                                                                 
UEF_3_Moy = ( UEF_3_TD * 0.4 ) + ( UEF_3_Exam * 0.6 )                                            #                                                                                                 
UEF_4_Moy = ( UEF_4_TD * 0.4 ) + ( UEF_4_Exam * 0.6 )                                            #   
##################################################################################################
UEM_1_Moy = UEM_1_TP                                                                             #
UEM_2_Moy = UEM_2_TP                                                                             #
UEM_3_Moy = UEM_3_TP                                                                             # 
UEM_4_Moy = (UEM_4_TP * 0.4) + (UEM_4_Exam * 0.6)                                                #
##################################################################################################
UED_1_Moy = UED_1_Exam                                                                           #
UED_2_Moy = UED_2_Exam                                                                           #
##################################################################################################
UET_1_Moy = UET_1_Exam                                                                           #
##################################################################################################
#Declaring Signle Module Coef
UEF_1_Coef = 3
UEF_2_Coef = 2
UEF_3_Coef = 2
UEF_4_Coef = 2
UEM_1_Coef = 1
UEM_2_Coef = 1
UEM_3_Coef = 1
UEM_4_Coef = 2
UED_1_Coef = 1
UED_2_Coef = 1
UET_1_Coef = 1
#Declaring Signle Module Crédits
UEF_1_Crdt = 6
UEF_2_Crdt = 4
UEF_3_Crdt = 4
UEF_4_Crdt = 4
UEM_1_Crdt = 2
UEM_2_Crdt = 2
UEM_3_Crdt = 2
UEM_4_Crdt = 3
UED_1_Crdt = 1
UED_2_Crdt = 1
UET_1_Crdt = 1
#Declaring Whole U.E Crédits & Coef
UEF_Coef = UEF_1_Coef + UEF_2_Coef + UEF_3_Coef + UEF_4_Coef
UEF_Crdt = UEF_1_Crdt + UEF_2_Crdt + UEF_3_Crdt + UEF_4_Crdt
UEF_Crdt_F_C = 0
UEM_Coef = UEM_1_Coef + UEM_2_Coef + UEM_3_Coef + UEM_4_Coef
UEM_Crdt = UEM_1_Crdt + UEM_2_Crdt + UEM_3_Crdt + UEM_4_Crdt
UEM_Crdt_F_C = 0
UED_Coef = UED_1_Coef + UED_2_Coef
UED_Crdt = UED_1_Crdt + UED_2_Crdt
UED_Crdt_F_C = 0
UET_Coef = UET_1_Coef
UET_Crdt = UET_1_Crdt
UET_Crdt_F_C = 0
##################################################################################################
UEF_COEF_SUM = UEF_1_Coef + UEF_2_Coef + UEF_3_Coef + UEF_4_Coef
UEF_Moy_SUM = (UEF_1_Moy * UEF_1_Coef)+(UEF_2_Moy * UEF_2_Coef)+(UEF_3_Moy * UEF_3_Coef)+(UEF_4_Moy * UEF_4_Coef)
UEF_Moy = (UEF_Moy_SUM / UEF_COEF_SUM)
##################################################################################################
UEM_COEF_SUM = UEM_1_Coef + UEM_2_Coef + UEM_3_Coef + UEM_4_Coef
UEM_Moy_SUM = (UEM_1_Moy * UEM_1_Coef)+(UEM_2_Moy * UEM_2_Coef)+(UEM_3_Moy * UEM_3_Coef)+(UEM_4_Moy * UEM_4_Coef)
UEM_Moy = (UEM_Moy_SUM / UEM_COEF_SUM)
##################################################################################################
UED_COEF_SUM = UED_1_Coef + UED_2_Coef
UED_Moy_SUM = (UED_1_Moy * UED_1_Coef)+(UED_2_Moy * UED_2_Coef)
UED_Moy = (UED_Moy_SUM / UED_COEF_SUM)
##################################################################################################
UET_COEF_SUM = UET_1_Coef
UET_Moy_SUM = (UET_1_Moy * UET_1_Coef)
UET_Moy = (UET_Moy_SUM / UET_COEF_SUM)
##################################################################################################
SEMESTRE_5_Coef_Sum = UEF_COEF_SUM + UEM_COEF_SUM + UED_COEF_SUM + UET_COEF_SUM
SEMESTRE_5_UE_Moy_Sum = (UEF_Moy * UEF_COEF_SUM) + (UEM_Moy * UEF_COEF_SUM) + (UED_Moy * UED_COEF_SUM) + (UET_Moy * UET_COEF_SUM)
SEMESTRE_5_Moy = SEMESTRE_5_UE_Moy_Sum / SEMESTRE_5_Coef_Sum
##################################################################################################
def UEF_1_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEF_1_Crdt
    elif M_Moy < 10.00:
        return 0
def UEF_2_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEF_2_Crdt
    elif M_Moy < 10.00:
        return 0
def UEF_3_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEF_3_Crdt
    elif M_Moy < 10.00:
        return 0
def UEF_4_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEF_4_Crdt
    elif M_Moy < 10.00:
        return 0
                        ###############################################  
def UEM_1_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEM_1_Crdt
    elif M_Moy < 10.00:
        return 0
def UEM_2_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEM_2_Crdt
    elif M_Moy < 10.00:
        return 0
def UEM_3_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEM_3_Crdt
    elif M_Moy < 10.00:
        return 0
def UEM_4_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UEM_4_Crdt
    elif M_Moy < 10.00:
        return 0        
                        ###############################################  
def UED_1_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UED_1_Crdt
    elif M_Moy < 10.00:
        return 0
def UED_2_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UED_2_Crdt
    elif M_Moy < 10.00:
        return 0
                        ###############################################  
def UET_1_Crdt_F(M_Moy):
    if M_Moy >= 10.00:
        return UET_1_Crdt
    elif M_Moy < 10.00:
        return 0               
##################################################################################################
def UEF_Crdt_F(UE_Moy):
    if UE_Moy >= 10.00:
      return UEF_Crdt
    elif UE_Moy < 10.00:
        UEF_Ms_Moys = [UEF_1_Moy,UEF_2_Moy,UEF_3_Moy,UEF_4_Moy]
        UEF_Ms_Crdt = [UEF_1_Crdt,UEF_2_Crdt,UEF_3_Crdt,UEF_4_Crdt]
        uef_ms_crdt_l = []
        for UEF_M_Moy,UEF_M_Crdt in zip(UEF_Ms_Moys,UEF_Ms_Crdt):
            if UEF_M_Moy >= 10.00:
                uef_ms_crdt_l.append(UEF_M_Crdt)
            elif UEF_M_Moy < 10.00:
                uef_ms_crdt_l.append(0)
        return  sum(uef_ms_crdt_l)
def UEM_Crdt_F(UE_Moy):
    if UE_Moy >= 10.00:
      return UEM_Crdt
    elif UE_Moy < 10.00:
        UEM_Ms_Moys = [UEM_1_Moy,UEM_2_Moy,UEM_3_Moy,UEM_4_Moy]
        UEM_Ms_Crdt = [UEM_1_Crdt,UEM_2_Crdt,UEM_3_Crdt,UEM_4_Crdt]
        uem_ms_crdt_l = []
        for UEM_M_Moy,UEM_M_Crdt in zip(UEM_Ms_Moys,UEM_Ms_Crdt):
            if UEM_M_Moy >= 10.00:
                uem_ms_crdt_l.append(UEM_M_Crdt)
            elif UEM_M_Moy < 10.00:
                uem_ms_crdt_l.append(0)
        return  sum(uem_ms_crdt_l)
def UED_Crdt_F(UE_Moy):
    if UE_Moy >= 10.00:
      return UED_Crdt
    elif UE_Moy < 10.00:
        UED_Ms_Moys = [UED_1_Moy,UED_2_Moy]
        UED_Ms_Crdt = [UED_1_Crdt,UED_2_Crdt]
        ued_ms_crdt_l = []
        for UED_M_Moy,UED_M_Crdt in zip(UED_Ms_Moys,UED_Ms_Crdt):
            if UED_M_Moy >= 10.00:
                ued_ms_crdt_l.append(UED_M_Crdt)
            elif UED_M_Moy < 10.00:
                ued_ms_crdt_l.append(0)
        return  sum(ued_ms_crdt_l)
def UET_Crdt_F(UE_Moy):
    if UE_Moy >= 10.00:
      return UET_Crdt
    elif UE_Moy < 10.00:
        UET_Ms_Moys = [UET_1_Moy]
        UET_Ms_Crdt = [UET_1_Crdt]
        uet_ms_crdt_l = []
        for UET_M_Moy,UET_M_Crdt in zip(UET_Ms_Moys,UET_Ms_Crdt):
            if UET_M_Moy >= 10.00:
                uet_ms_crdt_l.append(UET_M_Crdt)
            elif UET_M_Moy < 10.00:
                uet_ms_crdt_l.append(0)
        return  sum(uet_ms_crdt_l)
##################################################################################################
SEMESTRE_5_Crdt = UEF_Crdt_F(UEF_Moy) + UEM_Crdt_F(UEM_Moy) + UED_Crdt_F(UED_Moy) + UET_Crdt_F(UET_Moy)

##################################################################################################
File = """
<!DOCTYPE html>
<html>
<head>
	<title>ELN_L3_SEMESTRE5_MoyenneCalculator</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background-color:rgb(42,42,46);">
	<div style="width:1251px;height:520px;margin:auto;background:white;">
	
		<p style="text-align:center;font-family:Times New Roman,Times,serif;">Ahmed Draia University of Adrar</p>
		
		<pre style="text-align:center;font-family:Times New Roman,Times,serif;">Sciences et Technologies	Électronique	L3	Semestre 5	</pre>	
		
		<h2 style="text-align:center;font-family:"Times New Roman",Times,serif;">Relevé de Notes de {} {}</h2>
		

		<div class = "Wrapper">
			<table border = "1" width="100%";">
				<tr>
					<th colspan = "5">Unités d'enseignement (U.E)</th>
					<th colspan = "8">Matiére constitutive de l'unité d'enseignement</th>
				</tr>
				<tr>
					<th>Unités d'enseignement</th>
					<th>Crédits</th>
					<th>Coef</th>
					<th>Moy</th>
					<th>Crédits Accumulé</th>
					<th>Matiére</th>
					<th>Crédits</th>
					<th>Coef</th>
					<th>TD</th>
					<th>TP</th>
					<th>Exam(Cours)</th>
					<th>Moy</th>
					<th>Crédits Accumulé</th>
				</tr>
				<tr>
					<th rowspan="4" >U.E.F</th>
					<th rowspan="4" >18</th>
					<th rowspan="4" >9</th>
					<th rowspan="4" >{}</th>
					<th rowspan="4" >{}</th>
					<th>Systèmes à Microprocesseurs</th>
					<th>6</th>
					<th>3</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>Fonctions de l’Électronique</th>
					<th>4</th>
					<th>2</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>Traitement du signal</th>
					<th>4</th>
					<th>2</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>Réseaux informatiques locaux</th>
					<th>4</th>
					<th>2</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th rowspan="4">U.E.M</th>
					<th rowspan="4">9</th>
					<th rowspan="4">5</th>
					<th rowspan="4">{}</th>
					<th rowspan="4">{}</th>
					<th>TP Systèmes à Microprocesseurs</th>
					<th>2</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>TP Fonctions de l’Électronique</th>
					<th>2</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>TP Signal et Réseaux locaux</th>
					<th>2</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>Travaux avant-Projet</th>
					<th>3</th>
					<th>2</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th rowspan="2">U.E.D</th>
					<th rowspan="2">2</th>
					<th rowspan="2">2</th>
					<th rowspan="2">{}</th>
					<th rowspan="2">{}</th>
					<th>Technologie des composants électroniques 2</th>
					<th>1</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>Propagation d’ondes et Antennes</th>
					<th>1</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tr>
					<th>U.E.T</th>
					<th>1</th>
					<th>1</th>
					<th>{}</th>
					<th>{}</th>
					<th>Technologie et fabrication des circuits intégrés</th>
					<th>1</th>
					<th>1</th>
					<th bgcolor="black">N/A</th>
					<th bgcolor="black">N/A</th>
					<th>{}</th>
					<th>{}</th>
					<th>{}</th>
				</tr>
				<tfoot>
					<th colspan = "13" >Moyenne du Semestre 5 : {} <br> Crédits du Semestre 5 : {} </th>
				</tfoot>
			</table>
			<br>
			  &Tab;
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
""".format(
    ETUD_FirstName,
    ETUD_LastName,
    round(UEF_Moy,2),
    UEF_Crdt_F(UEF_Moy),
    UEF_1_TD,
    UEF_4_Exam,
    round(UEF_1_Moy,2),
    UEF_1_Crdt_F(UEF_1_Moy),
    UEF_2_TD,
    UEF_4_Exam,
    round(UEF_2_Moy,2),
    UEF_2_Crdt_F(UEF_2_Moy),
    UEF_3_TD,
    UEF_4_Exam,
    round(UEF_3_Moy,2),
    UEF_3_Crdt_F(UEM_3_Moy),
    UEF_4_TD,
    UEF_4_Exam,
    round(UEF_4_Moy,2),
    UEF_4_Crdt_F(UEF_4_Moy),
    round(UEM_Moy,2),
    UEM_Crdt_F(UEM_Moy),
    UEM_1_TP,
    round(UEM_1_Moy,2),
    UEM_1_Crdt_F(UEM_1_Moy),
    UEM_2_TP,
    round(UEM_2_Moy,2),
    UEM_2_Crdt_F(UEM_2_Moy),
    UEM_3_TP,
    round(UEM_3_Moy,2),
    UEM_3_Crdt_F(UEM_3_Moy),
    UEM_4_TP,
    UEM_4_Exam,
    round(UEM_4_Moy,2),
    UEM_4_Crdt_F(UEM_4_Moy),
    round(UED_Moy,2),
    UED_Crdt_F(UED_Moy),
    UED_1_Exam,
    round(UED_1_Moy,2),
    UED_1_Crdt_F(UED_1_Moy),
    UED_2_Exam,
    round(UED_2_Moy,2),
    UED_2_Crdt_F(UED_2_Moy),
    round(UET_Moy,2),
    UET_Crdt_F(UET_Moy),
    UET_1_Exam,
    round(UET_Moy,2),
    UET_1_Crdt_F(UET_1_Moy),
    round(SEMESTRE_5_Moy,2),
    SEMESTRE_5_Crdt,
           )
OutputFile = open('ELN_L3_SEMESTRE5_MoyenneCalculator_OutputFile.html','w')
OutputFile.write(File)
OutputFile.close()
