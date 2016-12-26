from django.db import models



class Ce10(models.Model):
    cgid = models.CharField(db_column='CGID', primary_key=True, max_length=255)  # Field name made lowercase.
    chrom = models.CharField(max_length=255)
    cgistart = models.IntegerField(db_column='CGIstart')  # Field name made lowercase.
    cgiend = models.IntegerField(db_column='CGIend')  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    pergc = models.DecimalField(db_column='perGC', max_digits=3, decimal_places=1)  # Field name made lowercase.
    obsexp = models.DecimalField(db_column='ObsExp', max_digits=4, decimal_places=3)  # Field name made lowercase.
    type1 = models.CharField(db_column='Type1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym1 = models.CharField(db_column='GeneSym1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    refid1 = models.CharField(db_column='RefID1', max_length=800, blank=True, null=True)  # Field name made lowercase.
    strand1 = models.CharField(db_column='Strand1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type2 = models.CharField(db_column='Type2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym2 = models.CharField(db_column='GeneSym2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    refid2 = models.CharField(db_column='RefID2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand2 = models.CharField(db_column='Strand2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type3 = models.CharField(db_column='Type3', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym3 = models.CharField(db_column='GeneSym3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    refid3 = models.CharField(db_column='RefID3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand3 = models.CharField(db_column='Strand3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type4 = models.CharField(db_column='Type4', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym4 = models.CharField(db_column='GeneSym4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    refid4 = models.CharField(db_column='RefID4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand4 = models.CharField(db_column='Strand4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type5 = models.CharField(db_column='Type5', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym5 = models.CharField(db_column='GeneSym5', max_length=11, blank=True, null=True)  # Field name made lowercase.
    refid5 = models.CharField(db_column='RefID5', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand5 = models.CharField(db_column='Strand5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type6 = models.CharField(db_column='Type6', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym6 = models.CharField(db_column='GeneSym6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid6 = models.CharField(db_column='RefID6', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand6 = models.CharField(db_column='Strand6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type7 = models.CharField(db_column='Type7', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym7 = models.CharField(db_column='GeneSym7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid7 = models.CharField(db_column='RefID7', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand7 = models.CharField(db_column='Strand7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type8 = models.CharField(db_column='Type8', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym8 = models.CharField(db_column='GeneSym8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid8 = models.CharField(db_column='RefID8', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand8 = models.CharField(db_column='Strand8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type9 = models.CharField(db_column='Type9', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym9 = models.CharField(db_column='GeneSym9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid9 = models.CharField(db_column='RefID9', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand9 = models.CharField(db_column='Strand9', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type10 = models.CharField(db_column='Type10', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym10 = models.CharField(db_column='GeneSym10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid10 = models.CharField(db_column='RefID10', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand10 = models.CharField(db_column='Strand10', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type11 = models.CharField(db_column='Type11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym11 = models.CharField(db_column='GeneSym11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid11 = models.CharField(db_column='RefID11', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand11 = models.CharField(db_column='Strand11', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type12 = models.CharField(db_column='Type12', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym12 = models.CharField(db_column='GeneSym12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid12 = models.CharField(db_column='RefID12', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand12 = models.CharField(db_column='Strand12', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type13 = models.CharField(db_column='Type13', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym13 = models.CharField(db_column='GeneSym13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid13 = models.CharField(db_column='RefID13', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand13 = models.CharField(db_column='Strand13', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type14 = models.CharField(db_column='Type14', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym14 = models.CharField(db_column='GeneSym14', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid14 = models.CharField(db_column='RefID14', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand14 = models.CharField(db_column='Strand14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type15 = models.CharField(db_column='Type15', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym15 = models.CharField(db_column='GeneSym15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid15 = models.CharField(db_column='RefID15', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand15 = models.CharField(db_column='Strand15', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type16 = models.CharField(db_column='Type16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym16 = models.CharField(db_column='GeneSym16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refid16 = models.CharField(db_column='RefID16', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand16 = models.CharField(db_column='Strand16', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type17 = models.CharField(db_column='Type17', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym17 = models.CharField(db_column='GeneSym17', max_length=9, blank=True, null=True)  # Field name made lowercase.
    refid17 = models.CharField(db_column='RefID17', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand17 = models.CharField(db_column='Strand17', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type18 = models.CharField(db_column='Type18', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym18 = models.CharField(db_column='GeneSym18', max_length=9, blank=True, null=True)  # Field name made lowercase.
    refid18 = models.CharField(db_column='RefID18', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand18 = models.CharField(db_column='Strand18', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type19 = models.CharField(db_column='Type19', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym19 = models.CharField(db_column='GeneSym19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    refid19 = models.CharField(db_column='RefID19', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand19 = models.CharField(db_column='Strand19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type20 = models.CharField(db_column='Type20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    genesym20 = models.CharField(db_column='GeneSym20', max_length=6, blank=True, null=True)  # Field name made lowercase.
    refid20 = models.CharField(db_column='RefID20', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand20 = models.CharField(db_column='Strand20', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type21 = models.CharField(db_column='Type21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym21 = models.CharField(db_column='GeneSym21', max_length=6, blank=True, null=True)  # Field name made lowercase.
    refid21 = models.CharField(db_column='RefID21', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand21 = models.CharField(db_column='Strand21', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type22 = models.CharField(db_column='Type22', max_length=13, blank=True, null=True)  # Field name made lowercase.
    genesym22 = models.CharField(db_column='GeneSym22', max_length=7, blank=True, null=True)  # Field name made lowercase.
    refid22 = models.CharField(db_column='RefID22', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand22 = models.CharField(db_column='Strand22', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type23 = models.CharField(db_column='Type23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym23 = models.CharField(db_column='GeneSym23', max_length=7, blank=True, null=True)  # Field name made lowercase.
    refid23 = models.CharField(db_column='RefID23', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand23 = models.CharField(db_column='Strand23', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type24 = models.CharField(db_column='Type24', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym24 = models.CharField(db_column='GeneSym24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    refid24 = models.CharField(db_column='RefID24', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand24 = models.CharField(db_column='Strand24', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type25 = models.CharField(db_column='Type25', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym25 = models.CharField(db_column='GeneSym25', max_length=7, blank=True, null=True)  # Field name made lowercase.
    refid25 = models.CharField(db_column='RefID25', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand25 = models.CharField(db_column='Strand25', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type26 = models.CharField(db_column='Type26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genesym26 = models.CharField(db_column='GeneSym26', max_length=7, blank=True, null=True)  # Field name made lowercase.
    refid26 = models.CharField(db_column='RefID26', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strand26 = models.CharField(db_column='Strand26', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ce10'


class Dm3(models.Model):
    cgid = models.CharField(db_column='CGID', primary_key=True, max_length=255)  # Field name made lowercase.
    chrom = models.TextField()
    cgistart = models.IntegerField(db_column='CGIstart')  # Field name made lowercase.
    cgiend = models.IntegerField(db_column='CGIend')  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    pergc = models.FloatField(db_column='perGC')  # Field name made lowercase.
    obsexp = models.FloatField(db_column='ObsExp')  # Field name made lowercase.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase.
    genesym1 = models.IntegerField(db_column='GeneSym1', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.TextField(db_column='RefID1', blank=True, null=True)  # Field name made lowercase.
    strand1 = models.TextField(db_column='Strand1', blank=True, null=True)  # Field name made lowercase.
    type2 = models.TextField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    genesym2 = models.TextField(db_column='GeneSym2', blank=True, null=True)  # Field name made lowercase.
    refid2 = models.TextField(db_column='RefID2', blank=True, null=True)  # Field name made lowercase.
    strand2 = models.TextField(db_column='Strand2', blank=True, null=True)  # Field name made lowercase.
    type3 = models.TextField(db_column='Type3', blank=True, null=True)  # Field name made lowercase.
    genesym3 = models.TextField(db_column='GeneSym3', blank=True, null=True)  # Field name made lowercase.
    refid3 = models.TextField(db_column='RefID3', blank=True, null=True)  # Field name made lowercase.
    strand3 = models.TextField(db_column='Strand3', blank=True, null=True)  # Field name made lowercase.
    type4 = models.TextField(db_column='Type4', blank=True, null=True)  # Field name made lowercase.
    genesym4 = models.TextField(db_column='GeneSym4', blank=True, null=True)  # Field name made lowercase.
    refid4 = models.TextField(db_column='RefID4', blank=True, null=True)  # Field name made lowercase.
    strand4 = models.TextField(db_column='Strand4', blank=True, null=True)  # Field name made lowercase.
    type5 = models.TextField(db_column='Type5', blank=True, null=True)  # Field name made lowercase.
    genesym5 = models.TextField(db_column='GeneSym5', blank=True, null=True)  # Field name made lowercase.
    refid5 = models.TextField(db_column='RefID5', blank=True, null=True)  # Field name made lowercase.
    strand5 = models.TextField(db_column='Strand5', blank=True, null=True)  # Field name made lowercase.
    type6 = models.TextField(db_column='Type6', blank=True, null=True)  # Field name made lowercase.
    genesym6 = models.TextField(db_column='GeneSym6', blank=True, null=True)  # Field name made lowercase.
    refid6 = models.TextField(db_column='RefID6', blank=True, null=True)  # Field name made lowercase.
    strand6 = models.TextField(db_column='Strand6', blank=True, null=True)  # Field name made lowercase.
    type7 = models.TextField(db_column='Type7', blank=True, null=True)  # Field name made lowercase.
    genesym7 = models.TextField(db_column='GeneSym7', blank=True, null=True)  # Field name made lowercase.
    refid7 = models.TextField(db_column='RefID7', blank=True, null=True)  # Field name made lowercase.
    strand7 = models.TextField(db_column='Strand7', blank=True, null=True)  # Field name made lowercase.
    type8 = models.TextField(db_column='Type8', blank=True, null=True)  # Field name made lowercase.
    genesym8 = models.TextField(db_column='GeneSym8', blank=True, null=True)  # Field name made lowercase.
    refid8 = models.TextField(db_column='RefID8', blank=True, null=True)  # Field name made lowercase.
    strand8 = models.TextField(db_column='Strand8', blank=True, null=True)  # Field name made lowercase.
    type9 = models.TextField(db_column='Type9', blank=True, null=True)  # Field name made lowercase.
    genesym9 = models.TextField(db_column='GeneSym9', blank=True, null=True)  # Field name made lowercase.
    refid9 = models.TextField(db_column='RefID9', blank=True, null=True)  # Field name made lowercase.
    strand9 = models.TextField(db_column='Strand9', blank=True, null=True)  # Field name made lowercase.
    type10 = models.TextField(db_column='Type10', blank=True, null=True)  # Field name made lowercase.
    genesym10 = models.TextField(db_column='GeneSym10', blank=True, null=True)  # Field name made lowercase.
    refid10 = models.TextField(db_column='RefID10', blank=True, null=True)  # Field name made lowercase.
    strand10 = models.TextField(db_column='Strand10', blank=True, null=True)  # Field name made lowercase.
    type11 = models.TextField(db_column='Type11', blank=True, null=True)  # Field name made lowercase.
    genesym11 = models.TextField(db_column='GeneSym11', blank=True, null=True)  # Field name made lowercase.
    refid11 = models.TextField(db_column='RefID11', blank=True, null=True)  # Field name made lowercase.
    strand11 = models.TextField(db_column='Strand11', blank=True, null=True)  # Field name made lowercase.
    type12 = models.TextField(db_column='Type12', blank=True, null=True)  # Field name made lowercase.
    genesym12 = models.TextField(db_column='GeneSym12', blank=True, null=True)  # Field name made lowercase.
    refid12 = models.TextField(db_column='RefID12', blank=True, null=True)  # Field name made lowercase.
    strand12 = models.TextField(db_column='Strand12', blank=True, null=True)  # Field name made lowercase.
    type13 = models.TextField(db_column='Type13', blank=True, null=True)  # Field name made lowercase.
    genesym13 = models.TextField(db_column='GeneSym13', blank=True, null=True)  # Field name made lowercase.
    refid13 = models.TextField(db_column='RefID13', blank=True, null=True)  # Field name made lowercase.
    strand13 = models.TextField(db_column='Strand13', blank=True, null=True)  # Field name made lowercase.
    type14 = models.TextField(db_column='Type14', blank=True, null=True)  # Field name made lowercase.
    genesym14 = models.TextField(db_column='GeneSym14', blank=True, null=True)  # Field name made lowercase.
    refid14 = models.TextField(db_column='RefID14', blank=True, null=True)  # Field name made lowercase.
    strand14 = models.TextField(db_column='Strand14', blank=True, null=True)  # Field name made lowercase.
    type15 = models.TextField(db_column='Type15', blank=True, null=True)  # Field name made lowercase.
    genesym15 = models.TextField(db_column='GeneSym15', blank=True, null=True)  # Field name made lowercase.
    refid15 = models.TextField(db_column='RefID15', blank=True, null=True)  # Field name made lowercase.
    strand15 = models.TextField(db_column='Strand15', blank=True, null=True)  # Field name made lowercase.
    type16 = models.TextField(db_column='Type16', blank=True, null=True)  # Field name made lowercase.
    genesym16 = models.TextField(db_column='GeneSym16', blank=True, null=True)  # Field name made lowercase.
    refid16 = models.TextField(db_column='RefID16', blank=True, null=True)  # Field name made lowercase.
    strand16 = models.TextField(db_column='Strand16', blank=True, null=True)  # Field name made lowercase.
    type17 = models.TextField(db_column='Type17', blank=True, null=True)  # Field name made lowercase.
    genesym17 = models.TextField(db_column='GeneSym17', blank=True, null=True)  # Field name made lowercase.
    refid17 = models.TextField(db_column='RefID17', blank=True, null=True)  # Field name made lowercase.
    strand17 = models.TextField(db_column='Strand17', blank=True, null=True)  # Field name made lowercase.
    type18 = models.TextField(db_column='Type18', blank=True, null=True)  # Field name made lowercase.
    genesym18 = models.TextField(db_column='GeneSym18', blank=True, null=True)  # Field name made lowercase.
    refid18 = models.TextField(db_column='RefID18', blank=True, null=True)  # Field name made lowercase.
    strand18 = models.TextField(db_column='Strand18', blank=True, null=True)  # Field name made lowercase.
    type19 = models.TextField(db_column='Type19', blank=True, null=True)  # Field name made lowercase.
    genesym19 = models.TextField(db_column='GeneSym19', blank=True, null=True)  # Field name made lowercase.
    refid19 = models.TextField(db_column='RefID19', blank=True, null=True)  # Field name made lowercase.
    strand19 = models.TextField(db_column='Strand19', blank=True, null=True)  # Field name made lowercase.
    type20 = models.TextField(db_column='Type20', blank=True, null=True)  # Field name made lowercase.
    genesym20 = models.TextField(db_column='GeneSym20', blank=True, null=True)  # Field name made lowercase.
    refid20 = models.TextField(db_column='RefID20', blank=True, null=True)  # Field name made lowercase.
    strand20 = models.TextField(db_column='Strand20', blank=True, null=True)  # Field name made lowercase.
    type21 = models.TextField(db_column='Type21', blank=True, null=True)  # Field name made lowercase.
    genesym21 = models.TextField(db_column='GeneSym21', blank=True, null=True)  # Field name made lowercase.
    refid21 = models.TextField(db_column='RefID21', blank=True, null=True)  # Field name made lowercase.
    strand21 = models.TextField(db_column='Strand21', blank=True, null=True)  # Field name made lowercase.
    type22 = models.TextField(db_column='Type22', blank=True, null=True)  # Field name made lowercase.
    genesym22 = models.TextField(db_column='GeneSym22', blank=True, null=True)  # Field name made lowercase.
    refid22 = models.TextField(db_column='RefID22', blank=True, null=True)  # Field name made lowercase.
    strand22 = models.TextField(db_column='Strand22', blank=True, null=True)  # Field name made lowercase.
    type23 = models.TextField(db_column='Type23', blank=True, null=True)  # Field name made lowercase.
    genesym23 = models.TextField(db_column='GeneSym23', blank=True, null=True)  # Field name made lowercase.
    refid23 = models.TextField(db_column='RefID23', blank=True, null=True)  # Field name made lowercase.
    strand23 = models.TextField(db_column='Strand23', blank=True, null=True)  # Field name made lowercase.
    type24 = models.TextField(db_column='Type24', blank=True, null=True)  # Field name made lowercase.
    genesym24 = models.TextField(db_column='GeneSym24', blank=True, null=True)  # Field name made lowercase.
    refid24 = models.TextField(db_column='RefID24', blank=True, null=True)  # Field name made lowercase.
    strand24 = models.TextField(db_column='Strand24', blank=True, null=True)  # Field name made lowercase.
    type25 = models.TextField(db_column='Type25', blank=True, null=True)  # Field name made lowercase.
    genesym25 = models.TextField(db_column='GeneSym25', blank=True, null=True)  # Field name made lowercase.
    refid25 = models.TextField(db_column='RefID25', blank=True, null=True)  # Field name made lowercase.
    strand25 = models.TextField(db_column='Strand25', blank=True, null=True)  # Field name made lowercase.
    type26 = models.TextField(db_column='Type26', blank=True, null=True)  # Field name made lowercase.
    genesym26 = models.TextField(db_column='GeneSym26', blank=True, null=True)  # Field name made lowercase.
    refid26 = models.TextField(db_column='RefID26', blank=True, null=True)  # Field name made lowercase.
    strand26 = models.TextField(db_column='Strand26', blank=True, null=True)  # Field name made lowercase.
    type27 = models.TextField(db_column='Type27', blank=True, null=True)  # Field name made lowercase.
    genesym27 = models.TextField(db_column='GeneSym27', blank=True, null=True)  # Field name made lowercase.
    refid27 = models.TextField(db_column='RefID27', blank=True, null=True)  # Field name made lowercase.
    strand27 = models.TextField(db_column='Strand27', blank=True, null=True)  # Field name made lowercase.
    type28 = models.TextField(db_column='Type28', blank=True, null=True)  # Field name made lowercase.
    genesym28 = models.TextField(db_column='GeneSym28', blank=True, null=True)  # Field name made lowercase.
    refid28 = models.TextField(db_column='RefID28', blank=True, null=True)  # Field name made lowercase.
    strand28 = models.TextField(db_column='Strand28', blank=True, null=True)  # Field name made lowercase.
    type29 = models.TextField(db_column='Type29', blank=True, null=True)  # Field name made lowercase.
    genesym29 = models.TextField(db_column='GeneSym29', blank=True, null=True)  # Field name made lowercase.
    refid29 = models.TextField(db_column='RefID29', blank=True, null=True)  # Field name made lowercase.
    strand29 = models.TextField(db_column='Strand29', blank=True, null=True)  # Field name made lowercase.
    type30 = models.TextField(db_column='Type30', blank=True, null=True)  # Field name made lowercase.
    genesym30 = models.TextField(db_column='GeneSym30', blank=True, null=True)  # Field name made lowercase.
    refid30 = models.TextField(db_column='RefID30', blank=True, null=True)  # Field name made lowercase.
    strand30 = models.TextField(db_column='Strand30', blank=True, null=True)  # Field name made lowercase.
    type31 = models.TextField(db_column='Type31', blank=True, null=True)  # Field name made lowercase.
    genesym31 = models.TextField(db_column='GeneSym31', blank=True, null=True)  # Field name made lowercase.
    refid31 = models.TextField(db_column='RefID31', blank=True, null=True)  # Field name made lowercase.
    strand31 = models.TextField(db_column='Strand31', blank=True, null=True)  # Field name made lowercase.
    type32 = models.TextField(db_column='Type32', blank=True, null=True)  # Field name made lowercase.
    genesym32 = models.TextField(db_column='GeneSym32', blank=True, null=True)  # Field name made lowercase.
    refid32 = models.TextField(db_column='RefID32', blank=True, null=True)  # Field name made lowercase.
    strand32 = models.TextField(db_column='Strand32', blank=True, null=True)  # Field name made lowercase.
    type33 = models.TextField(db_column='Type33', blank=True, null=True)  # Field name made lowercase.
    genesym33 = models.TextField(db_column='GeneSym33', blank=True, null=True)  # Field name made lowercase.
    refid33 = models.TextField(db_column='RefID33', blank=True, null=True)  # Field name made lowercase.
    strand33 = models.TextField(db_column='Strand33', blank=True, null=True)  # Field name made lowercase.
    type34 = models.TextField(db_column='Type34', blank=True, null=True)  # Field name made lowercase.
    genesym34 = models.TextField(db_column='GeneSym34', blank=True, null=True)  # Field name made lowercase.
    refid34 = models.TextField(db_column='RefID34', blank=True, null=True)  # Field name made lowercase.
    strand34 = models.TextField(db_column='Strand34', blank=True, null=True)  # Field name made lowercase.
    type35 = models.TextField(db_column='Type35', blank=True, null=True)  # Field name made lowercase.
    genesym35 = models.TextField(db_column='GeneSym35', blank=True, null=True)  # Field name made lowercase.
    refid35 = models.TextField(db_column='RefID35', blank=True, null=True)  # Field name made lowercase.
    strand35 = models.TextField(db_column='Strand35', blank=True, null=True)  # Field name made lowercase.
    type36 = models.TextField(db_column='Type36', blank=True, null=True)  # Field name made lowercase.
    genesym36 = models.TextField(db_column='GeneSym36', blank=True, null=True)  # Field name made lowercase.
    refid36 = models.TextField(db_column='RefID36', blank=True, null=True)  # Field name made lowercase.
    strand36 = models.TextField(db_column='Strand36', blank=True, null=True)  # Field name made lowercase.
    type37 = models.TextField(db_column='Type37', blank=True, null=True)  # Field name made lowercase.
    genesym37 = models.TextField(db_column='GeneSym37', blank=True, null=True)  # Field name made lowercase.
    refid37 = models.TextField(db_column='RefID37', blank=True, null=True)  # Field name made lowercase.
    strand37 = models.TextField(db_column='Strand37', blank=True, null=True)  # Field name made lowercase.
    type38 = models.TextField(db_column='Type38', blank=True, null=True)  # Field name made lowercase.
    genesym38 = models.TextField(db_column='GeneSym38', blank=True, null=True)  # Field name made lowercase.
    refid38 = models.TextField(db_column='RefID38', blank=True, null=True)  # Field name made lowercase.
    strand38 = models.TextField(db_column='Strand38', blank=True, null=True)  # Field name made lowercase.
    type39 = models.TextField(db_column='Type39', blank=True, null=True)  # Field name made lowercase.
    genesym39 = models.TextField(db_column='GeneSym39', blank=True, null=True)  # Field name made lowercase.
    refid39 = models.TextField(db_column='RefID39', blank=True, null=True)  # Field name made lowercase.
    strand39 = models.TextField(db_column='Strand39', blank=True, null=True)  # Field name made lowercase.
    type40 = models.TextField(db_column='Type40', blank=True, null=True)  # Field name made lowercase.
    genesym40 = models.TextField(db_column='GeneSym40', blank=True, null=True)  # Field name made lowercase.
    refid40 = models.TextField(db_column='RefID40', blank=True, null=True)  # Field name made lowercase.
    strand40 = models.TextField(db_column='Strand40', blank=True, null=True)  # Field name made lowercase.
    type41 = models.TextField(db_column='Type41', blank=True, null=True)  # Field name made lowercase.
    genesym41 = models.TextField(db_column='GeneSym41', blank=True, null=True)  # Field name made lowercase.
    refid41 = models.TextField(db_column='RefID41', blank=True, null=True)  # Field name made lowercase.
    strand41 = models.TextField(db_column='Strand41', blank=True, null=True)  # Field name made lowercase.
    type42 = models.TextField(db_column='Type42', blank=True, null=True)  # Field name made lowercase.
    genesym42 = models.TextField(db_column='GeneSym42', blank=True, null=True)  # Field name made lowercase.
    refid42 = models.TextField(db_column='RefID42', blank=True, null=True)  # Field name made lowercase.
    strand42 = models.TextField(db_column='Strand42', blank=True, null=True)  # Field name made lowercase.
    type43 = models.TextField(db_column='Type43', blank=True, null=True)  # Field name made lowercase.
    genesym43 = models.TextField(db_column='GeneSym43', blank=True, null=True)  # Field name made lowercase.
    refid43 = models.TextField(db_column='RefID43', blank=True, null=True)  # Field name made lowercase.
    strand43 = models.TextField(db_column='Strand43', blank=True, null=True)  # Field name made lowercase.
    type44 = models.TextField(db_column='Type44', blank=True, null=True)  # Field name made lowercase.
    genesym44 = models.TextField(db_column='GeneSym44', blank=True, null=True)  # Field name made lowercase.
    refid44 = models.TextField(db_column='RefID44', blank=True, null=True)  # Field name made lowercase.
    strand44 = models.TextField(db_column='Strand44', blank=True, null=True)  # Field name made lowercase.
    type45 = models.TextField(db_column='Type45', blank=True, null=True)  # Field name made lowercase.
    genesym45 = models.TextField(db_column='GeneSym45', blank=True, null=True)  # Field name made lowercase.
    refid45 = models.TextField(db_column='RefID45', blank=True, null=True)  # Field name made lowercase.
    strand45 = models.TextField(db_column='Strand45', blank=True, null=True)  # Field name made lowercase.
    type46 = models.TextField(db_column='Type46', blank=True, null=True)  # Field name made lowercase.
    genesym46 = models.TextField(db_column='GeneSym46', blank=True, null=True)  # Field name made lowercase.
    refid46 = models.TextField(db_column='RefID46', blank=True, null=True)  # Field name made lowercase.
    strand46 = models.TextField(db_column='Strand46', blank=True, null=True)  # Field name made lowercase.
    type47 = models.TextField(db_column='Type47', blank=True, null=True)  # Field name made lowercase.
    genesym47 = models.TextField(db_column='GeneSym47', blank=True, null=True)  # Field name made lowercase.
    refid47 = models.TextField(db_column='RefID47', blank=True, null=True)  # Field name made lowercase.
    strand47 = models.TextField(db_column='Strand47', blank=True, null=True)  # Field name made lowercase.
    type48 = models.TextField(db_column='Type48', blank=True, null=True)  # Field name made lowercase.
    genesym48 = models.TextField(db_column='GeneSym48', blank=True, null=True)  # Field name made lowercase.
    refid48 = models.TextField(db_column='RefID48', blank=True, null=True)  # Field name made lowercase.
    strand48 = models.TextField(db_column='Strand48', blank=True, null=True)  # Field name made lowercase.
    type49 = models.TextField(db_column='Type49', blank=True, null=True)  # Field name made lowercase.
    genesym49 = models.TextField(db_column='GeneSym49', blank=True, null=True)  # Field name made lowercase.
    refid49 = models.TextField(db_column='RefID49', blank=True, null=True)  # Field name made lowercase.
    strand49 = models.TextField(db_column='Strand49', blank=True, null=True)  # Field name made lowercase.
    type50 = models.TextField(db_column='Type50', blank=True, null=True)  # Field name made lowercase.
    genesym50 = models.TextField(db_column='GeneSym50', blank=True, null=True)  # Field name made lowercase.
    refid50 = models.TextField(db_column='RefID50', blank=True, null=True)  # Field name made lowercase.
    strand50 = models.TextField(db_column='Strand50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dm3'


class Hg38(models.Model):
    cgid = models.CharField(db_column='CGID', primary_key=True, max_length=255)  # Field name made lowercase.
    chrom = models.TextField()
    cgistart = models.IntegerField(db_column='CGIstart')  # Field name made lowercase.
    cgiend = models.IntegerField(db_column='CGIend')  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    pergc = models.FloatField(db_column='perGC')  # Field name made lowercase.
    obsexp = models.FloatField(db_column='ObsExp')  # Field name made lowercase.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase.
    genesym1 = models.TextField(db_column='GeneSym1', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.TextField(db_column='RefID1', blank=True, null=True)  # Field name made lowercase.
    strand1 = models.TextField(db_column='Strand1', blank=True, null=True)  # Field name made lowercase.
    type2 = models.TextField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    genesym2 = models.TextField(db_column='GeneSym2', blank=True, null=True)  # Field name made lowercase.
    refid2 = models.TextField(db_column='RefID2', blank=True, null=True)  # Field name made lowercase.
    strand2 = models.TextField(db_column='Strand2', blank=True, null=True)  # Field name made lowercase.
    type3 = models.TextField(db_column='Type3', blank=True, null=True)  # Field name made lowercase.
    genesym3 = models.TextField(db_column='GeneSym3', blank=True, null=True)  # Field name made lowercase.
    refid3 = models.TextField(db_column='RefID3', blank=True, null=True)  # Field name made lowercase.
    strand3 = models.TextField(db_column='Strand3', blank=True, null=True)  # Field name made lowercase.
    type4 = models.TextField(db_column='Type4', blank=True, null=True)  # Field name made lowercase.
    genesym4 = models.TextField(db_column='GeneSym4', blank=True, null=True)  # Field name made lowercase.
    refid4 = models.TextField(db_column='RefID4', blank=True, null=True)  # Field name made lowercase.
    strand4 = models.TextField(db_column='Strand4', blank=True, null=True)  # Field name made lowercase.
    type5 = models.TextField(db_column='Type5', blank=True, null=True)  # Field name made lowercase.
    genesym5 = models.TextField(db_column='GeneSym5', blank=True, null=True)  # Field name made lowercase.
    refid5 = models.TextField(db_column='RefID5', blank=True, null=True)  # Field name made lowercase.
    strand5 = models.TextField(db_column='Strand5', blank=True, null=True)  # Field name made lowercase.
    type6 = models.TextField(db_column='Type6', blank=True, null=True)  # Field name made lowercase.
    genesym6 = models.TextField(db_column='GeneSym6', blank=True, null=True)  # Field name made lowercase.
    refid6 = models.TextField(db_column='RefID6', blank=True, null=True)  # Field name made lowercase.
    strand6 = models.TextField(db_column='Strand6', blank=True, null=True)  # Field name made lowercase.
    type7 = models.TextField(db_column='Type7', blank=True, null=True)  # Field name made lowercase.
    genesym7 = models.TextField(db_column='GeneSym7', blank=True, null=True)  # Field name made lowercase.
    refid7 = models.TextField(db_column='RefID7', blank=True, null=True)  # Field name made lowercase.
    strand7 = models.TextField(db_column='Strand7', blank=True, null=True)  # Field name made lowercase.
    type8 = models.TextField(db_column='Type8', blank=True, null=True)  # Field name made lowercase.
    genesym8 = models.TextField(db_column='GeneSym8', blank=True, null=True)  # Field name made lowercase.
    refid8 = models.TextField(db_column='RefID8', blank=True, null=True)  # Field name made lowercase.
    strand8 = models.TextField(db_column='Strand8', blank=True, null=True)  # Field name made lowercase.
    type9 = models.TextField(db_column='Type9', blank=True, null=True)  # Field name made lowercase.
    genesym9 = models.TextField(db_column='GeneSym9', blank=True, null=True)  # Field name made lowercase.
    refid9 = models.TextField(db_column='RefID9', blank=True, null=True)  # Field name made lowercase.
    strand9 = models.TextField(db_column='Strand9', blank=True, null=True)  # Field name made lowercase.
    type10 = models.TextField(db_column='Type10', blank=True, null=True)  # Field name made lowercase.
    genesym10 = models.TextField(db_column='GeneSym10', blank=True, null=True)  # Field name made lowercase.
    refid10 = models.TextField(db_column='RefID10', blank=True, null=True)  # Field name made lowercase.
    strand10 = models.TextField(db_column='Strand10', blank=True, null=True)  # Field name made lowercase.
    type11 = models.TextField(db_column='Type11', blank=True, null=True)  # Field name made lowercase.
    genesym11 = models.TextField(db_column='GeneSym11', blank=True, null=True)  # Field name made lowercase.
    refid11 = models.TextField(db_column='RefID11', blank=True, null=True)  # Field name made lowercase.
    strand11 = models.TextField(db_column='Strand11', blank=True, null=True)  # Field name made lowercase.
    type12 = models.TextField(db_column='Type12', blank=True, null=True)  # Field name made lowercase.
    genesym12 = models.TextField(db_column='GeneSym12', blank=True, null=True)  # Field name made lowercase.
    refid12 = models.TextField(db_column='RefID12', blank=True, null=True)  # Field name made lowercase.
    strand12 = models.TextField(db_column='Strand12', blank=True, null=True)  # Field name made lowercase.
    type13 = models.TextField(db_column='Type13', blank=True, null=True)  # Field name made lowercase.
    genesym13 = models.TextField(db_column='GeneSym13', blank=True, null=True)  # Field name made lowercase.
    refid13 = models.TextField(db_column='RefID13', blank=True, null=True)  # Field name made lowercase.
    strand13 = models.TextField(db_column='Strand13', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hg38'


class Mm10(models.Model):
    cgid = models.CharField(db_column='CGID', primary_key=True, max_length=255)  # Field name made lowercase.
    chrom = models.TextField()
    cgistart = models.IntegerField(db_column='CGIstart')  # Field name made lowercase.
    cgiend = models.IntegerField(db_column='CGIend')  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    pergc = models.FloatField(db_column='perGC')  # Field name made lowercase.
    obsexp = models.FloatField(db_column='ObsExp')  # Field name made lowercase.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase.
    genesym1 = models.TextField(db_column='GeneSym1', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.TextField(db_column='RefID1', blank=True, null=True)  # Field name made lowercase.
    strand1 = models.TextField(db_column='Strand1', blank=True, null=True)  # Field name made lowercase.
    type2 = models.TextField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    genesym2 = models.TextField(db_column='GeneSym2', blank=True, null=True)  # Field name made lowercase.
    refid2 = models.TextField(db_column='RefID2', blank=True, null=True)  # Field name made lowercase.
    strand2 = models.TextField(db_column='Strand2', blank=True, null=True)  # Field name made lowercase.
    type3 = models.TextField(db_column='Type3', blank=True, null=True)  # Field name made lowercase.
    genesym3 = models.TextField(db_column='GeneSym3', blank=True, null=True)  # Field name made lowercase.
    refid3 = models.TextField(db_column='RefID3', blank=True, null=True)  # Field name made lowercase.
    strand3 = models.TextField(db_column='Strand3', blank=True, null=True)  # Field name made lowercase.
    type4 = models.TextField(db_column='Type4', blank=True, null=True)  # Field name made lowercase.
    genesym4 = models.TextField(db_column='GeneSym4', blank=True, null=True)  # Field name made lowercase.
    refid4 = models.TextField(db_column='RefID4', blank=True, null=True)  # Field name made lowercase.
    strand4 = models.TextField(db_column='Strand4', blank=True, null=True)  # Field name made lowercase.
    type5 = models.TextField(db_column='Type5', blank=True, null=True)  # Field name made lowercase.
    genesym5 = models.TextField(db_column='GeneSym5', blank=True, null=True)  # Field name made lowercase.
    refid5 = models.TextField(db_column='RefID5', blank=True, null=True)  # Field name made lowercase.
    strand5 = models.TextField(db_column='Strand5', blank=True, null=True)  # Field name made lowercase.
    type6 = models.TextField(db_column='Type6', blank=True, null=True)  # Field name made lowercase.
    genesym6 = models.TextField(db_column='GeneSym6', blank=True, null=True)  # Field name made lowercase.
    refid6 = models.TextField(db_column='RefID6', blank=True, null=True)  # Field name made lowercase.
    strand6 = models.TextField(db_column='Strand6', blank=True, null=True)  # Field name made lowercase.
    type7 = models.TextField(db_column='Type7', blank=True, null=True)  # Field name made lowercase.
    genesym7 = models.TextField(db_column='GeneSym7', blank=True, null=True)  # Field name made lowercase.
    refid7 = models.TextField(db_column='RefID7', blank=True, null=True)  # Field name made lowercase.
    strand7 = models.TextField(db_column='Strand7', blank=True, null=True)  # Field name made lowercase.
    type8 = models.TextField(db_column='Type8', blank=True, null=True)  # Field name made lowercase.
    genesym8 = models.TextField(db_column='GeneSym8', blank=True, null=True)  # Field name made lowercase.
    refid8 = models.TextField(db_column='RefID8', blank=True, null=True)  # Field name made lowercase.
    strand8 = models.TextField(db_column='Strand8', blank=True, null=True)  # Field name made lowercase.
    type9 = models.TextField(db_column='Type9', blank=True, null=True)  # Field name made lowercase.
    genesym9 = models.TextField(db_column='GeneSym9', blank=True, null=True)  # Field name made lowercase.
    refid9 = models.TextField(db_column='RefID9', blank=True, null=True)  # Field name made lowercase.
    strand9 = models.TextField(db_column='Strand9', blank=True, null=True)  # Field name made lowercase.
    type10 = models.TextField(db_column='Type10', blank=True, null=True)  # Field name made lowercase.
    genesym10 = models.TextField(db_column='GeneSym10', blank=True, null=True)  # Field name made lowercase.
    refid10 = models.TextField(db_column='RefID10', blank=True, null=True)  # Field name made lowercase.
    strand10 = models.TextField(db_column='Strand10', blank=True, null=True)  # Field name made lowercase.
    type11 = models.TextField(db_column='Type11', blank=True, null=True)  # Field name made lowercase.
    genesym11 = models.TextField(db_column='GeneSym11', blank=True, null=True)  # Field name made lowercase.
    refid11 = models.TextField(db_column='RefID11', blank=True, null=True)  # Field name made lowercase.
    strand11 = models.TextField(db_column='Strand11', blank=True, null=True)  # Field name made lowercase.
    type12 = models.TextField(db_column='Type12', blank=True, null=True)  # Field name made lowercase.
    genesym12 = models.TextField(db_column='GeneSym12', blank=True, null=True)  # Field name made lowercase.
    refid12 = models.TextField(db_column='RefID12', blank=True, null=True)  # Field name made lowercase.
    strand12 = models.TextField(db_column='Strand12', blank=True, null=True)  # Field name made lowercase.
    type13 = models.TextField(db_column='Type13', blank=True, null=True)  # Field name made lowercase.
    genesym13 = models.TextField(db_column='GeneSym13', blank=True, null=True)  # Field name made lowercase.
    refid13 = models.TextField(db_column='RefID13', blank=True, null=True)  # Field name made lowercase.
    strand13 = models.TextField(db_column='Strand13', blank=True, null=True)  # Field name made lowercase.
    type14 = models.TextField(db_column='Type14', blank=True, null=True)  # Field name made lowercase.
    genesym14 = models.TextField(db_column='GeneSym14', blank=True, null=True)  # Field name made lowercase.
    refid14 = models.TextField(db_column='RefID14', blank=True, null=True)  # Field name made lowercase.
    strand14 = models.TextField(db_column='Strand14', blank=True, null=True)  # Field name made lowercase.
    type15 = models.TextField(db_column='Type15', blank=True, null=True)  # Field name made lowercase.
    genesym15 = models.TextField(db_column='GeneSym15', blank=True, null=True)  # Field name made lowercase.
    refid15 = models.TextField(db_column='RefID15', blank=True, null=True)  # Field name made lowercase.
    strand15 = models.TextField(db_column='Strand15', blank=True, null=True)  # Field name made lowercase.
    type16 = models.TextField(db_column='Type16', blank=True, null=True)  # Field name made lowercase.
    genesym16 = models.TextField(db_column='GeneSym16', blank=True, null=True)  # Field name made lowercase.
    refid16 = models.TextField(db_column='RefID16', blank=True, null=True)  # Field name made lowercase.
    strand16 = models.TextField(db_column='Strand16', blank=True, null=True)  # Field name made lowercase.
    type17 = models.TextField(db_column='Type17', blank=True, null=True)  # Field name made lowercase.
    genesym17 = models.TextField(db_column='GeneSym17', blank=True, null=True)  # Field name made lowercase.
    refid17 = models.TextField(db_column='RefID17', blank=True, null=True)  # Field name made lowercase.
    strand17 = models.TextField(db_column='Strand17', blank=True, null=True)  # Field name made lowercase.
    type18 = models.TextField(db_column='Type18', blank=True, null=True)  # Field name made lowercase.
    genesym18 = models.TextField(db_column='GeneSym18', blank=True, null=True)  # Field name made lowercase.
    refid18 = models.TextField(db_column='RefID18', blank=True, null=True)  # Field name made lowercase.
    strand18 = models.TextField(db_column='Strand18', blank=True, null=True)  # Field name made lowercase.
    type19 = models.TextField(db_column='Type19', blank=True, null=True)  # Field name made lowercase.
    genesym19 = models.TextField(db_column='GeneSym19', blank=True, null=True)  # Field name made lowercase.
    refid19 = models.TextField(db_column='RefID19', blank=True, null=True)  # Field name made lowercase.
    strand19 = models.TextField(db_column='Strand19', blank=True, null=True)  # Field name made lowercase.
    type20 = models.TextField(db_column='Type20', blank=True, null=True)  # Field name made lowercase.
    genesym20 = models.TextField(db_column='GeneSym20', blank=True, null=True)  # Field name made lowercase.
    refid20 = models.TextField(db_column='RefID20', blank=True, null=True)  # Field name made lowercase.
    strand20 = models.TextField(db_column='Strand20', blank=True, null=True)  # Field name made lowercase.
    type21 = models.TextField(db_column='Type21', blank=True, null=True)  # Field name made lowercase.
    genesym21 = models.TextField(db_column='GeneSym21', blank=True, null=True)  # Field name made lowercase.
    refid21 = models.TextField(db_column='RefID21', blank=True, null=True)  # Field name made lowercase.
    strand21 = models.TextField(db_column='Strand21', blank=True, null=True)  # Field name made lowercase.
    type22 = models.TextField(db_column='Type22', blank=True, null=True)  # Field name made lowercase.
    genesym22 = models.TextField(db_column='GeneSym22', blank=True, null=True)  # Field name made lowercase.
    refid22 = models.TextField(db_column='RefID22', blank=True, null=True)  # Field name made lowercase.
    strand22 = models.TextField(db_column='Strand22', blank=True, null=True)  # Field name made lowercase.
    type23 = models.TextField(db_column='Type23', blank=True, null=True)  # Field name made lowercase.
    genesym23 = models.TextField(db_column='GeneSym23', blank=True, null=True)  # Field name made lowercase.
    refid23 = models.TextField(db_column='RefID23', blank=True, null=True)  # Field name made lowercase.
    strand23 = models.TextField(db_column='Strand23', blank=True, null=True)  # Field name made lowercase.
    type24 = models.TextField(db_column='Type24', blank=True, null=True)  # Field name made lowercase.
    genesym24 = models.TextField(db_column='GeneSym24', blank=True, null=True)  # Field name made lowercase.
    refid24 = models.TextField(db_column='RefID24', blank=True, null=True)  # Field name made lowercase.
    strand24 = models.TextField(db_column='Strand24', blank=True, null=True)  # Field name made lowercase.
    type25 = models.TextField(db_column='Type25', blank=True, null=True)  # Field name made lowercase.
    genesym25 = models.TextField(db_column='GeneSym25', blank=True, null=True)  # Field name made lowercase.
    refid25 = models.TextField(db_column='RefID25', blank=True, null=True)  # Field name made lowercase.
    strand25 = models.TextField(db_column='Strand25', blank=True, null=True)  # Field name made lowercase.
    type26 = models.TextField(db_column='Type26', blank=True, null=True)  # Field name made lowercase.
    genesym26 = models.TextField(db_column='GeneSym26', blank=True, null=True)  # Field name made lowercase.
    refid26 = models.TextField(db_column='RefID26', blank=True, null=True)  # Field name made lowercase.
    strand26 = models.TextField(db_column='Strand26', blank=True, null=True)  # Field name made lowercase.
    type27 = models.TextField(db_column='Type27', blank=True, null=True)  # Field name made lowercase.
    genesym27 = models.TextField(db_column='GeneSym27', blank=True, null=True)  # Field name made lowercase.
    refid27 = models.TextField(db_column='RefID27', blank=True, null=True)  # Field name made lowercase.
    strand27 = models.TextField(db_column='Strand27', blank=True, null=True)  # Field name made lowercase.
    type28 = models.TextField(db_column='Type28', blank=True, null=True)  # Field name made lowercase.
    genesym28 = models.TextField(db_column='GeneSym28', blank=True, null=True)  # Field name made lowercase.
    refid28 = models.TextField(db_column='RefID28', blank=True, null=True)  # Field name made lowercase.
    strand28 = models.TextField(db_column='Strand28', blank=True, null=True)  # Field name made lowercase.
    type29 = models.TextField(db_column='Type29', blank=True, null=True)  # Field name made lowercase.
    genesym29 = models.TextField(db_column='GeneSym29', blank=True, null=True)  # Field name made lowercase.
    refid29 = models.TextField(db_column='RefID29', blank=True, null=True)  # Field name made lowercase.
    strand29 = models.TextField(db_column='Strand29', blank=True, null=True)  # Field name made lowercase.
    type30 = models.TextField(db_column='Type30', blank=True, null=True)  # Field name made lowercase.
    genesym30 = models.TextField(db_column='GeneSym30', blank=True, null=True)  # Field name made lowercase.
    refid30 = models.TextField(db_column='RefID30', blank=True, null=True)  # Field name made lowercase.
    strand30 = models.TextField(db_column='Strand30', blank=True, null=True)  # Field name made lowercase.
    type31 = models.TextField(db_column='Type31', blank=True, null=True)  # Field name made lowercase.
    genesym31 = models.TextField(db_column='GeneSym31', blank=True, null=True)  # Field name made lowercase.
    refid31 = models.TextField(db_column='RefID31', blank=True, null=True)  # Field name made lowercase.
    strand31 = models.TextField(db_column='Strand31', blank=True, null=True)  # Field name made lowercase.
    type32 = models.TextField(db_column='Type32', blank=True, null=True)  # Field name made lowercase.
    genesym32 = models.TextField(db_column='GeneSym32', blank=True, null=True)  # Field name made lowercase.
    refid32 = models.TextField(db_column='RefID32', blank=True, null=True)  # Field name made lowercase.
    strand32 = models.TextField(db_column='Strand32', blank=True, null=True)  # Field name made lowercase.
    type33 = models.TextField(db_column='Type33', blank=True, null=True)  # Field name made lowercase.
    genesym33 = models.TextField(db_column='GeneSym33', blank=True, null=True)  # Field name made lowercase.
    refid33 = models.TextField(db_column='RefID33', blank=True, null=True)  # Field name made lowercase.
    strand33 = models.TextField(db_column='Strand33', blank=True, null=True)  # Field name made lowercase.
    type34 = models.TextField(db_column='Type34', blank=True, null=True)  # Field name made lowercase.
    genesym34 = models.TextField(db_column='GeneSym34', blank=True, null=True)  # Field name made lowercase.
    refid34 = models.TextField(db_column='RefID34', blank=True, null=True)  # Field name made lowercase.
    strand34 = models.TextField(db_column='Strand34', blank=True, null=True)  # Field name made lowercase.
    type35 = models.TextField(db_column='Type35', blank=True, null=True)  # Field name made lowercase.
    genesym35 = models.TextField(db_column='GeneSym35', blank=True, null=True)  # Field name made lowercase.
    refid35 = models.TextField(db_column='RefID35', blank=True, null=True)  # Field name made lowercase.
    strand35 = models.TextField(db_column='Strand35', blank=True, null=True)  # Field name made lowercase.
    type36 = models.TextField(db_column='Type36', blank=True, null=True)  # Field name made lowercase.
    genesym36 = models.TextField(db_column='GeneSym36', blank=True, null=True)  # Field name made lowercase.
    refid36 = models.TextField(db_column='RefID36', blank=True, null=True)  # Field name made lowercase.
    strand36 = models.TextField(db_column='Strand36', blank=True, null=True)  # Field name made lowercase.
    type37 = models.TextField(db_column='Type37', blank=True, null=True)  # Field name made lowercase.
    genesym37 = models.TextField(db_column='GeneSym37', blank=True, null=True)  # Field name made lowercase.
    refid37 = models.TextField(db_column='RefID37', blank=True, null=True)  # Field name made lowercase.
    strand37 = models.TextField(db_column='Strand37', blank=True, null=True)  # Field name made lowercase.
    type38 = models.TextField(db_column='Type38', blank=True, null=True)  # Field name made lowercase.
    genesym38 = models.TextField(db_column='GeneSym38', blank=True, null=True)  # Field name made lowercase.
    refid38 = models.TextField(db_column='RefID38', blank=True, null=True)  # Field name made lowercase.
    strand38 = models.TextField(db_column='Strand38', blank=True, null=True)  # Field name made lowercase.
    type39 = models.TextField(db_column='Type39', blank=True, null=True)  # Field name made lowercase.
    genesym39 = models.TextField(db_column='GeneSym39', blank=True, null=True)  # Field name made lowercase.
    refid39 = models.TextField(db_column='RefID39', blank=True, null=True)  # Field name made lowercase.
    strand39 = models.TextField(db_column='Strand39', blank=True, null=True)  # Field name made lowercase.
    type40 = models.TextField(db_column='Type40', blank=True, null=True)  # Field name made lowercase.
    genesym40 = models.TextField(db_column='GeneSym40', blank=True, null=True)  # Field name made lowercase.
    refid40 = models.TextField(db_column='RefID40', blank=True, null=True)  # Field name made lowercase.
    strand40 = models.TextField(db_column='Strand40', blank=True, null=True)  # Field name made lowercase.
    type41 = models.TextField(db_column='Type41', blank=True, null=True)  # Field name made lowercase.
    genesym41 = models.TextField(db_column='GeneSym41', blank=True, null=True)  # Field name made lowercase.
    refid41 = models.TextField(db_column='RefID41', blank=True, null=True)  # Field name made lowercase.
    strand41 = models.TextField(db_column='Strand41', blank=True, null=True)  # Field name made lowercase.
    type42 = models.TextField(db_column='Type42', blank=True, null=True)  # Field name made lowercase.
    genesym42 = models.TextField(db_column='GeneSym42', blank=True, null=True)  # Field name made lowercase.
    refid42 = models.TextField(db_column='RefID42', blank=True, null=True)  # Field name made lowercase.
    strand42 = models.TextField(db_column='Strand42', blank=True, null=True)  # Field name made lowercase.
    type43 = models.TextField(db_column='Type43', blank=True, null=True)  # Field name made lowercase.
    genesym43 = models.TextField(db_column='GeneSym43', blank=True, null=True)  # Field name made lowercase.
    refid43 = models.TextField(db_column='RefID43', blank=True, null=True)  # Field name made lowercase.
    strand43 = models.TextField(db_column='Strand43', blank=True, null=True)  # Field name made lowercase.
    type44 = models.TextField(db_column='Type44', blank=True, null=True)  # Field name made lowercase.
    genesym44 = models.TextField(db_column='GeneSym44', blank=True, null=True)  # Field name made lowercase.
    refid44 = models.TextField(db_column='RefID44', blank=True, null=True)  # Field name made lowercase.
    strand44 = models.TextField(db_column='Strand44', blank=True, null=True)  # Field name made lowercase.
    type45 = models.TextField(db_column='Type45', blank=True, null=True)  # Field name made lowercase.
    genesym45 = models.TextField(db_column='GeneSym45', blank=True, null=True)  # Field name made lowercase.
    refid45 = models.TextField(db_column='RefID45', blank=True, null=True)  # Field name made lowercase.
    strand45 = models.TextField(db_column='Strand45', blank=True, null=True)  # Field name made lowercase.
    type46 = models.TextField(db_column='Type46', blank=True, null=True)  # Field name made lowercase.
    genesym46 = models.TextField(db_column='GeneSym46', blank=True, null=True)  # Field name made lowercase.
    refid46 = models.TextField(db_column='RefID46', blank=True, null=True)  # Field name made lowercase.
    strand46 = models.TextField(db_column='Strand46', blank=True, null=True)  # Field name made lowercase.
    type47 = models.TextField(db_column='Type47', blank=True, null=True)  # Field name made lowercase.
    genesym47 = models.TextField(db_column='GeneSym47', blank=True, null=True)  # Field name made lowercase.
    refid47 = models.TextField(db_column='RefID47', blank=True, null=True)  # Field name made lowercase.
    strand47 = models.TextField(db_column='Strand47', blank=True, null=True)  # Field name made lowercase.
    type48 = models.TextField(db_column='Type48', blank=True, null=True)  # Field name made lowercase.
    genesym48 = models.TextField(db_column='GeneSym48', blank=True, null=True)  # Field name made lowercase.
    refid48 = models.TextField(db_column='RefID48', blank=True, null=True)  # Field name made lowercase.
    strand48 = models.TextField(db_column='Strand48', blank=True, null=True)  # Field name made lowercase.
    type49 = models.TextField(db_column='Type49', blank=True, null=True)  # Field name made lowercase.
    genesym49 = models.TextField(db_column='GeneSym49', blank=True, null=True)  # Field name made lowercase.
    refid49 = models.TextField(db_column='RefID49', blank=True, null=True)  # Field name made lowercase.
    strand49 = models.TextField(db_column='Strand49', blank=True, null=True)  # Field name made lowercase.
    type50 = models.TextField(db_column='Type50', blank=True, null=True)  # Field name made lowercase.
    genesym50 = models.TextField(db_column='GeneSym50', blank=True, null=True)  # Field name made lowercase.
    refid50 = models.TextField(db_column='RefID50', blank=True, null=True)  # Field name made lowercase.
    strand50 = models.TextField(db_column='Strand50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mm10'


class Rn6(models.Model):
    cgid = models.CharField(db_column='CGID', primary_key=True, max_length=255)  # Field name made lowercase.
    chrom = models.TextField()
    cgistart = models.IntegerField(db_column='CGIstart')  # Field name made lowercase.
    cgiend = models.IntegerField(db_column='CGIend')  # Field name made lowercase.
    length = models.IntegerField()
    pergc = models.FloatField(db_column='perGC')  # Field name made lowercase.
    obsexp = models.FloatField(db_column='ObsExp')  # Field name made lowercase.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase.
    genesym1 = models.TextField(db_column='GeneSym1', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.TextField(db_column='RefID1', blank=True, null=True)  # Field name made lowercase.
    strand1 = models.TextField(db_column='Strand1', blank=True, null=True)  # Field name made lowercase.
    type2 = models.TextField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    genesym2 = models.TextField(db_column='GeneSym2', blank=True, null=True)  # Field name made lowercase.
    refid2 = models.TextField(db_column='RefID2', blank=True, null=True)  # Field name made lowercase.
    strand2 = models.TextField(db_column='Strand2', blank=True, null=True)  # Field name made lowercase.
    type3 = models.TextField(db_column='Type3', blank=True, null=True)  # Field name made lowercase.
    genesym3 = models.TextField(db_column='GeneSym3', blank=True, null=True)  # Field name made lowercase.
    refid3 = models.TextField(db_column='RefID3', blank=True, null=True)  # Field name made lowercase.
    strand3 = models.TextField(db_column='Strand3', blank=True, null=True)  # Field name made lowercase.
    type4 = models.TextField(db_column='Type4', blank=True, null=True)  # Field name made lowercase.
    genesym4 = models.TextField(db_column='GeneSym4', blank=True, null=True)  # Field name made lowercase.
    refid4 = models.TextField(db_column='RefID4', blank=True, null=True)  # Field name made lowercase.
    strand4 = models.TextField(db_column='Strand4', blank=True, null=True)  # Field name made lowercase.
    type5 = models.TextField(db_column='Type5', blank=True, null=True)  # Field name made lowercase.
    genesym5 = models.TextField(db_column='GeneSym5', blank=True, null=True)  # Field name made lowercase.
    refid5 = models.TextField(db_column='RefID5', blank=True, null=True)  # Field name made lowercase.
    strand5 = models.TextField(db_column='Strand5', blank=True, null=True)  # Field name made lowercase.
    type6 = models.TextField(db_column='Type6', blank=True, null=True)  # Field name made lowercase.
    genesym6 = models.TextField(db_column='GeneSym6', blank=True, null=True)  # Field name made lowercase.
    refid6 = models.TextField(db_column='RefID6', blank=True, null=True)  # Field name made lowercase.
    strand6 = models.TextField(db_column='Strand6', blank=True, null=True)  # Field name made lowercase.
    type7 = models.TextField(db_column='Type7', blank=True, null=True)  # Field name made lowercase.
    genesym7 = models.TextField(db_column='GeneSym7', blank=True, null=True)  # Field name made lowercase.
    refid7 = models.TextField(db_column='RefID7', blank=True, null=True)  # Field name made lowercase.
    strand7 = models.TextField(db_column='Strand7', blank=True, null=True)  # Field name made lowercase.
    type8 = models.TextField(db_column='Type8', blank=True, null=True)  # Field name made lowercase.
    genesym8 = models.TextField(db_column='GeneSym8', blank=True, null=True)  # Field name made lowercase.
    refid8 = models.TextField(db_column='RefID8', blank=True, null=True)  # Field name made lowercase.
    strand8 = models.TextField(db_column='Strand8', blank=True, null=True)  # Field name made lowercase.
    type9 = models.TextField(db_column='Type9', blank=True, null=True)  # Field name made lowercase.
    genesym9 = models.TextField(db_column='GeneSym9', blank=True, null=True)  # Field name made lowercase.
    refid9 = models.TextField(db_column='RefID9', blank=True, null=True)  # Field name made lowercase.
    strand9 = models.TextField(db_column='Strand9', blank=True, null=True)  # Field name made lowercase.
    type10 = models.TextField(db_column='Type10', blank=True, null=True)  # Field name made lowercase.
    genesym10 = models.TextField(db_column='GeneSym10', blank=True, null=True)  # Field name made lowercase.
    refid10 = models.TextField(db_column='RefID10', blank=True, null=True)  # Field name made lowercase.
    strand10 = models.TextField(db_column='Strand10', blank=True, null=True)  # Field name made lowercase.
    type11 = models.TextField(db_column='Type11', blank=True, null=True)  # Field name made lowercase.
    genesym11 = models.TextField(db_column='GeneSym11', blank=True, null=True)  # Field name made lowercase.
    refid11 = models.TextField(db_column='RefID11', blank=True, null=True)  # Field name made lowercase.
    strand11 = models.TextField(db_column='Strand11', blank=True, null=True)  # Field name made lowercase.
    type12 = models.TextField(db_column='Type12', blank=True, null=True)  # Field name made lowercase.
    genesym12 = models.TextField(db_column='GeneSym12', blank=True, null=True)  # Field name made lowercase.
    refid12 = models.TextField(db_column='RefID12', blank=True, null=True)  # Field name made lowercase.
    strand12 = models.TextField(db_column='Strand12', blank=True, null=True)  # Field name made lowercase.
    type13 = models.TextField(db_column='Type13', blank=True, null=True)  # Field name made lowercase.
    genesym13 = models.TextField(db_column='GeneSym13', blank=True, null=True)  # Field name made lowercase.
    refid13 = models.TextField(db_column='RefID13', blank=True, null=True)  # Field name made lowercase.
    strand13 = models.TextField(db_column='Strand13', blank=True, null=True)  # Field name made lowercase.
    type14 = models.TextField(db_column='Type14', blank=True, null=True)  # Field name made lowercase.
    genesym14 = models.TextField(db_column='GeneSym14', blank=True, null=True)  # Field name made lowercase.
    refid14 = models.TextField(db_column='RefID14', blank=True, null=True)  # Field name made lowercase.
    strand14 = models.TextField(db_column='Strand14', blank=True, null=True)  # Field name made lowercase.
    type15 = models.TextField(db_column='Type15', blank=True, null=True)  # Field name made lowercase.
    genesym15 = models.TextField(db_column='GeneSym15', blank=True, null=True)  # Field name made lowercase.
    refid15 = models.TextField(db_column='RefID15', blank=True, null=True)  # Field name made lowercase.
    strand15 = models.TextField(db_column='Strand15', blank=True, null=True)  # Field name made lowercase.
    type16 = models.TextField(db_column='Type16', blank=True, null=True)  # Field name made lowercase.
    genesym16 = models.TextField(db_column='GeneSym16', blank=True, null=True)  # Field name made lowercase.
    refid16 = models.TextField(db_column='RefID16', blank=True, null=True)  # Field name made lowercase.
    strand16 = models.TextField(db_column='Strand16', blank=True, null=True)  # Field name made lowercase.
    type17 = models.TextField(db_column='Type17', blank=True, null=True)  # Field name made lowercase.
    genesym17 = models.TextField(db_column='GeneSym17', blank=True, null=True)  # Field name made lowercase.
    refid17 = models.TextField(db_column='RefID17', blank=True, null=True)  # Field name made lowercase.
    strand17 = models.TextField(db_column='Strand17', blank=True, null=True)  # Field name made lowercase.
    type18 = models.TextField(db_column='Type18', blank=True, null=True)  # Field name made lowercase.
    genesym18 = models.TextField(db_column='GeneSym18', blank=True, null=True)  # Field name made lowercase.
    refid18 = models.TextField(db_column='RefID18', blank=True, null=True)  # Field name made lowercase.
    strand18 = models.TextField(db_column='Strand18', blank=True, null=True)  # Field name made lowercase.
    type19 = models.TextField(db_column='Type19', blank=True, null=True)  # Field name made lowercase.
    genesym19 = models.TextField(db_column='GeneSym19', blank=True, null=True)  # Field name made lowercase.
    refid19 = models.TextField(db_column='RefID19', blank=True, null=True)  # Field name made lowercase.
    strand19 = models.TextField(db_column='Strand19', blank=True, null=True)  # Field name made lowercase.
    type20 = models.TextField(db_column='Type20', blank=True, null=True)  # Field name made lowercase.
    genesym20 = models.TextField(db_column='GeneSym20', blank=True, null=True)  # Field name made lowercase.
    refid20 = models.TextField(db_column='RefID20', blank=True, null=True)  # Field name made lowercase.
    strand20 = models.TextField(db_column='Strand20', blank=True, null=True)  # Field name made lowercase.
    type21 = models.TextField(db_column='Type21', blank=True, null=True)  # Field name made lowercase.
    genesym21 = models.TextField(db_column='GeneSym21', blank=True, null=True)  # Field name made lowercase.
    refid21 = models.TextField(db_column='RefID21', blank=True, null=True)  # Field name made lowercase.
    strand21 = models.TextField(db_column='Strand21', blank=True, null=True)  # Field name made lowercase.
    type22 = models.TextField(db_column='Type22', blank=True, null=True)  # Field name made lowercase.
    genesym22 = models.TextField(db_column='GeneSym22', blank=True, null=True)  # Field name made lowercase.
    refid22 = models.TextField(db_column='RefID22', blank=True, null=True)  # Field name made lowercase.
    strand22 = models.TextField(db_column='Strand22', blank=True, null=True)  # Field name made lowercase.
    type23 = models.TextField(db_column='Type23', blank=True, null=True)  # Field name made lowercase.
    genesym23 = models.TextField(db_column='GeneSym23', blank=True, null=True)  # Field name made lowercase.
    refid23 = models.TextField(db_column='RefID23', blank=True, null=True)  # Field name made lowercase.
    strand23 = models.TextField(db_column='Strand23', blank=True, null=True)  # Field name made lowercase.
    type24 = models.TextField(db_column='Type24', blank=True, null=True)  # Field name made lowercase.
    genesym24 = models.TextField(db_column='GeneSym24', blank=True, null=True)  # Field name made lowercase.
    refid24 = models.TextField(db_column='RefID24', blank=True, null=True)  # Field name made lowercase.
    strand24 = models.TextField(db_column='Strand24', blank=True, null=True)  # Field name made lowercase.
    type25 = models.TextField(db_column='Type25', blank=True, null=True)  # Field name made lowercase.
    genesym25 = models.TextField(db_column='GeneSym25', blank=True, null=True)  # Field name made lowercase.
    refid25 = models.TextField(db_column='RefID25', blank=True, null=True)  # Field name made lowercase.
    strand25 = models.TextField(db_column='Strand25', blank=True, null=True)  # Field name made lowercase.
    type26 = models.TextField(db_column='Type26', blank=True, null=True)  # Field name made lowercase.
    genesym26 = models.TextField(db_column='GeneSym26', blank=True, null=True)  # Field name made lowercase.
    refid26 = models.TextField(db_column='RefID26', blank=True, null=True)  # Field name made lowercase.
    strand26 = models.TextField(db_column='Strand26', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rn6'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)