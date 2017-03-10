from django import forms
from django.utils.safestring import mark_safe
from .views import *

    
ORGANISM_CHOICES = (("", "Please select..."),("hs", "Homo sapiens"),
                    ("mm", "Mus musculus"),
                    ("dm", "Drosophila melanogaster"),
                    ("ce", "Caenorhabditis elegans"),
                    ("rn", "Rattus norvegicus"))    

ALGORITHM_CHOICES = (("gg", "Gardiner-Garden and Frommer"),
                     ("tj", "Takai & Jones"),
                     ("pm", "Ponger & Mouchiroud"))

ASSEMBLY_CHOICES_HS = (("hg19", "Feb. 2009 (hg19, GRCh37)"),
                        ("hg38", "Dec. 2013 (hg38, GRCh38)"),
                        ("hg18", "Mar. 2006 (hg18, NCBI36)"),
                        ("hg17", "May. 2004 (hg17, NCBI35)"),
                        ("hg16", "Jul. 2003 (hg16, NCBI34)"))

ASSEMBLY_CHOICES_MM = (("mm10", "Dec. 2011 (mm10, GRCm38)"),
                       ("mm9", "Jul. 2007 (mm9, NCBI37)"))


INPUT_LIST_CHOICES = (("Mixed", "My input has mixed input IDs"),
                      ("1","Affy ID"),
                      ("2","EC Number"),
                      ("3","Ensembl Gene ID"),
                      ("4","Ensembl Protein ID"),
                      ("5","Ensembl Transcript ID"),
                      ("6","FlyBase Gene ID"),
                      ("7","Gene ID"),
                      ("8","Genbank Nucleotide Accession"),
                      ("9","Genbank Protein Accession"),
                      ("10","Gene Symbol"),
                      ("11","Gene Symbol and Synonyms"),
                      ("12","GI Number"),
                      ("13","GO ID"),
                      ("14","GSEA Standard Name"),
                      ("15","HGNC ID"),
                      ("16","Illumina ID"),
                      ("17","Kegg Gene ID"),
                      ("18","PDB ID"),
                      ("19","Pfam ID"),
                      ("20","RefSeq Genomic Accession"),
                      ("21","RefSeq mRNA Accession"),
                      ("22","RefSeq Protein Accession"),
                      ("23","UniGene ID"),
                      ("24","PIR ID"))
                      

class DocumentForm(forms.Form):
    main_menu = forms.ChoiceField(label="Select Organism", choices=ORGANISM_CHOICES, widget=forms.Select(attrs={'onchange' : "displayAccordingly()"}))
    Select_Input = forms.ChoiceField(label="Select Input Type:", choices=INPUT_LIST_CHOICES)

class IDForm(forms.Form):
    #main_menu = forms.ChoiceField(label="Select Organism", choices=ORGANISM_CHOICES, widget=forms.Select(attrs={'onchange' : "displayAccordingly()"}))
    

    #Select_Assembly_for_Homo_sapiens = forms.ChoiceField(label="Please select", choices=ASSEMBLY_CHOICES_HS)

    #Select_Assembly_for_Mus_musculus = forms.ChoiceField(label="Please select", choices=ASSEMBLY_CHOICES_MM)

    #main_menu = forms.ChoiceField(label="Please select organism, followed by assembly:", choices=ORGS)
    
    #Select_Input = forms.ChoiceField(label="Select Input Type:", choices=INPUT_LIST_CHOICES)

    upload_file = forms.FileField(label="Please upload Gene ID File: ")
    
class DocumentForm2(forms.Form):
    loc_file = forms.FileField(label="Please upload Chromosomal Location File: ")
    

class InitialForm(forms.Form):
    Select_Organism = forms.ChoiceField(label="Select Organism", choices=ORGANISM_CHOICES, widget=forms.Select
    (attrs={'onchange' : "assCaller(this.value);"}))
    
    
