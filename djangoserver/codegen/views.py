from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import argparse
import sympy
from sympy import Symbol, latex
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
#from . models import Question
import os
import cv2
import numpy as np
import urllib
import png
import subprocess

def preprocess(request):
	im = urllib.urlretrieve("http://192.168.43.171/uploads/test.png")
	img = cv2.imread(im[0])               

	retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

	grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	retval2, threshold2 = cv2.threshold(grayscaled,12, 255, cv2.THRESH_BINARY)
	#gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	retval,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	png.from_array(otsu, 'L').save("codegen/resultimgs/aar.png")
	#cv2.imshow('original',img)
	#cv2.imshow('threshold',threshold)
	#cv2.imshow('threshold2',threshold2)
	#cv2.imshow('gaus',gaus)
	#cv2.imwrite('testbout.png',gaus)
	#cv2.imshow('otsu',otsu)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows
#	return HttpResponse("success")


#def call(request):
	os.system("tesseract codegen/resultimgs/aar.png codegen/resultimgs/out")
#	return HttpResponse("success")

#def codegen(request):
	a = sympy.symbols("a")
	b = sympy.symbols("b")
	c = sympy.symbols("c")
	d = sympy.symbols("d")
	e = sympy.symbols("e")
	f = sympy.symbols("f")
	g = sympy.symbols("g")
	h = sympy.symbols("h")
	i = sympy.symbols("i")
	j = sympy.symbols("j")
	k = sympy.symbols("k")
	l = sympy.symbols("l")
	m = sympy.symbols("m")
	n = sympy.symbols("n")
	o = sympy.symbols("o")
	p = sympy.symbols("p")
	q = sympy.symbols("q")
	r = sympy.symbols("r")
	s = sympy.symbols("s")
	t = sympy.symbols("t")
	u = sympy.symbols("u")
	v = sympy.symbols("v")
	w = sympy.symbols("w")
	x = sympy.symbols("x")
	y = sympy.symbols("y")
	z = sympy.symbols("z")


	A = sympy.symbols("A")
	B = sympy.symbols("B")
	C = sympy.symbols("C")
	D = sympy.symbols("D")
	E = sympy.symbols("E")
	F = sympy.symbols("F")
	G = sympy.symbols("G")
	H = sympy.symbols("H")
	I = sympy.symbols("I")
	J = sympy.symbols("J")
	K = sympy.symbols("K")
	L = sympy.symbols("L")
	M = sympy.symbols("M")
	N = sympy.symbols("N")
	O = sympy.symbols("O")
	P = sympy.symbols("P")
	Q = sympy.symbols("Q")
	R = sympy.symbols("R")
	S = sympy.symbols("S")
	T = sympy.symbols("T")
	U = sympy.symbols("U")
	V = sympy.symbols("V")
	W = sympy.symbols("W")
	X = sympy.symbols("X")
	Y = sympy.symbols("Y")
	Z = sympy.symbols("Z")

	with open('codegen/resultimgs/out.txt', 'r') as myfile:
		data=myfile.read().replace('\n', '')

	latexcode=sympy.latex(eval(data))


	text_file = open("codegen/resultimgs/final.tex", "w")
	text_file.write("%s" % latexcode)
	text_file.close()

	#send mail
	
	fromaddr = "latexprojectmec@gmail.com"
	toaddr = "jithuandjinu@gmail.com"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Latexcode"
	 
	body = "Latex code to the image "
	 
	msg.attach(MIMEText(body, 'plain'))
	 
	filename = "final.tex"
	attachment = open("codegen/resultimgs/final.tex", "rb")
	 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	msg.attach(part)
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "12089181")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	return HttpResponse("Success")