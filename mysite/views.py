# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http  import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from .forms import *
import random, string
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import mygene
from mmap import mmap, ACCESS_READ
import itertools
from yattag import indent
import urllib
import fileinput
import ipdb
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.graph_objs import *
import cufflinks as cf
tls.set_credentials_file(username='greengageplum', api_key='2639ajlqmu')
import pandas as pd
from openpyxl.cell import get_column_letter
from compiler.ast import flatten
import zipfile
from StringIO import *
import os
import sys, time
# Organisms (Models)
from mysite.models import Hg38, Mm10, Dm3, Ce10, Rn6
from mysite.utils import *

# Create your views here.

def url_redirect(request):
    return HttpResponsePermanentRedirect("http://otulab.unl.edu:9000")

resultName = ''
resultName2 = ''

print "---- SYSTEM WARMING UP --------"
start = time.clock()
print "---- SYSTEM READY in %s ms-------- " % ((time.clock() - start)*1000)

#-------------------------------------------------------(CE10) GENE ID --> REFSEQ_ID ---> QUERY RESULTS ------------------------------------------------#
def ce10IDQuery(uploaded_file):    	
	mg = mygene.MyGeneInfo()
	IDList = uploaded_file.read().splitlines()
	Scope = 'symbol,entrezgene,ensembl.*,refseq.*,accession.*,unigene'
	MyScopes = 'symbol,entrezgene,ensembl.*,alias,refseq.*,accession.*,unigene,pdb,pfam,mim,reporter,go,hgnc'		
	MyFields = "refseq.rna"
	#qStart = time.clock()
	CE_Query = mg.querymany(IDList, scopes=Scope, fields=MyFields, species='nematode', returnall=True)
	outCE = CE_Query['out']
	
	#### GENE ID MAPPING outputs are read for querying ####
	refseqs = []
	for ls in outCE:
		if 'refseq.rna' in ls:
			refseq = ls['refseq.rna']
			if type(refseq) == list:
				refseq = refseq[0]
			refseqs.append(refseq)
		else:
			refseqs.append("NO HIT")
	########### For Results ###########		
	inputPKpair = zip(IDList, refseqs)

	
	inputPKpairNew = []
	notMappedGenes = []
	for i in inputPKpair:
		if i[1] == "NO HIT":
			notMappedGenes.append(i[0])
			continue
		else:
			inputPKpairNew.append(i)

	PKs = []
	InIDs = []
	for i in range(len(inputPKpairNew)):
		InIDs.append(inputPKpairNew[i][0])
		PKs.append(inputPKpairNew[i][1])
	
	print "----------- QUERY --------------"
	curpath = os.path.abspath(os.curdir)
	## FILES ##
	resultName = "ce10IDresult.csv"
	#resultName = "ce10results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)) + ".csv"
	#resultImage = "ce10images.png"
	print "Current Dir : %s" % (curpath)
	print resultName
	print "Trying to open %s" % (os.path.join(curpath, resultName))	
	print "--------------- WRITING RESULTS ----------------"
    
	writingStart = time.clock()
	with open(resultName, 'w+') as f:
		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		TPROM = []
		TINTRA = []
		TTERM = []
		PPROM = []
		PINTRA = []
		PTERM = []	

		GGFGenes = []
		TJGenes = []
		PMGenes = []
		GenesNotAss = []
		CGIDS = []


		for pk in range(len(PKs)):
    			
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			TProm = []
			TIntra = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			GG = []
			TJ = []
			PM = []	
								
			ID = str(PKs[pk])
			originalID = str(InIDs[pk])
			originID = originalID.replace("\n","")
			tag = "=============ID: " + str(originID) + "==============="
			f.write(str(tag)+"\n")
			header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
			header.replace("'",'')
			f.write(header+"\n")
			RES = Ce10.objects.raw('SELECT * FROM Ce10 WHERE type1!="Intergenic" and refid1 like  \"%%%%%s;%%%%\" or refid2 like  \"%%%%%s;%%%%\" or refid3 like  \"%%%%%s;%%%%\" or refid4 like  \"%%%%%s;%%%%\" or refid5 like  \"%%%%%s;%%%%\" or refid6 like  \"%%%%%s;%%%%\" or refid7 like  \"%%%%%s;%%%%\" or refid8 like  \"%%%%%s;%%%%\" or refid9 like  \"%%%%%s;%%%%\" or refid10 like  \"%%%%%s;%%%%\" or refid11 like  \"%%%%%s;%%%%\" or refid12 like  \"%%%%%s;%%%%\" or refid13 like  \"%%%%%s;%%%%\" or refid14 like  \"%%%%%s;%%%%\" or refid15 like  \"%%%%%s;%%%%\" or refid16 like  \"%%%%%s;%%%%\" or refid17 like  \"%%%%%s;%%%%\" or refid18 like  \"%%%%%s;%%%%\" or refid19 like  \"%%%%%s;%%%%\" or refid20 like  \"%%%%%s;%%%%\" or refid21 like  \"%%%%%s;%%%%\" or refid22 like  \"%%%%%s;%%%%\" or refid23 like  \"%%%%%s;%%%%\" or refid24 like  \"%%%%%s;%%%%\" or refid25 like  \"%%%%%s;%%%%\" or refid26 like  \"%%%%%s;%%%%\"' % (ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
			for obj in RES:
				AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
				AssoCGI = [str(i) for i in AssoCGI]
				Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
							[obj.type2, obj.genesym2, obj.strand2, obj.refid2],
							[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
							[obj.type4, obj.genesym4, obj.strand4, obj.refid4],
							[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
							[obj.type6, obj.genesym6, obj.strand6, obj.refid6],
							[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
							[obj.type8, obj.genesym8, obj.strand8, obj.refid8],
							[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
							[obj.type10, obj.genesym10, obj.strand10, obj.refid10],
							[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
							[obj.type12, obj.genesym12, obj.strand12, obj.refid12],
							[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
							[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],
							[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
							[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],
							[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
							[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],
							[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
							[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],
							[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
							[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],
							[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
							[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],
							[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
							[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
				Annot = [x for x in Annot if x != ['','','','']]	
				Annot = [map(str,i) for i in Annot]							
				nr = []	
				for a in Annot[0:]:
					for item in a:
						if ID in item:
							nr.append(a)
				A = [AssoCGI, nr]

				All.append(A) # All queries per entry
				A = str(A)
				A = A.replace('[','')
				A = A.replace(']','')
				A = A.replace("'",'')
				f.write(A + "\n")	
			#========================= Stat Report (File and Figure) =========================
			cgID = []						
			for l in All:
				CGIDs = l[0][0]
				cgID.append(CGIDs)
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					
			CGIDS.append(cgID)
			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)
			


			if len(list(RES)) == 0:
				res2 = "ID: " + originalID + "   is not associated with a CpG Island"
				f.write(str(res2)+"\n")		
			else:		
				f.write("--------------------------------------------------------------------" + "\n"
				+ "This gene has a total number of  " + str(GG+TJ+PM) + "   CpG Islands associated with it." + "\n" + 
				"--------------------------------------------------------------------" + "\n"
				+ "Gardiner-Garden and Frommer algorithm found " + str(GG) + " CGIs " + " with " + str(GProm) + "  Promoter CGIs | " + str(GIntra) + "  Intragenic CGIs |  " + str(GTerm) + " Gene-terminal CGIs." + "\n"
				+ "Takai-Jones algorithm found  " + str(TJ) + " CGIs "  + "with " + str(TProm) + " Promoter CGIs | " + str(TIntra) + "  Intragenic CGIs |  " + str(TTerm) + " Gene-terminal CGIs." + "\n"
				+ "Ponger-Mouchiroud algorithm found  " + str(PM) + " CGIs" + "with  " + str(PProm) + " Promoter CGIs | " + str(PIntra) + "  Intragenic CGIs |  " + str(PTerm) + " Gene-terminal CGIs." + "\n" + "\n")
					
		f.seek(0)


		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)

		for cgid in CGIDS:
    			combined = '\t'.join(cgid)
			if 'GG' in combined:
				GGFGenes.append(1)
			if 'TJ' in combined:
				TJGenes.append(1)
			if 'PM' in combined:
				PMGenes.append(1)
			else:
				GenesNotAss.append(1)
		
		GGFGenes = len(GGFGenes)
		TJGenes = len(TJGenes)
		PMGenes = len(PMGenes)
		GenesNotAss = len(GenesNotAss)
		GenesAssoc = len(inputPKpairNew)-GenesNotAss		
		
		ce10page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
									<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
									<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"></link>
									<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>									
									
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}


												div.summary {
													max-width: 900px;
													background-color: #34495E ;
													font-family: Arial;
													margin: 0 auto;
												border:5px solid black;
												
												}
												b {  
												color: #EBEDEF
												}
												h2{
												background-color: #9B59B6;
												color: white;
												height: 40px;
												margin: 0 auto;
												text-align:center;
												
												}
												p {
												color: #EBEDEF;
												}
												b2 {
												color: #EBEDEF   ;
												}
												div.algorithms{
													max-width: 700px;
													max-height: 200px;
													background-color: #566573  ;
													font-family: Arial;
													margin: 0 auto;
													border:5px solid black;


										</style>
	
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for CE10</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../ce10IDresult">Download</a></h4>
											</div>
											<br></br>

										<div class="summary"> 
										<h2>Summary</h2>
										<p>   <b> %s </b>/<b> %s </b> genes were mapped successfully. </p>
										<p> IDs which are not mapped are:  <b> %s </b> </p>
										<p> <b> %s </b>/<b> %s </b> mapped genes were associated with a CGI.
										<div class="algorithms">
										<p> <b2>Gardiner-Garden and Frommer</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Takai-Jones</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Ponger-Mouchiroud</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>

										</div>
										<br>
										</div>


											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<br></br>
											
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
															{
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>

									</body>
									</font>
									</head>
									</html>

									""" % (str(len(inputPKpairNew)), str(len(inputPKpair)), str(notMappedGenes), str(GenesAssoc) ,str(len(inputPKpairNew)),str(GGFGenes), str(len(inputPKpairNew)),str(TJGenes),str(len(inputPKpairNew)),str(PMGenes),str(len(inputPKpairNew)), str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(TPROM), str(TINTRA), str(TTERM), str(PPROM), str(PINTRA), str(PTERM))	
		
										
		response = HttpResponse(ce10page, content_type='text/html')
		return response
		#response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart)*1000)
		#response = HttpResponse(ce10page, StringIO(f.read()).getvalue(), content_type='text/html')
		#response['Content-Disposition']='attachment; filename=%s' % resultName

#-------------------------------------------------------(HG38) GENE ID --> REFSEQ_ID ---> QUERY RESULTS ------------------------------------------------#
def hg38IDQuery(uploaded_file):
	
	mg = mygene.MyGeneInfo()
	IDList = uploaded_file.read().splitlines()
	Scope = 'symbol,entrezgene,ensembl.*,refseq.*,accession.*,unigene'
	MyScopes = 'symbol,entrezgene,ensembl.*,alias,refseq.*,accession.*,unigene,pdb,pfam,mim,reporter,go,hgnc'		
	MyFields = "refseq.rna"
	
	#qStart = time.clock()
	
	HS_Query = mg.querymany(IDList, scopes=Scope, fields=MyFields, species='human', returnall=True)
	
	outHS = HS_Query['out']
	
	#### GENE ID MAPPING outputs are read for querying ####
	refseqs = []
	for ls in outHS:
		if 'refseq.rna' in ls:
			refseq = ls['refseq.rna']
			if type(refseq) == list:
				refseq = refseq[0]
			refseqs.append(refseq)
		else:
			refseqs.append("NO HIT")


	########### For Results ###########		
	inputPKpair = zip(IDList, refseqs)

	
	inputPKpairNew = []
	notMappedGenes = []
	for i in inputPKpair:
		if i[1] == "NO HIT":
			notMappedGenes.append(i[0])
			continue
		else:
			inputPKpairNew.append(i)

	PKs = []
	InIDs = []
	for i in range(len(inputPKpairNew)):
		InIDs.append(inputPKpairNew[i][0])
		PKs.append(inputPKpairNew[i][1])


	#print inputPKpair
	#print inputPKpairNew

	print "----------- QUERY --------------"
	

	
	curpath = os.path.abspath(os.curdir)
	
	## FILES ##
	resultName = "hg38IDresult.csv"
	#resultName = "hg38results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)) + ".csv"
	#resultImage = "hg38images.png"
	print "Current Dir : %s" % (curpath)
	print resultName
	print "Trying to open %s" % (os.path.join(curpath, resultName))
	
	print "--------------- WRITING RESULTS ----------------"
    



	writingStart = time.clock()
	with open(resultName, 'w+') as f:
		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		TPROM = []
		TINTRA = []
		TTERM = []
		PPROM = []
		PINTRA = []
		PTERM = []


		GGFGenes = []
		TJGenes = []
		PMGenes = []
		GenesNotAss = []
		CGIDS = []


		for pk in range(len(PKs)):
		
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			TProm = []
			TIntra = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			GG = []
			TJ = []
			PM = []
	
								
			ID = str(PKs[pk])
			originalID = str(InIDs[pk])
			originID = originalID.replace("\n","")
			tag = "=============ID: " + str(originID) + "==============="
			f.write(str(tag)+"\n")
			header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
			header.replace("'",'')
			f.write(header+"\n")
			RES = Hg38.objects.raw('SELECT * FROM Hg38 WHERE type1!="Intergenic" and refid1 like  \"%%%%%s;%%%%\" or refid2 like  \"%%%%%s;%%%%\" or refid3 like  \"%%%%%s;%%%%\" or refid4 like  \"%%%%%s;%%%%\" or refid5 like  \"%%%%%s;%%%%\" or refid6 like  \"%%%%%s;%%%%\" or refid7 like  \"%%%%%s;%%%%\" or refid8 like  \"%%%%%s;%%%%\" or refid9 like  \"%%%%%s;%%%%\" or refid10 like  \"%%%%%s;%%%%\" or refid11 like  \"%%%%%s;%%%%\" or refid12 like  \"%%%%%s;%%%%\" or refid13 like  \"%%%%%s;%%%%\"' % (ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
			for obj in RES:
				AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
				AssoCGI = [str(i) for i in AssoCGI]
				Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
							[obj.type2, obj.genesym2, obj.strand2, obj.refid2],
							[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
							[obj.type4, obj.genesym4, obj.strand4, obj.refid4],
							[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
							[obj.type6, obj.genesym6, obj.strand6, obj.refid6],
							[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
							[obj.type8, obj.genesym8, obj.strand8, obj.refid8],
							[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
							[obj.type10, obj.genesym10, obj.strand10, obj.refid10],
							[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
							[obj.type12, obj.genesym12, obj.strand12, obj.refid12],
							[obj.type13, obj.genesym13 , obj.strand13, obj.refid13]]						
				Annot = [x for x in Annot if x != ['','','','']]	
				Annot = [map(str,i) for i in Annot]							
				nr = []	
				for a in Annot[0:]:
					for item in a:
						if ID in item:
							nr.append(a)
				A = [AssoCGI, nr]
				
				All.append(A) # All queries per entry
				A = str(A)
				A = A.replace('[','')
				A = A.replace(']','')
				A = A.replace("'",'')
				f.write(A + "\n")	
			#========================= Stat Report (File and Figure) =========================
			cgID = []
			for l in All:
				CGIDs = l[0][0]
				cgID.append(CGIDs)
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					
			CGIDS.append(cgID)
			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)

			if len(list(RES)) == 0:
				res2 = "ID: " + originalID + "   is not associated with a CpG Island"
				f.write(str(res2)+"\n")		
			else:		
				f.write("--------------------------------------------------------------------" + "\n"
				+ "This gene has a total number of  " + str(GG+TJ+PM) + "   CpG Islands associated with it." + "\n" + 
				"--------------------------------------------------------------------" + "\n"
				+ "Gardiner-Garden and Frommer algorithm found " + str(GG) + " CGIs " + " with " + str(GProm) + "  Promoter CGIs | " + str(GIntra) + "  Intragenic CGIs |  " + str(GTerm) + " Gene-terminal CGIs." + "\n"
				+ "Takai-Jones algorithm found  " + str(TJ) + " CGIs "  + "with " + str(TProm) + " Promoter CGIs | " + str(TIntra) + "  Intragenic CGIs |  " + str(TTerm) + " Gene-terminal CGIs." + "\n"
				+ "Ponger-Mouchiroud algorithm found  " + str(PM) + " CGIs" + "with  " + str(PProm) + " Promoter CGIs | " + str(PIntra) + "  Intragenic CGIs |  " + str(PTerm) + " Gene-terminal CGIs." + "\n" + "\n")

		f.seek(0)


		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)



		for cgid in CGIDS:
			combined = '\t'.join(cgid)
			if 'GG' in combined:
				GGFGenes.append(1)
			if 'TJ' in combined:
				TJGenes.append(1)
			if 'PM' in combined:
				PMGenes.append(1)
			else:
				GenesNotAss.append(1)
		
		GGFGenes = len(GGFGenes)
		TJGenes = len(TJGenes)
		PMGenes = len(PMGenes)
		GenesNotAss = len(GenesNotAss)
		GenesAssoc = len(inputPKpairNew)-GenesNotAss

		
		hg38page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
									<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
									<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"></link>
									<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>									
									
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}


												div.summary {
													max-width: 900px;
													background-color: #34495E ;
													font-family: Arial;
													margin: 0 auto;
												border:5px solid black;
												
												}
												b {  
												color: #EBEDEF
												}
												h2{
												background-color: #9B59B6;
												color: white;
												height: 40px;
												margin: 0 auto;
												text-align:center;
												
												}
												p {
												color: #EBEDEF;
												}
												b2 {
												color: #EBEDEF   ;
												}
												div.algorithms{
													max-width: 700px;
													max-height: 200px;
													background-color: #566573  ;
													font-family: Arial;
													margin: 0 auto;
													border:5px solid black;


										</style>
	
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for HG38</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../hg38IDresult">Download</a></h4>
											</div>
											<br></br>

										<div class="summary"> 
										<h2>Summary</h2>
										<p>   <b> %s </b>/<b> %s </b> genes were mapped successfully. </p>
										<p> IDs which are not mapped are:  <b> %s </b> </p>
										<p> <b> %s </b>/<b> %s </b> mapped genes were associated with a CGI.
										<div class="algorithms">
										<p> <b2>Gardiner-Garden and Frommer</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Takai-Jones</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Ponger-Mouchiroud</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>

										</div>
										<br>
										</div>


											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<br></br>
											
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
															{
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>

									</body>
									</font>
									</head>
									</html>

									""" % (str(len(inputPKpairNew)), str(len(inputPKpair)), str(notMappedGenes), str(GenesAssoc) ,str(len(inputPKpairNew)),str(GGFGenes), str(len(inputPKpairNew)),str(TJGenes),str(len(inputPKpairNew)),str(PMGenes),str(len(inputPKpairNew)), str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(TPROM), str(TINTRA), str(TTERM), str(PPROM), str(PINTRA), str(PTERM))	

		
										
		response = HttpResponse(hg38page, content_type='text/html')
		return response
		#response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart)*1000)
		#response = HttpResponse(hg38page, StringIO(f.read()).getvalue(), content_type='text/html')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		


#-------------------------------------------------------(MM10) GENE ID --> REFSEQ_ID ---> QUERY RESULTS --------------------------------------------------#
def mm10IDQuery(uploaded_file):
	
	mg = mygene.MyGeneInfo()
	IDList = uploaded_file.read().splitlines()
	Scope = 'symbol,entrezgene,ensembl.*,refseq.*,accession.*,unigene'
	MyScopes = 'symbol,entrezgene,ensembl.*,alias,refseq.*,accession.*,unigene,pdb,pfam,mim,reporter,go,hgnc'		
	MyFields = "refseq.rna"
	
	#qStart = time.clock()
	
	MM_Query = mg.querymany(IDList, scopes=Scope, fields=MyFields, species='mouse', returnall=True)
	
	#print "Mapping time : %s ms" % ((time.clock() - qStart)*1000)
	
	outMM = MM_Query['out']
	
	#### GENE ID MAPPING outputs are read for querying ####
	refseqs = []
	for ls in outMM:
		if 'refseq.rna' in ls:
			refseq = ls['refseq.rna']
			if type(refseq) == list:
				refseq = refseq[0]
			refseqs.append(refseq)
		else:
			refseqs.append("NO HIT")
	########### For Results ###########		
	inputPKpair = zip(IDList, refseqs)

	
	inputPKpairNew = []
	notMappedGenes = []
	for i in inputPKpair:
		if i[1] == "NO HIT":
			notMappedGenes.append(i[0])
			continue
		else:
			inputPKpairNew.append(i)

	PKs = []
	InIDs = []
	for i in range(len(inputPKpairNew)):
		InIDs.append(inputPKpairNew[i][0])
		PKs.append(inputPKpairNew[i][1])
	
	
	#print inputPKpair
	print "----------- QUERY --------------"
	

	
	
	curpath = os.path.abspath(os.curdir)
	resultName = "mm10IDresult.csv"
	#resultName = "mm10results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)) + ".csv"
	#resultName = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath)
	print resultName
	print "Trying to open %s" % (os.path.join(curpath, resultName))
	
	print "--------------- WRITING RESULTS ----------------"

	
    
	writingStart = time.clock()
	with open(resultName, 'w+') as f:
	
		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		TPROM = []
		TINTRA = []
		TTERM = []
		PPROM = []
		PINTRA = []
		PTERM = []

		GGFGenes = []
		TJGenes = []
		PMGenes = []
		GenesNotAss = []
		CGIDS = []

		for pk in range(len(PKs)):
		
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			TProm = []
			TIntra = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			GG = []
			TJ = []
			PM = []	
			
		
		
			ID = str(PKs[pk])
			originalID = InIDs[pk]
			tag = "ID: " + str(originalID).replace("\n","")
			f.write("=============" + str(tag)+ "=================="+"\n")
			header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
			header.replace("'",'')
			f.write(header+"\n")						
			RES = Mm10.objects.raw('SELECT * FROM Mm10 WHERE type1!="Intergenic" and refid1 like  \"%%%%%s;%%%%\" or refid2 like  \"%%%%%s;%%%%\" or refid3 like  \"%%%%%s;%%%%\" or refid4 like  \"%%%%%s;%%%%\" or refid5 like  \"%%%%%s;%%%%\" or refid6 like  \"%%%%%s;%%%%\" or refid7 like  \"%%%%%s;%%%%\" or refid8 like  \"%%%%%s;%%%%\" or refid9 like  \"%%%%%s;%%%%\" or refid10 like  \"%%%%%s;%%%%\" or refid11 like  \"%%%%%s;%%%%\" or refid12 like  \"%%%%%s;%%%%\" or refid13 like  \"%%%%%s;%%%%\" or refid14 like  \"%%%%%s;%%%%\" or refid15 like  \"%%%%%s;%%%%\" or refid16 like  \"%%%%%s;%%%%\" or refid17 like  \"%%%%%s;%%%%\" or refid18 like  \"%%%%%s;%%%%\" or refid19 like  \"%%%%%s;%%%%\" or refid20 like  \"%%%%%s;%%%%\" or refid21 like  \"%%%%%s;%%%%\" or refid22 like  \"%%%%%s;%%%%\" or refid23 like  \"%%%%%s;%%%%\" or refid24 like  \"%%%%%s;%%%%\" or refid25 like  \"%%%%%s;%%%%\" or refid26 like  \"%%%%%s;%%%%\" or refid27 like  \"%%%%%s;%%%%\" or refid28 like  \"%%%%%s;%%%%\" or refid29 like  \"%%%%%s;%%%%\" or refid30 like  \"%%%%%s;%%%%\" or refid31 like  \"%%%%%s;%%%%\" or refid32 like  \"%%%%%s;%%%%\" or refid33 like  \"%%%%%s;%%%%\" or refid34 like  \"%%%%%s;%%%%\" or refid35 like  \"%%%%%s;%%%%\" or refid36 like  \"%%%%%s;%%%%\" or refid37 like  \"%%%%%s;%%%%\" or refid38 like  \"%%%%%s;%%%%\" or refid39 like  \"%%%%%s;%%%%\" or refid40 like  \"%%%%%s;%%%%\" or refid41 like  \"%%%%%s;%%%%\" or refid42 like  \"%%%%%s;%%%%\" or refid43 like  \"%%%%%s;%%%%\" or refid44 like  \"%%%%%s;%%%%\" or refid45 like  \"%%%%%s;%%%%\" or refid46 like  \"%%%%%s;%%%%\" or refid47 like  \"%%%%%s;%%%%\" or refid48 like  \"%%%%%s;%%%%\" or refid49 like  \"%%%%%s;%%%%\" or refid50 like  \"%%%%%s;%%%%\"' % (ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
			
			for obj in RES:
				AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
				AssoCGI = [str(i) for i in AssoCGI]
				Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
							[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
							[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
							[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
							[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
							[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
							[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
							[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
							[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
							[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
							[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
							[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
							[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
							[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
							[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
							[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
							[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
							[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
							[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
							[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
							[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
							[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
							[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
							[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
							[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
							[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
				Annot = [x for x in Annot if x != ['','','','']]	
				Annot = [map(str,i) for i in Annot]			
				nr = []	
				for a in Annot[0:]:
					for item in a:
						if ID in item:
							nr.append(a)
				A = [AssoCGI, nr]
				All.append(A)								

				A = str(A)
				A = A.replace('[','')
				A = A.replace(']','')
				A = A.replace("'",'')
				f.write(A + "\n")	


			#========================= Stat Report =========================	
			cgID = []
			for l in All:
				CGIDs = l[0][0]
				cgID.append(CGIDs)
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)

				
			CGIDS.append(cgID)
			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



						
			if len(list(RES)) == 0:
				res2 = "ID: " + originalID + "   is not associated with a CpG Island"
				f.write(str(res2)+"\n")						
			else:						
				f.write("--------------------------------------------------------------------" + "\n"
				+ "This gene has a total number of  " + str(GG+TJ+PM) + "   CpG Islands associated with it." + "\n" + 
				"--------------------------------------------------------------------" + "\n"
				+ "Gardiner-Garden and Frommer algorithm found " + str(GG) + " CGIs " + " with " + str(GProm) + "  Promoter CGIs | " + str(GIntra) + "  Intragenic CGIs |  " + str(GTerm) + " Gene-terminal CGIs." + "\n"
				+ "Takai-Jones algorithm found  " + str(TJ) + " CGIs "  + "with " + str(TProm) + " Promoter CGIs | " + str(TIntra) + "  Intragenic CGIs |  " + str(TTerm) + " Gene-terminal CGIs." + "\n"
				+ "Ponger-Mouchiroud algorithm found  " + str(PM) + " CGIs" + "with  " + str(PProm) + " Promoter CGIs | " + str(PIntra) + "  Intragenic CGIs |  " + str(PTerm) + " Gene-terminal CGIs." + "\n" + "\n")
		f.seek(0)

		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)


		for cgid in CGIDS:
    			combined = '\t'.join(cgid)
			if 'GG' in combined:
				GGFGenes.append(1)
			if 'TJ' in combined:
				TJGenes.append(1)
			if 'PM' in combined:
				PMGenes.append(1)
			else:
				GenesNotAss.append(1)
		
		GGFGenes = len(GGFGenes)
		TJGenes = len(TJGenes)
		PMGenes = len(PMGenes)
		GenesNotAss = len(GenesNotAss)
		GenesAssoc = len(inputPKpairNew)-GenesNotAss

		mm10page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
									<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
									<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"></link>
									<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>									
									
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}


												div.summary {
													max-width: 900px;
													background-color: #34495E ;
													font-family: Arial;
													margin: 0 auto;
												border:5px solid black;
												
												}
												b {  
												color: #EBEDEF
												}
												h2{
												background-color: #9B59B6;
												color: white;
												height: 40px;
												margin: 0 auto;
												text-align:center;
												
												}
												p {
												color: #EBEDEF;
												}
												b2 {
												color: #EBEDEF   ;
												}
												div.algorithms{
													max-width: 700px;
													max-height: 200px;
													background-color: #566573  ;
													font-family: Arial;
													margin: 0 auto;
													border:5px solid black;


										</style>
	
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for MM10</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../mm10IDresult">Download</a></h4>
											</div>
											<br></br>

										<div class="summary"> 
										<h2>Summary</h2>
										<p>   <b> %s </b>/<b> %s </b> genes were mapped successfully. </p>
										<p> IDs which are not mapped are:  <b> %s </b> </p>
										<p> <b> %s </b>/<b> %s </b> mapped genes were associated with a CGI.
										<div class="algorithms">
										<p> <b2>Gardiner-Garden and Frommer</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Takai-Jones</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Ponger-Mouchiroud</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>

										</div>
										<br>
										</div>


											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<br></br>
											
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
															{
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>

									</body>
									</font>
									</head>
									</html>

									""" % (str(len(inputPKpairNew)), str(len(inputPKpair)), str(notMappedGenes), str(GenesAssoc) ,str(len(inputPKpairNew)),str(GGFGenes), str(len(inputPKpairNew)),str(TJGenes),str(len(inputPKpairNew)),str(PMGenes),str(len(inputPKpairNew)), str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(TPROM), str(TINTRA), str(TTERM), str(PPROM), str(PINTRA), str(PTERM))	


		response = HttpResponse(mm10page, content_type='text/html')
		#response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart)*1000)
		return response

#-------------------------------------------------------(DM3) GENE ID --> REFSEQ_ID ---> QUERY RESULTS --------------------------------------------------#
def dm3IDQuery(uploaded_file):
	
	mg = mygene.MyGeneInfo()
	IDList = uploaded_file.read().splitlines()
	Scope = 'symbol,entrezgene,ensembl.*,refseq.*,accession.*,unigene'
	MyScopes = 'symbol,entrezgene,ensembl.*,alias,refseq.*,accession.*,unigene,pdb,pfam,mim,reporter,go,hgnc'		
	MyFields = "refseq.rna"
	
	#qStart = time.clock()
	
	DM_Query = mg.querymany(IDList, scopes=Scope, fields=MyFields, species='fruitfly', returnall=True)
	
	#print "Mapping time : %s ms" % ((time.clock() - qStart)*1000)
	
	outDM = DM_Query['out']
	
	#### GENE ID MAPPING outputs are read for querying ####
	refseqs = []
	for ls in outDM:
		if 'refseq.rna' in ls:
			refseq = ls['refseq.rna']
			if type(refseq) == list:
				refseq = refseq[0]
			refseqs.append(refseq)
		else:
			refseqs.append("NO HIT")
	########### For Results ###########		
	inputPKpair = zip(IDList, refseqs)

	
	inputPKpairNew = []
	notMappedGenes = []
	for i in inputPKpair:
		if i[1] == "NO HIT":
			notMappedGenes.append(i[0])
			continue
		else:
			inputPKpairNew.append(i)

	PKs = []
	InIDs = []
	for i in range(len(inputPKpairNew)):
		InIDs.append(inputPKpairNew[i][0])
		PKs.append(inputPKpairNew[i][1])


	print "----------- QUERY --------------"
	
	
	curpath = os.path.abspath(os.curdir)
	resultName = "dm3IDresult.csv"
	#resultName = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath)
	print resultName
	print "Trying to open %s" % (os.path.join(curpath, resultName))
	
	print "--------------- WRITING RESULTS ----------------"
    
	writingStart = time.clock()
	with open(resultName, 'w+') as f:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		TPROM = []
		TINTRA = []
		TTERM = []
		PPROM = []
		PINTRA = []
		PTERM = []	


		GGFGenes = []
		TJGenes = []
		PMGenes = []
		GenesNotAss = []
		CGIDS = []

		for pk in range(len(PKs)):

			All = []
			GProm = []
			GIntra = []
			GTerm = []
			TProm = []
			TIntra = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			GG = []
			TJ = []
			PM = []	
		
		
			ID = str(PKs[pk])
			originalID = InIDs[pk]
			tag = "ID: " + str(originalID).replace("\n","")
			f.write("=============" + str(tag)+ "==================" + "\n")
			header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
			header.replace("'",'')
			f.write(header+"\n")
						
			RES = Dm3.objects.raw('SELECT * FROM Dm3 WHERE type1!="Intergenic" and refid1 like  \"%%%%%s;%%%%\" or refid2 like  \"%%%%%s;%%%%\" or refid3 like  \"%%%%%s;%%%%\" or refid4 like  \"%%%%%s;%%%%\" or refid5 like  \"%%%%%s;%%%%\" or refid6 like  \"%%%%%s;%%%%\" or refid7 like  \"%%%%%s;%%%%\" or refid8 like  \"%%%%%s;%%%%\" or refid9 like  \"%%%%%s;%%%%\" or refid10 like  \"%%%%%s;%%%%\" or refid11 like  \"%%%%%s;%%%%\" or refid12 like  \"%%%%%s;%%%%\" or refid13 like  \"%%%%%s;%%%%\" or refid14 like  \"%%%%%s;%%%%\" or refid15 like  \"%%%%%s;%%%%\" or refid16 like  \"%%%%%s;%%%%\" or refid17 like  \"%%%%%s;%%%%\" or refid18 like  \"%%%%%s;%%%%\" or refid19 like  \"%%%%%s;%%%%\" or refid20 like  \"%%%%%s;%%%%\" or refid21 like  \"%%%%%s;%%%%\" or refid22 like  \"%%%%%s;%%%%\" or refid23 like  \"%%%%%s;%%%%\" or refid24 like  \"%%%%%s;%%%%\" or refid25 like  \"%%%%%s;%%%%\" or refid26 like  \"%%%%%s;%%%%\" or refid27 like  \"%%%%%s;%%%%\" or refid28 like  \"%%%%%s;%%%%\" or refid29 like  \"%%%%%s;%%%%\" or refid30 like  \"%%%%%s;%%%%\" or refid31 like  \"%%%%%s;%%%%\" or refid32 like  \"%%%%%s;%%%%\" or refid33 like  \"%%%%%s;%%%%\" or refid34 like  \"%%%%%s;%%%%\" or refid35 like  \"%%%%%s;%%%%\" or refid36 like  \"%%%%%s;%%%%\" or refid37 like  \"%%%%%s;%%%%\" or refid38 like  \"%%%%%s;%%%%\" or refid39 like  \"%%%%%s;%%%%\" or refid40 like  \"%%%%%s;%%%%\" or refid41 like  \"%%%%%s;%%%%\" or refid42 like  \"%%%%%s;%%%%\" or refid43 like  \"%%%%%s;%%%%\" or refid44 like  \"%%%%%s;%%%%\" or refid45 like  \"%%%%%s;%%%%\" or refid46 like  \"%%%%%s;%%%%\" or refid47 like  \"%%%%%s;%%%%\" or refid48 like  \"%%%%%s;%%%%\" or refid49 like  \"%%%%%s;%%%%\" or refid50 like  \"%%%%%s;%%%%\"' % (ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))


			for obj in RES:
				AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
				AssoCGI = [str(i) for i in AssoCGI]
				Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
							[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
							[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
							[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
							[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
							[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
							[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
							[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
							[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
							[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
							[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
							[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
							[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
							[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
							[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
							[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
							[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
							[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
							[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
							[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
							[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
							[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
							[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
							[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
							[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
							[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
				Annot = [x for x in Annot if x != ['','','','']]	
				Annot = [map(str,i) for i in Annot]			
				nr = []	
				for a in Annot[0:]:
					for item in a:
						if ID in item:
							nr.append(a)
				A = [AssoCGI, nr]
				All.append(A)								

				A = str(A)
				A = A.replace('[','')
				A = A.replace(']','')
				A = A.replace("'",'')
				f.write(A + "\n")	




			#========================= Stat Report =========================	
			cgID = []
			for l in All:
				CGIDs = l[0][0]
				cgID.append(CGIDs)
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)

			CGIDS.append(cgID)
			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)
			
			if len(list(RES)) == 0:
				res2 = "ID: " + originalID + "   is not associated with a CpG Island"
				f.write(str(res2)+"\n")						
			else:						
				f.write("--------------------------------------------------------------------" + "\n"
				+ "This gene has a total number of  " + str(GG+TJ+PM) + "   CpG Islands associated with it." + "\n" + 
				"--------------------------------------------------------------------" + "\n"
				+ "Gardiner-Garden and Frommer algorithm found " + str(GG) + " CGIs " + " with " + str(GProm) + "  Promoter CGIs | " + str(GIntra) + "  Intragenic CGIs |  " + str(GTerm) + " Gene-terminal CGIs." + "\n"
				+ "Takai-Jones algorithm found  " + str(TJ) + " CGIs "  + "with " + str(TProm) + " Promoter CGIs | " + str(TIntra) + "  Intragenic CGIs |  " + str(TTerm) + " Gene-terminal CGIs." + "\n"
				+ "Ponger-Mouchiroud algorithm found  " + str(PM) + " CGIs" + "with  " + str(PProm) + " Promoter CGIs | " + str(PIntra) + "  Intragenic CGIs |  " + str(PTerm) + " Gene-terminal CGIs." + "\n" + "\n")
													
		f.seek(0)
		
		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)


		for cgid in CGIDS:
			combined = '\t'.join(cgid)
			if 'GG' in combined:
				GGFGenes.append(1)
			if 'TJ' in combined:
				TJGenes.append(1)
			if 'PM' in combined:
				PMGenes.append(1)
			else:
				GenesNotAss.append(1)
		
		GGFGenes = len(GGFGenes)
		TJGenes = len(TJGenes)
		PMGenes = len(PMGenes)
		GenesNotAss = len(GenesNotAss)
		GenesAssoc = len(inputPKpairNew)-GenesNotAss


		dm3page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
									<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
									<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"></link>
									<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>									
									
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}


												div.summary {
													max-width: 900px;
													background-color: #34495E ;
													font-family: Arial;
													margin: 0 auto;
												border:5px solid black;
												
												}
												b {  
												color: #EBEDEF
												}
												h2{
												background-color: #9B59B6;
												color: white;
												height: 40px;
												margin: 0 auto;
												text-align:center;
												
												}
												p {
												color: #EBEDEF;
												}
												b2 {
												color: #EBEDEF   ;
												}
												div.algorithms{
													max-width: 700px;
													max-height: 200px;
													background-color: #566573  ;
													font-family: Arial;
													margin: 0 auto;
													border:5px solid black;


										</style>
	
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for DM3</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../dm3IDresult">Download</a></h4>
											</div>
											<br></br>

										<div class="summary"> 
										<h2>Summary</h2>
										<p>   <b> %s </b>/<b> %s </b> genes were mapped successfully. </p>
										<p> IDs which are not mapped are:  <b> %s </b> </p>
										<p> <b> %s </b>/<b> %s </b> mapped genes were associated with a CGI.
										<div class="algorithms">
										<p> <b2>Gardiner-Garden and Frommer</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Takai-Jones</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Ponger-Mouchiroud</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>

										</div>
										<br>
										</div>


											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<br></br>
											
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
															{
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>

									</body>
									</font>
									</head>
									</html>

									""" % (str(len(inputPKpairNew)), str(len(inputPKpair)), str(notMappedGenes), str(GenesAssoc) ,str(len(inputPKpairNew)),str(GGFGenes), str(len(inputPKpairNew)),str(TJGenes),str(len(inputPKpairNew)),str(PMGenes),str(len(inputPKpairNew)), str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(TPROM), str(TINTRA), str(TTERM), str(PPROM), str(PINTRA), str(PTERM))	



		response = HttpResponse(dm3page, content_type='text/html')
		#response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart)*1000)
		return response

#-------------------------------------------------------(RN6) GENE ID --> REFSEQ_ID ---> QUERY RESULTS --------------------------------------------------#
def rn6IDQuery(uploaded_file):
    	
	mg = mygene.MyGeneInfo()
	IDList = uploaded_file.read().splitlines()
	Scope = 'symbol,entrezgene,ensembl.*,refseq.*,accession.*,unigene'
	MyScopes = 'symbol,entrezgene,ensembl.*,alias,refseq.*,accession.*,unigene,pdb,pfam,mim,reporter,go,hgnc'		
	MyFields = "refseq.rna"
	
	#qStart = time.clock()
	
	RN_Query = mg.querymany(IDList, scopes=Scope, fields=MyFields, species='rat', returnall=True)
	
	#print "Mapping time : %s ms" % ((time.clock() - qStart)*1000)
	
	outRN = RN_Query['out']
	
	#### GENE ID MAPPING outputs are read for querying ####
	refseqs = []
	for ls in outRN:
		if 'refseq.rna' in ls:
			refseq = ls['refseq.rna']
			if type(refseq) == list:
				refseq = refseq[0]
			refseqs.append(refseq)
		else:
			refseqs.append("NO HIT")
	########### For Results ###########		
	inputPKpair = zip(IDList, refseqs)

	
	inputPKpairNew = []
	notMappedGenes = []
	for i in inputPKpair:
		if i[1] == "NO HIT":
			notMappedGenes.append(i[0])
			continue
		else:
			inputPKpairNew.append(i)

	PKs = []
	InIDs = []
	for i in range(len(inputPKpairNew)):
		InIDs.append(inputPKpairNew[i][0])
		PKs.append(inputPKpairNew[i][1])
	print "----------- QUERY --------------"
	
	
	curpath = os.path.abspath(os.curdir)
	resultName = "rn6IDresult.csv"
	#resultName = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath)
	print resultName
	print "Trying to open %s" % (os.path.join(curpath, resultName))
	
	print "--------------- WRITING RESULTS ----------------"
    
	writingStart = time.clock()
	with open(resultName, 'w+') as f:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		TPROM = []
		TINTRA = []
		TTERM = []
		PPROM = []
		PINTRA = []
		PTERM = []	

		GGFGenes = []
		TJGenes = []
		PMGenes = []
		GenesNotAss = []
		CGIDS = []

		for pk in range(len(PKs)):

			All = []
			GProm = []
			GIntra = []
			GTerm = []
			TProm = []
			TIntra = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			GG = []
			TJ = []
			PM = []	
		
		
			ID = str(PKs[pk])
			originalID = InIDs[pk]
			tag = "ID: " + str(originalID).replace("\n","")
			f.write("=============" + str(tag)+ "==================" + "\n")
			header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
			header.replace("'",'')
			f.write(header+"\n")
						
			RES = Rn6.objects.raw('SELECT * FROM Rn6 WHERE type1!="Intergenic" and refid1 like  \"%%%%%s;%%%%\" or refid2 like  \"%%%%%s;%%%%\" or refid3 like  \"%%%%%s;%%%%\" or refid4 like  \"%%%%%s;%%%%\" or refid5 like  \"%%%%%s;%%%%\" or refid6 like  \"%%%%%s;%%%%\" or refid7 like  \"%%%%%s;%%%%\" or refid8 like  \"%%%%%s;%%%%\" or refid9 like  \"%%%%%s;%%%%\" or refid10 like  \"%%%%%s;%%%%\" or refid11 like  \"%%%%%s;%%%%\" or refid12 like  \"%%%%%s;%%%%\" or refid13 like  \"%%%%%s;%%%%\" or refid14 like  \"%%%%%s;%%%%\" or refid15 like  \"%%%%%s;%%%%\" or refid16 like  \"%%%%%s;%%%%\" or refid17 like  \"%%%%%s;%%%%\" or refid18 like  \"%%%%%s;%%%%\" or refid19 like  \"%%%%%s;%%%%\" or refid20 like  \"%%%%%s;%%%%\" or refid21 like  \"%%%%%s;%%%%\" or refid22 like  \"%%%%%s;%%%%\" or refid23 like  \"%%%%%s;%%%%\" or refid24 like  \"%%%%%s;%%%%\" or refid25 like  \"%%%%%s;%%%%\" or refid26 like  \"%%%%%s;%%%%\"' % (ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))


			for obj in RES:
				AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
				AssoCGI = [str(i) for i in AssoCGI]
				Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
							[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
							[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
							[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
							[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
							[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
							[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
							[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
							[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
							[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
							[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
							[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
							[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
							[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
				Annot = [x for x in Annot if x != ['','','','']]	
				Annot = [map(str,i) for i in Annot]			
				nr = []	
				for a in Annot[0:]:
					for item in a:
						if ID in item:
							nr.append(a)
				A = [AssoCGI, nr]
				All.append(A)								

				A = str(A)
				A = A.replace('[','')
				A = A.replace(']','')
				A = A.replace("'",'')
				f.write(A + "\n")	




			#========================= Stat Report =========================	
			cgID = []
			for l in All:
				CGIDs = l[0][0]
				cgID.append(CGIDs)
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)

			CGIDS.append(cgID)
			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)
			
			if len(list(RES)) == 0:
				res2 = "ID: " + originalID + "   is not associated with a CpG Island"
				f.write(str(res2)+"\n")						
			else:						
				f.write("--------------------------------------------------------------------" + "\n"
				+ "This gene has a total number of  " + str(GG+TJ+PM) + "   CpG Islands associated with it." + "\n" + 
				"--------------------------------------------------------------------" + "\n"
				+ "Gardiner-Garden and Frommer algorithm found " + str(GG) + " CGIs " + " with " + str(GProm) + "  Promoter CGIs | " + str(GIntra) + "  Intragenic CGIs |  " + str(GTerm) + " Gene-terminal CGIs." + "\n"
				+ "Takai-Jones algorithm found  " + str(TJ) + " CGIs "  + "with " + str(TProm) + " Promoter CGIs | " + str(TIntra) + "  Intragenic CGIs |  " + str(TTerm) + " Gene-terminal CGIs." + "\n"
				+ "Ponger-Mouchiroud algorithm found  " + str(PM) + " CGIs" + "with  " + str(PProm) + " Promoter CGIs | " + str(PIntra) + "  Intragenic CGIs |  " + str(PTerm) + " Gene-terminal CGIs." + "\n" + "\n")
													
		f.seek(0)
		
		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)


		for cgid in CGIDS:
			combined = '\t'.join(cgid)
			if 'GG' in combined:
				GGFGenes.append(1)
			if 'TJ' in combined:
				TJGenes.append(1)
			if 'PM' in combined:
				PMGenes.append(1)
			else:
				GenesNotAss.append(1)
		
		GGFGenes = len(GGFGenes)
		TJGenes = len(TJGenes)
		PMGenes = len(PMGenes)
		GenesNotAss = len(GenesNotAss)
		GenesAssoc = len(inputPKpairNew)-GenesNotAss


		rn6page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
									<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
									<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css"></link>
									<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>									
									
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}


												div.summary {
													max-width: 900px;
													background-color: #34495E ;
													font-family: Arial;
													margin: 0 auto;
												border:5px solid black;
												
												}
												b {  
												color: #EBEDEF
												}
												h2{
												background-color: #9B59B6;
												color: white;
												height: 40px;
												margin: 0 auto;
												text-align:center;
												
												}
												p {
												color: #EBEDEF;
												}
												b2 {
												color: #EBEDEF   ;
												}
												div.algorithms{
													max-width: 700px;
													max-height: 200px;
													background-color: #566573  ;
													font-family: Arial;
													margin: 0 auto;
													border:5px solid black;


										</style>
	
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for RN6</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../rn6IDresult">Download</a></h4>
											</div>
											<br></br>

										<div class="summary"> 
										<h2>Summary</h2>
										<p>   <b> %s </b>/<b> %s </b> genes were mapped successfully. </p>
										<p> IDs which are not mapped are:  <b> %s </b> </p>
										<p> <b> %s </b>/<b> %s </b> mapped genes were associated with a CGI.
										<div class="algorithms">
										<p> <b2>Gardiner-Garden and Frommer</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Takai-Jones</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>
										<hr>
										<p> <b2>Ponger-Mouchiroud</b2> algorithm found <b> %s </b>/<b> %s </b> genes associated with a CGI.</p>

										</div>
										<br>
										</div>


											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<br></br>
											
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
															{
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>

									</body>
									</font>
									</head>
									</html>

									""" % (str(len(inputPKpairNew)), str(len(inputPKpair)), str(notMappedGenes), str(GenesAssoc) ,str(len(inputPKpairNew)),str(GGFGenes), str(len(inputPKpairNew)),str(TJGenes),str(len(inputPKpairNew)),str(PMGenes),str(len(inputPKpairNew)), str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(TPROM), str(TINTRA), str(TTERM), str(PPROM), str(PINTRA), str(PTERM))	



		response = HttpResponse(rn6page, content_type='text/html')
		#response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
		#response['Content-Disposition']='attachment; filename=%s' % resultName
		print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart)*1000)
		return response





#-------------------------------------------------------------(HG38) CHROM LOCS --> QUERY RESULTS --------------------------------------------------------#
def hg38LocQuery(uploaded_file):

	curpath2 = os.path.abspath(os.curdir)
	resultName2 = "hg38LOCresult.csv"
	#resultName2 = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath2)
	print resultName2
	print "Trying to open %s" % (os.path.join(curpath2, resultName2))

	LocList = uploaded_file.read().splitlines()
						
	writingStart2 = time.clock()		
	with open(resultName2, 'w+') as f2:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		GINTER = []
		TPROM = []
		TINTRA = []
		TTERM = []
		TINTER = []
		PPROM = []
		PINTRA = []
		PTERM = []	
		PINTER = []
	
		
		for line in LocList:
				
			L = line.rstrip('\n').split('-')

			All = []
			GProm = []
			GIntra = []
			GTerm = []
			GInter = []
			TProm = []
			TIntra = []
			TInter = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			PInter = []
			GG = []
			TJ = []
			PM = []				
			
			if len(L) == 1:
				chr = str(L[0])
				tag = "Your given chromosome: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
								
				Q = Hg38.objects.raw('SELECT * FROM Hg38 WHERE chrom = "%s"' % (chr))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],
								[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],
								[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],
								[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],
								[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],
								[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],
								[obj.type13, obj.genesym13 , obj.strand13, obj.refid13]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]
					All.append(A)
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
				
			if len(L)>1:	
				chr = str(L[0])
				chr = chr.lower()
				sLoc = int(L[1])
				eLoc = int(L[2])
				tag = "Your given locations: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")	
										
				Q = Hg38.objects.raw('SELECT * FROM Hg38 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],
								[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],
								[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],
								[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],
								[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],
								[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],
								[obj.type13, obj.genesym13 , obj.strand13, obj.refid13]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]
					All.append(A)								
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
					
			if len(list(Q)) == 0:
				q2 = "There are no CpG Islands found between the locations " + line + "  you provided."
				f2.write(str(q2)+"\n")						

			#========================= Stat Report =========================	
			for l in All:
				CGIDs = l[0][0]
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
					GInCount = Annotations.count("Intergenic")
					GInter.append(GInCount)
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
					TInCount = Annotations.count("Intergenic")
					TInter.append(TInCount)
					
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					PInCount = Annotations.count("Intergenic")
					PInter.append(PInCount)

			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)	
			GInter = sum(GInter)
			GINTER.append(GInter)							
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			TInter = sum(TInter)
			TINTER.append(TInter)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			PInter = sum(PInter)
			PINTER.append(PInter)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)

		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)

		TJstdL = np.std(TJLs)

		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)

		TJstdOE = np.std(TJOEs)

		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		GINTER = sum(GINTER)
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		TINTER = sum(TINTER)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)
		PINTER = sum(PINTER)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)
		
		f2.seek(0)
		

		hg38page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}
										</style>
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for HG38</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../hg38LOCresult">Download</a></h4>
											</div>
											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
														{
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>


									</body>
									</font>
									</head>
									</html>

									""" % (str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(GINTER), str(TPROM), str(TINTRA), str(TTERM), str(TINTER), str(PPROM), str(PINTRA), str(PTERM), str(PINTER))	

		response2 = HttpResponse(hg38page, content_type='text/html')
		return response2
									

		#response2 = HttpResponse(StringIO(f2.read()).getvalue(), content_type='text/csv')
		#response2['Content-Disposition']='attachment; filename=%s' % resultName2
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart2)*1000)
		#return response2					
		
#-------------------------------------------------------------(MM10) CHROM LOCS --> QUERY RESULTS --------------------------------------------------------#	
def mm10LocQuery(uploaded_file):

	curpath2 = os.path.abspath(os.curdir)
	resultName2 = "mm10LOCresult.csv"
	#resultName2 = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath2)
	print resultName2
	print "Trying to open %s" % (os.path.join(curpath2, resultName2))
	LocList = uploaded_file.read().splitlines()						
	writingStart2 = time.clock()		
	with open(resultName2, 'w+') as f2:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		GINTER = []
		TPROM = []
		TINTRA = []
		TTERM = []
		TINTER = []
		PPROM = []
		PINTRA = []
		PTERM = []	
		PINTER = []	

	
		for line in LocList:

			All = []
			GProm = []
			GIntra = []
			GTerm = []
			GInter = []
			TProm = []
			TIntra = []
			TInter = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			PInter = []
			GG = []
			TJ = []
			PM = []	

		
			L = line.rstrip('\n').split('-')
			if len(L)==1:
				chr = str(L[0])
				tag = "Your given chromosome: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
				

							
				Q = Mm10.objects.raw('SELECT * FROM Mm10 WHERE chrom = "%s"' % (chr))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
								[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
								[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
								[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
								[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
								[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
								[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
								[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
								[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
								[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
								[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
								[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
								[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			
					A = [AssoCGI, Annot]
					All.append(A)								
					
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
								
			if len(L)>1:
				chr = str(L[0])
				chr = chr.lower()
				sLoc = int(L[1])
				eLoc = int(L[2])
				tag = "Your given locations: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")

				Q = Mm10.objects.raw('SELECT * FROM Mm10 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
								[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
								[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
								[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
								[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
								[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
								[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
								[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
								[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
								[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
								[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
								[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
								[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			
					A = [AssoCGI, Annot]
					All.append(A)								
	
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")				

			#========================= Stat Report =========================	
			for l in All:
				CGIDs = l[0][0]
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					
					GInCount = Annotations.count("Intergenic")
					GInter.append(GInCount)
					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
					TInCount = Annotations.count("Intergenic")
					TInter.append(TInCount)
					
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					PInCount = Annotations.count("Intergenic")
					PInter.append(PInCount)
					
			if len(list(Q)) == 0:
				q2 = "There are no CpG Islands found between the locations " + line + "  you provided."
				f2.write(str(q2)+ "\n" )					

			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)	
			GInter = sum(GInter)
			GINTER.append(GInter)							
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			TInter = sum(TInter)
			TINTER.append(TInter)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			PInter = sum(PInter)
			PINTER.append(PInter)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)

		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)

		TJstdL = np.std(TJLs)

		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)

		TJstdOE = np.std(TJOEs)

		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		GINTER = sum(GINTER)
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		TINTER = sum(TINTER)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)
		PINTER = sum(PINTER)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)
		

		f2.seek(0)

		mm10page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}
										</style>
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for MM10</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../mm10LOCresult">Download</a></h4>
											</div>
											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
														{
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>
									</body>
									</font>
									</head>
									</html>

									""" % (str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(GINTER), str(TPROM), str(TINTRA), str(TTERM), str(TINTER), str(PPROM), str(PINTRA), str(PTERM), str(PINTER))	



		response2 = HttpResponse(mm10page, content_type='text/html')
		return response2



		#response2 = HttpResponse(StringIO(f2.read()).getvalue(), content_type='text/csv')
		#response2['Content-Disposition']='attachment; filename=%s' % resultName2
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart2)*1000)
		#return response2					




#-------------------------------------------------------------(DM3) CHROM LOCS --> QUERY RESULTS --------------------------------------------------------#
def dm3LocQuery(uploaded_file):
    	

	curpath2 = os.path.abspath(os.curdir)
	resultName2 = "dm3LOCresult.csv"
	#resultName2 = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath2)
	print resultName2
	print "Trying to open %s" % (os.path.join(curpath2, resultName2))

	LocList = uploaded_file.read().splitlines()						
						
	writingStart2 = time.clock()		
	with open(resultName2, 'w+') as f2:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		GINTER = []
		TPROM = []
		TINTRA = []
		TTERM = []
		TINTER = []
		PPROM = []
		PINTRA = []
		PTERM = []	
		PINTER = []	
	
	
	
		for line in LocList:
		
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			GInter = []
			TProm = []
			TIntra = []
			TInter = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			PInter = []
			GG = []
			TJ = []
			PM = []	
		
			L = line.rstrip('\n').split('-')
			if len(L)==1:
				chr = str(L[0])
				tag = "Your given chromosome: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
	
				Q = Dm3.objects.raw('SELECT * FROM Dm3 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
								[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
								[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
								[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
								[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
								[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
								[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
								[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
								[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
								[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
								[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
								[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
								[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]					
					All.append(A)
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(L)>1:
				chr = str(L[0])
				chr = chr.lower()
				sLoc = int(L[1])
				eLoc = int(L[2])
				tag = "Your given locations: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
				
				Q = Dm3.objects.raw('SELECT * FROM Dm3 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26],[obj.type27, obj.genesym27 , obj.strand27, obj.refid27],
								[obj.type28, obj.genesym28 , obj.strand28, obj.refid28],[obj.type29, obj.genesym29 , obj.strand29, obj.refid29],
								[obj.type30, obj.genesym30 , obj.strand30, obj.refid30],[obj.type31, obj.genesym31 , obj.strand31, obj.refid31],
								[obj.type32, obj.genesym32 , obj.strand32, obj.refid32],[obj.type33, obj.genesym33 , obj.strand33, obj.refid33],
								[obj.type34, obj.genesym34 , obj.strand34, obj.refid34],[obj.type35, obj.genesym35 , obj.strand35, obj.refid35],
								[obj.type36, obj.genesym36 , obj.strand36, obj.refid36],[obj.type37, obj.genesym37 , obj.strand37, obj.refid37],
								[obj.type38, obj.genesym38 , obj.strand38, obj.refid38],[obj.type39, obj.genesym39 , obj.strand39, obj.refid39],
								[obj.type40, obj.genesym40 , obj.strand40, obj.refid40],[obj.type41, obj.genesym41 , obj.strand41, obj.refid41],
								[obj.type42, obj.genesym42 , obj.strand42, obj.refid42],[obj.type43, obj.genesym43 , obj.strand43, obj.refid43],
								[obj.type44, obj.genesym44 , obj.strand44, obj.refid44],[obj.type45, obj.genesym45 , obj.strand45, obj.refid45],
								[obj.type46, obj.genesym46 , obj.strand46, obj.refid46],[obj.type47, obj.genesym47 , obj.strand47, obj.refid47],
								[obj.type48, obj.genesym48 , obj.strand48, obj.refid48],[obj.type49, obj.genesym49 , obj.strand49, obj.refid49],
								[obj.type50, obj.genesym50 , obj.strand50, obj.refid50]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]
					All.append(A)								
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(list(Q)) == 0:
				q2 = "There are no CpG Islands found between the locations " + line + "  you provided."
				f2.write(str(q2)+ "\n")							

			#========================= Stat Report =========================	
			for l in All:
				CGIDs = l[0][0]
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					GInCount = Annotations.count("Intergenic")
					GInter.append(GInCount)

					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
					TInCount = Annotations.count("Intergenic")
					TInter.append(TInCount)
					
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					PInCount = Annotations.count("Intergenic")
					PInter.append(PInCount)
	

			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



			

		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)

		f2.seek(0)
		

		dm3page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}
										</style>
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for DM3</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../dm3LOCresult">Download</a></h4>
											</div>
											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
														{
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>
									</body>
									</font>
									</head>
									</html>

									""" % (str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(GINTER), str(TPROM), str(TINTRA), str(TTERM), str(TINTER), str(PPROM), str(PINTRA), str(PTERM), str(PINTER))	

		response2 = HttpResponse(dm3page, content_type='text/html')
		return response2



		#response2 = HttpResponse(StringIO(f2.read()).getvalue(), content_type='text/csv')
		#response2['Content-Disposition']='attachment; filename=%s' % resultName2
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart2)*1000)
		#return response2					


#-------------------------------------------------------------(CE10) CHROM LOCS --> QUERY RESULTS --------------------------------------------------------#
def ce10LocQuery(uploaded_file):
    
	curpath2 = os.path.abspath(os.curdir)
	resultName2 = "ce10LOCresult.csv"
	#resultName2 = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath2)
	print resultName2
	print "Trying to open %s" % (os.path.join(curpath2, resultName2))

	LocList = uploaded_file.read().splitlines()						
						
	writingStart2 = time.clock()		
	with open(resultName2, 'w+') as f2:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		GINTER = []
		TPROM = []
		TINTRA = []
		TTERM = []
		TINTER = []
		PPROM = []
		PINTRA = []
		PTERM = []	
		PINTER = []	
	
	
	
		for line in LocList:
		
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			GInter = []
			TProm = []
			TIntra = []
			TInter = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			PInter = []
			GG = []
			TJ = []
			PM = []	
		
			L = line.rstrip('\n').split('-')
			if len(L)==1:
				chr = str(L[0])
				tag = "Your given chromosome: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
	
				Q = Ce10.objects.raw('SELECT * FROM Ce10 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]					
					All.append(A)
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(L)>1:
				chr = str(L[0])
				chr = chr.lower()
				sLoc = int(L[1])
				eLoc = int(L[2])
				tag = "Your given locations: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
				
				Q = Ce10.objects.raw('SELECT * FROM Ce10 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]
					All.append(A)								
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(list(Q)) == 0:
				q2 = "There are no CpG Islands found between the locations " + line + "  you provided."
				f2.write(str(q2)+ "\n")							

			#========================= Stat Report =========================	
			for l in All:
				CGIDs = l[0][0]
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					GInCount = Annotations.count("Intergenic")
					GInter.append(GInCount)

					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
					TInCount = Annotations.count("Intergenic")
					TInter.append(TInCount)
					
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					PInCount = Annotations.count("Intergenic")
					PInter.append(PInCount)
	

			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



			

		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)

		f2.seek(0)
		

		ce10page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}
										</style>
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for CE10</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../ce10LOCresult">Download</a></h4>
											</div>
											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
														{
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>
									</body>
									</font>
									</head>
									</html>

									""" % (str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(GINTER), str(TPROM), str(TINTRA), str(TTERM), str(TINTER), str(PPROM), str(PINTRA), str(PTERM), str(PINTER))	

		response2 = HttpResponse(ce10page, content_type='text/html')
		return response2



		#response2 = HttpResponse(StringIO(f2.read()).getvalue(), content_type='text/csv')
		#response2['Content-Disposition']='attachment; filename=%s' % resultName2
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart2)*1000)
		#return response2					

#-------------------------------------------------------------(CE10) CHROM LOCS --> QUERY RESULTS --------------------------------------------------------#
def rn6LocQuery(uploaded_file):
    
	curpath2 = os.path.abspath(os.curdir)
	resultName2 = "rn6LOCresult.csv"
	#resultName2 = "results" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
	print "Current Dir : %s" % (curpath2)
	print resultName2
	print "Trying to open %s" % (os.path.join(curpath2, resultName2))

	LocList = uploaded_file.read().splitlines()						
						
	writingStart2 = time.clock()		
	with open(resultName2, 'w+') as f2:

		GGGCs = []
		GGLs = []
		GGOEs = []
		TJGCs = []
		TJLs = []
		TJOEs = []	
		PMGCs = []
		PMLs = []
		PMOEs = []		
		sumGG = []
		sumTJ = []
		sumPM = []
		GPROM = []
		GINTRA= []
		GTERM = []
		GINTER = []
		TPROM = []
		TINTRA = []
		TTERM = []
		TINTER = []
		PPROM = []
		PINTRA = []
		PTERM = []	
		PINTER = []	
	
	
	
		for line in LocList:
		
			All = []
			GProm = []
			GIntra = []
			GTerm = []
			GInter = []
			TProm = []
			TIntra = []
			TInter = []
			TTerm = []
			PProm = []
			PIntra = []
			PTerm = []
			PInter = []
			GG = []
			TJ = []
			PM = []	
		
			L = line.rstrip('\n').split('-')
			if len(L)==1:
				chr = str(L[0])
				tag = "Your given chromosome: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
	
				Q = Rn6.objects.raw('SELECT * FROM Rn6 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]					
					All.append(A)
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(L)>1:
				chr = str(L[0])
				chr = chr.lower()
				sLoc = int(L[1])
				eLoc = int(L[2])
				tag = "Your given locations: " + str(line)
				f2.write("=============" + str(tag)+ "==================" + "\n")
				header = 'CGID, chrom, CGIstart, CGIend, PerGC, Length, ObsExp, Annotation Type, GeneSym, Strand, RefSeqIDs'
				header.replace("'",'')
				f2.write(header+"\n")
				
				Q = Rn6.objects.raw('SELECT * FROM Rn6 WHERE chrom = "%s" and cgistart >= %d AND cgiend <= %d' % (chr, sLoc, eLoc))
				for obj in Q:
					AssoCGI = [obj.cgid, obj.chrom, obj.cgistart, obj.cgiend, obj.pergc, obj.length, obj.obsexp]
					AssoCGI = [str(i) for i in AssoCGI]
					Annot = [[obj.type1, obj.genesym1, obj.strand1, obj.refid1],
								[obj.type2, obj.genesym2, obj.strand2, obj.refid2],[obj.type3, obj.genesym3, obj.strand3, obj.refid3],
								[obj.type4, obj.genesym4, obj.strand4, obj.refid4],[obj.type5, obj.genesym5, obj.strand5, obj.refid5],
								[obj.type6, obj.genesym6, obj.strand6, obj.refid6],[obj.type7, obj.genesym7, obj.strand7, obj.refid7],
								[obj.type8, obj.genesym8, obj.strand8, obj.refid8],[obj.type9, obj.genesym9, obj.strand9, obj.refid9],
								[obj.type10, obj.genesym10, obj.strand10, obj.refid10],[obj.type11, obj.genesym11, obj.strand11, obj.refid11],
								[obj.type12, obj.genesym12, obj.strand12, obj.refid12],[obj.type13, obj.genesym13 , obj.strand13, obj.refid13],
								[obj.type14, obj.genesym14 , obj.strand14, obj.refid14],[obj.type15, obj.genesym15 , obj.strand15, obj.refid15],
								[obj.type16, obj.genesym16 , obj.strand16, obj.refid16],[obj.type17, obj.genesym17 , obj.strand17, obj.refid17],
								[obj.type18, obj.genesym18 , obj.strand18, obj.refid18],[obj.type19, obj.genesym19 , obj.strand19, obj.refid19],
								[obj.type20, obj.genesym20 , obj.strand20, obj.refid20],[obj.type21, obj.genesym21 , obj.strand21, obj.refid21],
								[obj.type22, obj.genesym22 , obj.strand22, obj.refid22],[obj.type23, obj.genesym23 , obj.strand23, obj.refid23],
								[obj.type24, obj.genesym24 , obj.strand24, obj.refid24],[obj.type25, obj.genesym25 , obj.strand25, obj.refid25],
								[obj.type26, obj.genesym26 , obj.strand26, obj.refid26]]						
					Annot = [x for x in Annot if x != ['','','','']]	
					Annot = [map(str,i) for i in Annot]			

					A = [AssoCGI, Annot]
					All.append(A)								
					
					A = str(A)
					A = A.replace('[','')
					A = A.replace(']','')
					A = A.replace("'",'')
					f2.write(str(A) + "\n")	
			if len(list(Q)) == 0:
				q2 = "There are no CpG Islands found between the locations " + line + "  you provided."
				f2.write(str(q2)+ "\n")							

			#========================= Stat Report =========================	
			for l in All:
				CGIDs = l[0][0]
				#perGCs = l[0][4]
				#Lengths = l[0][5]
				#OEs = l[0][6]
				Annotations = flatten(l[1])
				if CGIDs.find("GG") != -1:
					G = CGIDs.count('GG') 
					GG.append(G) # Number of CGIs found by GG algorithm
										
					# CGI properties
					GGGCs.append(float(l[0][4])) # GC percentages by GG
					GGLs.append(float(l[0][5])) # Lengths by GG
					GGOEs.append(float(l[0][6])) # OE ratios by GG
					
					GPCount = Annotations.count("Promoter")
					GProm.append(GPCount) # Number of 'Promoter' Types found by GG
					
					GICount = Annotations.count("Intragenic")
					GIntra.append(GICount) # Number of 'Intragenic' Types found by GG
					
					GGCount = Annotations.count("Gene-terminal")
					GTerm.append(GGCount) # Number of 'Gene-terminal' Types found by GG
					GInCount = Annotations.count("Intergenic")
					GInter.append(GInCount)

					
				if CGIDs.find("TJ") != -1:
					T = CGIDs.count('TJ')
					TJ.append(T) # Number of CGIs found by TJ algorithm
					
					TJGCs.append(float(l[0][4]))
					TJLs.append(float(l[0][5]))
					TJOEs.append(float(l[0][6]))	
														
					TPCount = Annotations.count("Promoter")
					TProm.append(TPCount)
					TICount = Annotations.count("Intragenic")
					TIntra.append(TICount)
					TGCount = Annotations.count("Gene-terminal")
					TTerm.append(TGCount)
					TInCount = Annotations.count("Intergenic")
					TInter.append(TInCount)
					
				if CGIDs.find("PM") != -1:
					P = CGIDs.count('PM')
					PM.append(P)
					
					PMGCs.append(float(l[0][4]))
					PMLs.append(float(l[0][5]))
					PMOEs.append(float(l[0][6]))
										
					PPCount = Annotations.count("Promoter")
					PProm.append(PPCount)
					PICount = Annotations.count("Intragenic")
					PIntra.append(PICount)
					PGCount = Annotations.count("Gene-terminal")
					PTerm.append(PGCount)
					PInCount = Annotations.count("Intergenic")
					PInter.append(PInCount)
	

			GProm = sum(GProm)
			GPROM.append(GProm)	
			GIntra = sum(GIntra)
			GINTRA.append(GIntra)			
			GTerm = sum(GTerm)
			GTERM.append(GTerm)								
			TProm = sum(TProm)
			TPROM.append(TProm)			
			TIntra = sum(TIntra)
			TINTRA.append(TIntra)			
			TTerm = sum(TTerm)
			TTERM.append(TTerm)
			PProm = sum(PProm)
			PPROM.append(PProm)
			PIntra = sum(PIntra)
			PINTRA.append(PIntra)
			PTerm = sum(PTerm)
			PTERM.append(PTerm)
			
			# CGI Figure 4 data
					
			GG = sum(GG)
			TJ = sum(TJ)
			PM = sum(PM)			
			sumGG.append(GG)
			sumTJ.append(TJ)
			sumPM.append(PM)



			

		# CGI Figure 1 data
		GGavgGC = np.average(GGGCs)
		GGstdGC = np.std(GGGCs)
		TJavgGC = np.average(TJGCs)
		TJstdGC = np.std(TJGCs)
		PMavgGC = np.average(PMGCs)
		PMstdGC = np.std(PMGCs)

		# CGI Figure 2 data
		GGavgL = np.average(GGLs)
		GGstdL = np.std(GGLs)
		TJavgL = np.average(TJLs)
		TJstdL = np.std(TJLs)
		PMavgL = np.average(PMLs)
		PMstdL = np.std(PMLs)
		
		# CGI Figure 3 data
		GGavgOE = np.average(GGOEs)
		GGstdOE = np.std(GGOEs)
		TJavgOE = np.average(TJOEs)
		TJstdOE = np.std(TJOEs)
		PMavgOE = np.average(PMOEs)
		PMstdOE = np.std(PMOEs)


		# Annotation Information			
		GPROM = sum(GPROM) 
		GINTRA = sum(GINTRA) 
		GTERM = sum(GTERM) 
		TPROM = sum(TPROM)
		TINTRA = sum(TINTRA)
		TTERM = sum(TTERM)
		PPROM = sum(PPROM)
		PINTRA = sum(PINTRA)
		PTERM = sum(PTERM)			
			
		# CGI Properties
		sumGG = sum(sumGG)
		sumTJ = sum(sumTJ)
		sumPM = sum(sumPM)

		f2.seek(0)
		

		rn6page = """<!DOCTYPE html>
									<html>
									<head>
									<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
									<script src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
										<style>
											div.container {
												width: 800px;
												margin-left: 100px;
											}
										</style>
										<font size="2">
										<body style='font-family:"Verdana"'>							
											<center><h1>Results for RN6</h1></center>
											<br></br> 
											<div class="container">
												<h4>Your file is ready to <a href="../../rn6LOCresult">Download</a></h4>
											</div>
											<br></br>
											<center>
											<div class="container">
												<center><div id="myDiv" style="width: 900px; height: 600px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
													
													function getNum(val) {
														var n = parseFloat(val);
														if (isNaN(n)) {
															return 0;
														}
														else{
															return n;
														}														
													}
														var trace1 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg GC',                     
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},
														type: 'bar'
														};

														var trace2 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'),getNum('%s')],
														name: 'Avg Length',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x2',
														yaxis: 'y2',
														type: 'bar'
														};

														var trace3 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'),getNum('%s'), getNum('%s')],
														name: 'Avg Observed/Expected Ratio',
														error_y: {
															type: 'data',
															array: [getNum('%s'),getNum('%s'),getNum('%s')],
															visible: true
														},  
														xaxis: 'x3',
														yaxis: 'y3',
														type: 'bar'
														};

														var trace4 = {
														x: ['GG-F', 'TJ', 'PM'],
														y: [getNum('%s'), getNum('%s'),getNum('%s')], 
														name: 'Number of CGI found',
														xaxis: 'x4',
														yaxis: 'y4',
														type: 'bar'
														};

														var data = [trace1, trace2, trace3, trace4];

														var layout = {
															xaxis: {domain: [0, 0.45]},
															yaxis: {domain: [0, 0.45]},
															xaxis4: {
																domain: [0.55, 1],
																anchor: 'y4'
															},
															xaxis3: {
																domain: [0, 0.45],
																anchor: 'y3'
															},
															xaxis2: {domain: [0.55, 1]},
															yaxis2: {
																domain: [0, 0.45],
																anchor: 'x2'
															},
															yaxis3: {domain: [0.55, 1]},
															yaxis4: {
																domain: [0.55, 1],
																anchor: 'x4'
															}
														};

														Plotly.newPlot('myDiv', data, layout);
													</script>					
											</div>
											</center>
											<div class="container">
												  <center><div id="myDiv2" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div></center>
													<script>
														function getNum(val) {
															var n = parseFloat(val);
															if (isNaN(n)) {
																return 0;
															}
															else{
																return n;
															}														
														}													
														
														var data = [
														{
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'GG-F',
														textposition: 'inside',
														domain: {
															x: [0, .32]
														},
														name: 'GG-F Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'TJ',
														textposition: 'inside',
														domain: {
															x: [.34, .66]
														},
														name: 'TJ Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},
																	
														type: 'pie'
														}, {
														values: [getNum('%s'),getNum('%s'),getNum('%s'),getNum('%s')],
														labels: ['Promoter', 'Intragenic', 'Gene-Terminal','Intergenic'],
														text: 'PM',
														textposition: 'inside',
														domain: {
															x: [.68, 1]
														},
														name: 'PM Annotations',
														hoverinfo: 'label+percent+name',
														hole: .5,
														marker: {'colors': ['rgb(255,127,80)',
																						'rgb(152,251,152)',
																						'rgb(255,215,0)',
																						'rgb(135,206,235)']},														
														type: 'pie'
														}, ];

														var layout = {
														title: 'Annotation Stats by Three Algorithms',
														annotations: [{
															font: {
															size: 14
															},
															showarrow: false,
															text: 'GG-F',
															x: 0.11,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'TJ',
															x: 0.48,
															y: 0.5
														}, {
															font: {
															size: 14
															},
															showarrow: false,
															text: 'PM',
															x: 0.88,
															y: 0.5

														}],
														height: 500,
														width: 800
														};

														Plotly.newPlot('myDiv2', data, layout);														
														
													</script>
											
											</div>
									</body>
									</font>
									</head>
									</html>

									""" % (str(GGavgGC), str(TJavgGC), str(PMavgGC), str(GGstdGC), str(TJstdGC), str(PMstdGC),str(GGavgL), str(TJavgL), str(PMavgL), str(GGstdL), str(TJstdL), str(PMstdL), str(GGavgOE), str(TJavgOE), str(PMavgOE), str(GGstdOE), str(TJstdOE), str(PMstdOE), str(sumGG), str(sumTJ), str(sumPM), str(GPROM), str(GINTRA), str(GTERM), str(GINTER), str(TPROM), str(TINTRA), str(TTERM), str(TINTER), str(PPROM), str(PINTRA), str(PTERM), str(PINTER))	

		response2 = HttpResponse(rn6page, content_type='text/html')
		return response2

		#response2 = HttpResponse(StringIO(f2.read()).getvalue(), content_type='text/csv')
		#response2['Content-Disposition']='attachment; filename=%s' % resultName2
		#print "-----------------WRITING RESULTS END --------- time spent : %s ms -------" % ((time.clock() - writingStart2)*1000)
		#return response2




#---------------------------------------------------------------------  HANDLING FILES  -----------------------------------------------------------------#

def handleInputs1(uploaded_file,mm):
	if(mm == "hs"):
		return hg38IDQuery(uploaded_file)
	elif(mm == "mm"):
		return mm10IDQuery(uploaded_file)
	elif(mm == "dm"):
		return dm3IDQuery(uploaded_file)
	elif(mm == "ce"):
		return ce10IDQuery(uploaded_file)
	elif(mm == "rn"):
		return rn6IDQuery(uploaded_file)
	else:
		raise RuntimeError("Invalid Organism")
	
		
def handleInputs2(uploaded_file,mm):
	if (mm == "hs"):
		return hg38IDQuery(uploaded_file)
	elif (mm == "mm"):
		return mm10IDQuery(uploaded_file)
	elif (mm == "dm"):
		return dm3IDQuery(uploaded_file)
	elif (mm == "ce"):
		return ce10IDQuery(uploaded_file)
	elif (mm == "rn"):
		return rn6IDQuery(uploaded_file)
	else:
		raise RuntimeError("Invalid organism")
    
def handleInputs3(uploaded_file,mm):
	if (mm == "hs"):
		return hg38LocQuery(uploaded_file)
	elif (mm == "mm"):
		return mm10LocQuery(uploaded_file)
	elif (mm == "dm"):
		return dm3LocQuery(uploaded_file)
	elif (mm == "ce"):
		return ce10LocQuery(uploaded_file)
	elif (mm == "rn"):
		return rn6LocQuery(uploaded_file)
	else:
		raise RuntimeError("Invalid organism")


def index(request):

    # if this is a POST request we need to process the form data
	print request.method
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = DocumentForm(request.POST, request.FILES)
		IDform = IDForm(request.POST, request.FILES)
		locForm = DocumentForm2(request.POST,request.FILES)
		# check whether it's valid:
		if form.is_valid():
			mm = form.cleaned_data['main_menu']
			#print mm
			#print form.cleaned_data.keys()
			#fl1 = request.FILES['upload_file']
			#fl3 = request.FILES['loc_file']
			#return handleInputs1(fl1,mm)

			if IDform.is_valid():
				#mm = IDform.cleaned_data['main_menu']
				fl1 = request.FILES['upload_file']
				return handleInputs1(fl1,mm)
			if locForm.is_valid():
				# process the data in form.cleaned_data as required
				#mm = locForm.cleaned_data['main_menu']
				print mm
				fl3 = request.FILES['loc_file']	 
				return handleInputs3(fl3,mm)
				# redirect to a new URL:
				#return HttpResponseRedirect('/thanks/')
				# if a GET (or any other method) we'll create a blank form
	else:
		form = DocumentForm()
		IDform = IDForm()
		locForm = DocumentForm2()
		
	return render(request, 'index.html', {'form': form, 'IDform': IDform, 'locForm': locForm})
