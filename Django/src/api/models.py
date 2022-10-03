from django.db import models
import numpy as np
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from datetime import datetime




# Create your models here.

		


   	
   	
class Attack(models.Model):
	wlan_tag_length = models.CharField(max_length=32, null=True)
	wlan_country_info_fnm = models.CharField(max_length=32, null=True)
	wlan_da = models.CharField(max_length=32, null=True)
	wlan_sa = models.CharField(max_length=32, null=True)
	wlan_bssid = models.CharField(max_length=32, null=True)
	ip_src = models.CharField(max_length=32, null=True)
	ip_dst = models.CharField(max_length=32, null=True)
	wlan_fixed_reason_code =models.CharField(max_length=32, null=True)
	radiotap_channel_freq = models.CharField(max_length=32, null=True)
	udp_length = models.CharField(max_length=32, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.wlan_tag_length
		
	@classmethod
	def preprocessDataAndPredict(self, wlan_tag_length, wlan_country_info_fnm, wlan_da, wlan_sa, wlan_bssid, ip_src, ip_dst, wlan_fixed_reason_code, radiotap_channel_freq, udp_length):
		#we want a pandas dataframe for our model
		inputData = {'wlan_tag_length': [wlan_tag_length], 'wlan_country_info_fnm': [wlan_country_info_fnm],'wlan_da': [wlan_da], 'wlan_sa': [wlan_sa],'wlan_bssid': [wlan_bssid], 'ip_src': [ip_src],'ip_dst': [ip_dst], 'wlan_fixed_reason_code':[wlan_fixed_reason_code],'radiotap_channel_freq': [radiotap_channel_freq], 'udp_length': [udp_length]}
		test_data = pd.DataFrame(data=inputData)
		
		
		#open our model
		with open('./api/smallmodel.joblib', 'rb') as joblib_file:
    			trained_model = joblib.load(joblib_file)
		
    		
		#predict
		prediction = trained_model.predict(test_data)
		return prediction
		    		
		
	
	def save(self, *args, **kwargs):
        	super().save(*args, **kwargs)
        	prediction = self.preprocessDataAndPredict(self.wlan_tag_length, self.wlan_country_info_fnm, self.wlan_da, self.wlan_sa, self.wlan_bssid, self.ip_src, self.ip_dst, self.wlan_fixed_reason_code, self.radiotap_channel_freq, self.udp_length)
        	if(prediction==1):
        		Prediction.objects.create(AD=self,predicted=True)
        	elif(prediction==0):
        		Prediction.objects.create(AD=self,predicted=False)
        		
class Prediction(models.Model):
   	AD = models.OneToOneField(Attack, on_delete=models.CASCADE)
   	predicted=models.BooleanField(default=True)
	
		




